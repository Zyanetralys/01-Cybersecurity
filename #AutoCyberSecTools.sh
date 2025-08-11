#!/bin/bash

# KaliToolsManager v2.0 - Herramienta completa de gestión para Kali Linux
# Gestión avanzada de herramientas de seguridad ofensiva y defensiva

set -euo pipefail

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m'

# Variables globales
LOGFILE="/var/log/kali-tools-manager.log"
TOOLS_DIR="/opt/tools"
BACKUP_DIR="/opt/backups"
CONFIG_FILE="/etc/kali-tools-manager.conf"

# Banner principal
show_banner() {
    clear
    echo -e "${RED}╔══════════════════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${RED}║${WHITE}                         KaliToolsManager v2.0                                ${RED}║${NC}"
    echo -e "${RED}║${CYAN}                    Gestión Avanzada de Herramientas                         ${RED}║${NC}"
    echo -e "${RED}║${YELLOW}                       Sistema de Arsenal Táctico                           ${RED}║${NC}"
    echo -e "${RED}╚══════════════════════════════════════════════════════════════════════════════╝${NC}"
    echo
}

# Logging función
log_action() {
    local action="$1"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $action" >> "$LOGFILE"
}

# Verificación de privilegios
check_privileges() {
    if [[ $EUID -ne 0 ]]; then
        echo -e "${RED}[!] Este script requiere privilegios de root${NC}"
        echo -e "${YELLOW}[*] Ejecuta con: sudo $0${NC}"
        exit 1
    fi
}

# Inicialización del sistema
initialize_system() {
    echo -e "${BLUE}[*] Inicializando sistema...${NC}"
    
    # Crear directorios necesarios
    mkdir -p "$TOOLS_DIR" "$BACKUP_DIR" "$(dirname "$LOGFILE")"
    
    # Verificar conexión a internet
    if ! ping -c 1 8.8.8.8 &> /dev/null; then
        echo -e "${RED}[!] Sin conexión a internet${NC}"
        exit 1
    fi
    
    # Actualizar keyring
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3B4FE6ACC0B21F32 &> /dev/null || true
    
    log_action "Sistema inicializado correctamente"
    echo -e "${GREEN}[✓] Sistema inicializado${NC}"
}

# Definición de herramientas por categorías
declare -A RECON_TOOLS=(
    ["amass"]="amass"
    ["theharvester"]="theharvester"
    ["recon-ng"]="recon-ng"
    ["nmap"]="nmap"
    ["fping"]="fping"
    ["searchsploit"]="exploitdb"
    ["shodan"]="python3-shodan"
    ["maltego"]="maltego"
    ["spiderfoot"]="spiderfoot"
    ["sublist3r"]="sublist3r"
    ["dnsenum"]="dnsenum"
    ["dnsrecon"]="dnsrecon"
    ["whatweb"]="whatweb"
    ["nikto"]="nikto"
)

declare -A VULN_TOOLS=(
    ["openvas"]="openvas"
    ["nikto"]="nikto"
    ["wpscan"]="wpscan"
    ["nuclei"]="nuclei"
    ["burpsuite"]="burpsuite"
    ["arachni"]="arachni"
    ["skipfish"]="skipfish"
    ["osquery"]="osquery"
)

declare -A EXPLOIT_TOOLS=(
    ["metasploit-framework"]="metasploit-framework"
    ["empire"]="powershell-empire"
    ["mimikatz"]="mimikatz"
    ["crackmapexec"]="crackmapexec"
    ["impacket"]="impacket-scripts"
    ["responder"]="responder"
    ["chisel"]="chisel"
    ["bloodhound"]="bloodhound"
    ["evil-winrm"]="evil-winrm"
)

declare -A CRACK_TOOLS=(
    ["hydra"]="hydra"
    ["john"]="john"
    ["hashcat"]="hashcat"
    ["cewl"]="cewl"
    ["crunch"]="crunch"
    ["medusa"]="medusa"
    ["patator"]="patator"
)

declare -A WEB_TOOLS=(
    ["sqlmap"]="sqlmap"
    ["ffuf"]="ffuf"
    ["gobuster"]="gobuster"
    ["dirsearch"]="dirsearch"
    ["awscli"]="awscli"
    ["dirb"]="dirb"
    ["commix"]="commix"
)

declare -A FORENSICS_TOOLS=(
    ["wireshark"]="wireshark"
    ["volatility3"]="volatility3"
    ["ghidra"]="ghidra"
    ["radare2"]="radare2"
    ["autopsy"]="autopsy"
    ["tcpdump"]="tcpdump"
    ["networkminer"]="networkminer"
    ["sleuthkit"]="sleuthkit"
)

declare -A EXFIL_TOOLS=(
    ["exiftool"]="exiftool"
    ["steghide"]="steghide"
    ["gpg"]="gnupg"
    ["rclone"]="rclone"
    ["syncthing"]="syncthing"
    ["rsync"]="rsync"
)

declare -A PAYLOAD_TOOLS=(
    ["msfvenom"]="metasploit-framework"
    ["veil"]="veil"
    ["unicorn"]="unicorn-magic"
    ["donut"]="donut-shellcode"
)

# Instalación de herramientas especiales (fuentes alternativas)
install_special_tools() {
    local category="$1"
    
    case $category in
        "recon")
            # FOCA (manual install)
            if [[ ! -d "$TOOLS_DIR/FOCA" ]]; then
                echo -e "${BLUE}[*] Instalando FOCA...${NC}"
                cd "$TOOLS_DIR"
                git clone https://github.com/ElevenPaths/FOCA.git
            fi
            
            # Censys CLI
            pip3 install censys &> /dev/null || true
            
            # Shodan CLI
            pip3 install shodan &> /dev/null || true
            ;;
            
        "exploit")
            # Sliver C2
            if [[ ! -f "/usr/local/bin/sliver-server" ]]; then
                echo -e "${BLUE}[*] Instalando Sliver C2...${NC}"
                curl https://sliver.sh/install|sudo bash &> /dev/null || true
            fi
            
            # Havoc C2
            if [[ ! -d "$TOOLS_DIR/Havoc" ]]; then
                echo -e "${BLUE}[*] Instalando Havoc C2...${NC}"
                cd "$TOOLS_DIR"
                git clone https://github.com/HavocFramework/Havoc.git
                cd Havoc && make &> /dev/null || true
            fi
            
            # Covenant
            if [[ ! -d "$TOOLS_DIR/Covenant" ]]; then
                echo -e "${BLUE}[*] Instalando Covenant...${NC}"
                cd "$TOOLS_DIR"
                git clone --recurse-submodules https://github.com/cobbr/Covenant
            fi
            
            # Pupy RAT
            if [[ ! -d "$TOOLS_DIR/pupy" ]]; then
                echo -e "${BLUE}[*] Instalando Pupy RAT...${NC}"
                cd "$TOOLS_DIR"
                git clone --recursive https://github.com/n1nj4sec/pupy.git
            fi
            
            # DNSCat2
            if [[ ! -d "$TOOLS_DIR/dnscat2" ]]; then
                echo -e "${BLUE}[*] Instalando DNSCat2...${NC}"
                cd "$TOOLS_DIR"
                git clone https://github.com/iagox86/dnscat2.git
                cd dnscat2/server && gem install bundler && bundle install &> /dev/null || true
            fi
            
            # Ligolo-ng
            if [[ ! -f "/usr/local/bin/ligolo-ng" ]]; then
                echo -e "${BLUE}[*] Instalando Ligolo-ng...${NC}"
                cd /tmp
                LATEST=$(curl -s "https://api.github.com/repos/nicocha30/ligolo-ng/releases/latest" | grep -Po '"tag_name": "\K.*?(?=")')
                wget -q "https://github.com/nicocha30/ligolo-ng/releases/download/${LATEST}/ligolo-ng_agent_${LATEST#v}_Linux_64bit.tar.gz"
                tar -xzf ligolo-ng_agent_${LATEST#v}_Linux_64bit.tar.gz
                mv agent /usr/local/bin/ligolo-ng
                chmod +x /usr/local/bin/ligolo-ng
            fi
            ;;
            
        "web")
            # CloudBrute
            if [[ ! -d "$TOOLS_DIR/CloudBrute" ]]; then
                echo -e "${BLUE}[*] Instalando CloudBrute...${NC}"
                cd "$TOOLS_DIR"
                git clone https://github.com/0xsha/CloudBrute.git
                cd CloudBrute && go build . &> /dev/null || true
            fi
            
            # Pacu (AWS)
            pip3 install pacu &> /dev/null || true
            
            # ScoutSuite
            pip3 install scoutsuite &> /dev/null || true
            
            # AzureHound
            if [[ ! -f "/usr/local/bin/azurehound" ]]; then
                echo -e "${BLUE}[*] Instalando AzureHound...${NC}"
                cd /tmp
                LATEST=$(curl -s "https://api.github.com/repos/BloodHoundAD/AzureHound/releases/latest" | grep -Po '"tag_name": "\K.*?(?=")')
                wget -q "https://github.com/BloodHoundAD/AzureHound/releases/download/${LATEST}/azurehound-linux-amd64.zip"
                unzip -q azurehound-linux-amd64.zip
                mv azurehound /usr/local/bin/
                chmod +x /usr/local/bin/azurehound
            fi
            ;;
            
        "payload")
            # Veil-Evasion
            if [[ ! -d "$TOOLS_DIR/Veil" ]]; then
                echo -e "${BLUE}[*] Instalando Veil...${NC}"
                cd "$TOOLS_DIR"
                git clone https://github.com/Veil-Framework/Veil.git
                cd Veil && ./config/setup.sh --force --silent &> /dev/null || true
            fi
            
            # ScareCrow
            if [[ ! -d "$TOOLS_DIR/ScareCrow" ]]; then
                echo -e "${BLUE}[*] Instalando ScareCrow...${NC}"
                cd "$TOOLS_DIR"
                git clone https://github.com/optiv/ScareCrow.git
                cd ScareCrow && go build ScareCrow.go &> /dev/null || true
            fi
            
            # GreatSCT
            if [[ ! -d "$TOOLS_DIR/GreatSCT" ]]; then
                echo -e "${BLUE}[*] Instalando GreatSCT...${NC}"
                cd "$TOOLS_DIR"
                git clone https://github.com/GreatSCT/GreatSCT.git
                cd GreatSCT/setup && ./setup.sh &> /dev/null || true
            fi
            
            # Magic Unicorn
            if [[ ! -d "$TOOLS_DIR/unicorn" ]]; then
                echo -e "${BLUE}[*] Instalando Magic Unicorn...${NC}"
                cd "$TOOLS_DIR"
                git clone https://github.com/trustedsec/unicorn.git
            fi
            
            # PayloadsAllTheThings
            if [[ ! -d "$TOOLS_DIR/PayloadsAllTheThings" ]]; then
                echo -e "${BLUE}[*] Descargando PayloadsAllTheThings...${NC}"
                cd "$TOOLS_DIR"
                git clone https://github.com/swisskyrepo/PayloadsAllTheThings.git
            fi
            
            # SharpShooter
            if [[ ! -d "$TOOLS_DIR/SharpShooter" ]]; then
                echo -e "${BLUE}[*] Instalando SharpShooter...${NC}"
                cd "$TOOLS_DIR"
                git clone https://github.com/mdsecactivebreach/SharpShooter.git
            fi
            ;;
            
        "forensics")
            # Zeek
            if ! command -v zeek &> /dev/null; then
                echo -e "${BLUE}[*] Instalando Zeek...${NC}"
                echo 'deb http://download.opensuse.org/repositories/security:/zeek/Debian_11/ /' > /etc/apt/sources.list.d/security:zeek.list
                curl -fsSL https://download.opensuse.org/repositories/security:zeek/Debian_11/Release.key | gpg --dearmor > /etc/apt/trusted.gpg.d/security_zeek.gpg
                apt update &> /dev/null && apt install -y zeek &> /dev/null || true
            fi
            
            # MFTDump
            if [[ ! -d "$TOOLS_DIR/MFTDump" ]]; then
                echo -e "${BLUE}[*] Instalando MFTDump...${NC}"
                cd "$TOOLS_DIR"
                git clone https://github.com/jschicht/MftDump.git MFTDump
            fi
            ;;
    esac
}

# Función para instalar herramientas de una categoría
install_category() {
    local category="$1"
    local -n tools_ref=$2
    local category_name="$3"
    
    echo -e "${PURPLE}[*] Instalando herramientas de $category_name...${NC}"
    
    # Actualizar repositorios antes de instalar
    apt update &> /dev/null
    
    local failed_tools=()
    local success_count=0
    
    for tool_name in "${!tools_ref[@]}"; do
        local package_name="${tools_ref[$tool_name]}"
        echo -e "${BLUE}[*] Instalando $tool_name...${NC}"
        
        if apt install -y "$package_name" &> /dev/null; then
            echo -e "${GREEN}[✓] $tool_name instalado correctamente${NC}"
            log_action "Instalado: $tool_name"
            ((success_count++))
        else
            echo -e "${YELLOW}[!] Falló la instalación de $tool_name${NC}"
            failed_tools+=("$tool_name")
        fi
    done
    
    # Instalar herramientas especiales para esta categoría
    install_special_tools "$category"
    
    echo -e "${GREEN}[✓] Categoría $category_name completada: $success_count herramientas instaladas${NC}"
    
    if [[ ${#failed_tools[@]} -gt 0 ]]; then
        echo -e "${YELLOW}[!] Herramientas que fallaron: ${failed_tools[*]}${NC}"
    fi
}

# Menú de selección de categorías
category_menu() {
    while true; do
        show_banner
        echo -e "${WHITE}╔════════════════════════════════════════════════════════════════╗${NC}"
        echo -e "${WHITE}║${CYAN}                    SELECCIÓN DE CATEGORÍAS                     ${WHITE}║${NC}"
        echo -e "${WHITE}╠════════════════════════════════════════════════════════════════╣${NC}"
        echo -e "${WHITE}║ ${YELLOW}1)${NC} 🔍 Reconocimiento y OSINT                                ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}2)${NC} 🛡️  Escaneo y Análisis de Vulnerabilidades               ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}3)${NC} ⚔️  Explotación y Post-Explotación                       ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}4)${NC} 🔓 Cracking y Fuerza Bruta                               ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}5)${NC} 🌐 Web & Cloud Offensive                                 ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}6)${NC} 📡 Análisis de Tráfico y Forense                         ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}7)${NC} 📦 Exfiltración y Manipulación de Datos                  ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}8)${NC} 💣 Payloads                                               ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}9)${NC} 🎯 Instalar TODAS las categorías                          ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}0)${NC} ← Volver al menú principal                               ${WHITE}║${NC}"
        echo -e "${WHITE}╚════════════════════════════════════════════════════════════════╝${NC}"
        echo
        echo -ne "${WHITE}Selecciona una opción: ${NC}"
        
        read -r choice
        
        case $choice in
            1) install_category "recon" RECON_TOOLS "Reconocimiento y OSINT" ;;
            2) install_category "vuln" VULN_TOOLS "Escaneo y Análisis de Vulnerabilidades" ;;
            3) install_category "exploit" EXPLOIT_TOOLS "Explotación y Post-Explotación" ;;
            4) install_category "crack" CRACK_TOOLS "Cracking y Fuerza Bruta" ;;
            5) install_category "web" WEB_TOOLS "Web & Cloud Offensive" ;;
            6) install_category "forensics" FORENSICS_TOOLS "Análisis de Tráfico y Forense" ;;
            7) install_category "exfil" EXFIL_TOOLS "Exfiltración y Manipulación de Datos" ;;
            8) install_category "payload" PAYLOAD_TOOLS "Payloads" ;;
            9) install_all_categories ;;
            0) return ;;
            *) echo -e "${RED}[!] Opción inválida${NC}" ;;
        esac
        
        if [[ $choice != 0 ]]; then
            echo -e "\n${GREEN}[*] Presiona Enter para continuar...${NC}"
            read -r
        fi
    done
}

# Instalar todas las categorías
install_all_categories() {
    echo -e "${RED}[!] INSTALACIÓN COMPLETA INICIADA${NC}"
    echo -e "${YELLOW}[*] Esto puede tomar considerable tiempo...${NC}"
    echo -ne "${WHITE}¿Continuar? [y/N]: ${NC}"
    read -r confirm
    
    if [[ ! $confirm =~ ^[Yy]$ ]]; then
        return
    fi
    
    local start_time=$(date +%s)
    
    install_category "recon" RECON_TOOLS "Reconocimiento y OSINT"
    install_category "vuln" VULN_TOOLS "Escaneo y Análisis de Vulnerabilidades"
    install_category "exploit" EXPLOIT_TOOLS "Explotación y Post-Explotación"
    install_category "crack" CRACK_TOOLS "Cracking y Fuerza Bruta"
    install_category "web" WEB_TOOLS "Web & Cloud Offensive"
    install_category "forensics" FORENSICS_TOOLS "Análisis de Tráfico y Forense"
    install_category "exfil" EXFIL_TOOLS "Exfiltración y Manipulación de Datos"
    install_category "payload" PAYLOAD_TOOLS "Payloads"
    
    local end_time=$(date +%s)
    local duration=$((end_time - start_time))
    
    echo -e "${GREEN}[✓] INSTALACIÓN COMPLETA FINALIZADA${NC}"
    echo -e "${CYAN}[*] Tiempo total: $((duration / 60)) minutos y $((duration % 60)) segundos${NC}"
    
    log_action "Instalación completa finalizada en ${duration}s"
}

# Menú de herramientas individuales
individual_menu() {
    local all_tools=()
    
    # Recopilar todas las herramientas
    for tool in "${!RECON_TOOLS[@]}"; do all_tools+=("$tool [RECON]"); done
    for tool in "${!VULN_TOOLS[@]}"; do all_tools+=("$tool [VULN]"); done
    for tool in "${!EXPLOIT_TOOLS[@]}"; do all_tools+=("$tool [EXPLOIT]"); done
    for tool in "${!CRACK_TOOLS[@]}"; do all_tools+=("$tool [CRACK]"); done
    for tool in "${!WEB_TOOLS[@]}"; do all_tools+=("$tool [WEB]"); done
    for tool in "${!FORENSICS_TOOLS[@]}"; do all_tools+=("$tool [FORENSICS]"); done
    for tool in "${!EXFIL_TOOLS[@]}"; do all_tools+=("$tool [EXFIL]"); done
    for tool in "${!PAYLOAD_TOOLS[@]}"; do all_tools+=("$tool [PAYLOAD]"); done
    
    # Ordenar alfabéticamente
    IFS=$'\n' sorted_tools=($(sort <<<"${all_tools[*]}"))
    unset IFS
    
    while true; do
        show_banner
        echo -e "${WHITE}╔════════════════════════════════════════════════════════════════╗${NC}"
        echo -e "${WHITE}║${CYAN}                 INSTALACIÓN INDIVIDUAL                         ${WHITE}║${NC}"
        echo -e "${WHITE}╠════════════════════════════════════════════════════════════════╣${NC}"
        
        local count=0
        for tool in "${sorted_tools[@]}"; do
            ((count++))
            printf "${WHITE}║ ${YELLOW}%2d)${NC} %-55s ${WHITE}║${NC}\n" "$count" "$tool"
        done
        
        echo -e "${WHITE}║ ${YELLOW} 0)${NC} ← Volver al menú principal                               ${WHITE}║${NC}"
        echo -e "${WHITE}╚════════════════════════════════════════════════════════════════╝${NC}"
        echo
        echo -ne "${WHITE}Selecciona una herramienta (número): ${NC}"
        
        read -r choice
        
        if [[ $choice == "0" ]]; then
            return
        elif [[ $choice =~ ^[0-9]+$ ]] && [[ $choice -ge 1 && $choice -le ${#sorted_tools[@]} ]]; then
            local selected_tool="${sorted_tools[$((choice-1))]}"
            local tool_name=$(echo "$selected_tool" | cut -d' ' -f1)
            
            echo -e "${BLUE}[*] Instalando $tool_name...${NC}"
            
            # Determinar la categoría y instalar
            local installed=false
            for category_tools in RECON_TOOLS VULN_TOOLS EXPLOIT_TOOLS CRACK_TOOLS WEB_TOOLS FORENSICS_TOOLS EXFIL_TOOLS PAYLOAD_TOOLS; do
                declare -n ref=$category_tools
                if [[ -n "${ref[$tool_name]:-}" ]]; then
                    if apt install -y "${ref[$tool_name]}" &> /dev/null; then
                        echo -e "${GREEN}[✓] $tool_name instalado correctamente${NC}"
                        log_action "Instalado individualmente: $tool_name"
                        installed=true
                    else
                        echo -e "${RED}[!] Error al instalar $tool_name${NC}"
                    fi
                    break
                fi
            done
            
            if [[ $installed == false ]]; then
                echo -e "${RED}[!] Herramienta no encontrada${NC}"
            fi
            
            echo -e "\n${GREEN}[*] Presiona Enter para continuar...${NC}"
            read -r
        else
            echo -e "${RED}[!] Opción inválida${NC}"
            sleep 1
        fi
    done
}

# Sistema de actualización completa
full_system_update() {
    echo -e "${BLUE}[*] Iniciando actualización completa del sistema...${NC}"
    
    local start_time=$(date +%s)
    
    echo -e "${BLUE}[*] Actualizando listas de paquetes...${NC}"
    apt update
    
    echo -e "${BLUE}[*] Actualizando sistema completo...${NC}"
    apt full-upgrade -y
    
    echo -e "${BLUE}[*] Eliminando paquetes obsoletos...${NC}"
    apt autoremove --purge -y
    
    echo -e "${BLUE}[*] Limpiando caché de paquetes...${NC}"
    apt clean
    
    echo -e "${BLUE}[*] Actualizando herramientas personalizadas...${NC}"
    if [[ -d "$TOOLS_DIR" ]]; then
        for dir in "$TOOLS_DIR"/*; do
            if [[ -d "$dir/.git" ]]; then
                echo -e "${CYAN}[*] Actualizando $(basename "$dir")...${NC}"
                cd "$dir" && git pull origin main 2>/dev/null || git pull origin master 2>/dev/null || true
            fi
        done
    fi
    
    # Actualizar utilidades de Python
    echo -e "${BLUE}[*] Actualizando herramientas de Python...${NC}"
    pip3 install --upgrade pip setuptools wheel &> /dev/null || true
    pip3 install --upgrade shodan censys pacu scoutsuite &> /dev/null || true
    
    # Actualizar base de datos de exploits
    echo -e "${BLUE}[*] Actualizando base de datos de exploits...${NC}"
    searchsploit -u &> /dev/null || true
    
    local end_time=$(date +%s)
    local duration=$((end_time - start_time))
    
    echo -e "${GREEN}[✓] Actualización completa finalizada${NC}"
    echo -e "${CYAN}[*] Tiempo total: $((duration / 60)) minutos y $((duration % 60)) segundos${NC}"
    
    log_action "Actualización completa del sistema finalizada en ${duration}s"
    
    echo -e "\n${GREEN}[*] Presiona Enter para continuar...${NC}"
    read -r
}

# Backup y restauración
backup_system() {
    echo -e "${BLUE}[*] Creando backup del sistema...${NC}"
    
    local backup_name="kali-backup-$(date +%Y%m%d-%H%M%S)"
    local backup_path="$BACKUP_DIR/$backup_name"
    
    mkdir -p "$backup_path"
    
    echo -e "${BLUE}[*] Respaldando configuraciones...${NC}"
    
    # Backup de listas de paquetes instalados
    dpkg --get-selections > "$backup_path/packages.list"
    
    # Backup de repositorios
    cp -r /etc/apt/sources.list* "$backup_path/"
    
    # Backup de herramientas personalizadas
    if [[ -d "$TOOLS_DIR" ]]; then
        tar -czf "$backup_path/custom-tools.tar.gz" -C "$TOOLS_DIR" . 2>/dev/null || true
    fi
    
    # Backup de configuraciones importantes
    mkdir -p "$backup_path/configs"
    [[ -f /etc/hosts ]] && cp /etc/hosts "$backup_path/configs/"
    [[ -f ~/.bashrc ]] && cp ~/.bashrc "$backup_path/configs/"
    [[ -f ~/.zshrc ]] && cp ~/.zshrc "$backup_path/configs/" 2>/dev/null || true
    
    # Backup de logs
    [[ -f "$LOGFILE" ]] && cp "$LOGFILE" "$backup_path/"
    
    echo -e "${GREEN}[✓] Backup completado: $backup_path${NC}"
    log_action "Backup creado: $backup_name"
    
    echo -e "\n${GREEN}[*] Presiona Enter para continuar...${NC}"
    read -r
}

# Gestión de servicios
service_management() {
    while true; do
        show_banner
        echo -e "${WHITE}╔════════════════════════════════════════════════════════════════╗${NC}"
        echo -e "${WHITE}║${CYAN}                   GESTIÓN DE SERVICIOS                         ${WHITE}║${NC}"
        echo -e "${WHITE}╠════════════════════════════════════════════════════════════════╣${NC}"
        echo -e "${WHITE}║ ${YELLOW}1)${NC} 🚀 Iniciar Metasploit RPC                               ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}2)${NC} 🛡️  Iniciar/Parar OpenVAS                                ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}3)${NC} 📡 Iniciar/Parar Wireshark (tshark)                      ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}4)${NC} 🌐 Iniciar PostgreSQL                                    ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}5)${NC} 🔍 Estado de servicios activos                           ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}6)${NC} 🔄 Reiniciar servicios de red                            ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}0)${NC} ← Volver                                                 ${WHITE}║${NC}"
        echo -e "${WHITE}╚════════════════════════════════════════════════════════════════╝${NC}"
        echo
        echo -ne "${WHITE}Selecciona una opción: ${NC}"
        
        read -r choice
        
        case $choice in
            1)
                echo -e "${BLUE}[*] Iniciando Metasploit RPC...${NC}"
                systemctl start postgresql
                msfdb init &>/dev/null || true
                echo -e "${GREEN}[✓] Metasploit RPC iniciado${NC}"
                ;;
            2)
                echo -e "${BLUE}[*] Gestionando OpenVAS...${NC}"
                if systemctl is-active --quiet openvas-manager; then
                    systemctl stop openvas-manager openvas-scanner
                    echo -e "${YELLOW}[*] OpenVAS detenido${NC}"
                else
                    systemctl start openvas-scanner openvas-manager
                    echo -e "${GREEN}[✓] OpenVAS iniciado${NC}"
                fi
                ;;
            3)
                echo -e "${BLUE}[*] Verificando tshark...${NC}"
                if pgrep -f tshark > /dev/null; then
                    pkill -f tshark
                    echo -e "${YELLOW}[*] tshark detenido${NC}"
                else
                    echo -e "${GREEN}[✓] tshark disponible${NC}"
                fi
                ;;
            4)
                echo -e "${BLUE}[*] Iniciando PostgreSQL...${NC}"
                systemctl start postgresql
                systemctl enable postgresql
                echo -e "${GREEN}[✓] PostgreSQL iniciado${NC}"
                ;;
            5)
                echo -e "${BLUE}[*] Servicios activos:${NC}"
                echo -e "${CYAN}PostgreSQL:${NC} $(systemctl is-active postgresql)"
                echo -e "${CYAN}SSH:${NC} $(systemctl is-active ssh)"
                echo -e "${CYAN}OpenVAS Manager:${NC} $(systemctl is-active openvas-manager 2>/dev/null || echo 'no instalado')"
                echo -e "${CYAN}Apache2:${NC} $(systemctl is-active apache2 2>/dev/null || echo 'no instalado')"
                ;;
            6)
                echo -e "${BLUE}[*] Reiniciando servicios de red...${NC}"
                systemctl restart networking
                systemctl restart NetworkManager
                echo -e "${GREEN}[✓] Servicios de red reiniciados${NC}"
                ;;
            0) return ;;
            *) echo -e "${RED}[!] Opción inválida${NC}" ;;
        esac
        
        if [[ $choice != 0 ]]; then
            echo -e "\n${GREEN}[*] Presiona Enter para continuar...${NC}"
            read -r
        fi
    done
}

# Configuración avanzada
advanced_config() {
    while true; do
        show_banner
        echo -e "${WHITE}╔════════════════════════════════════════════════════════════════╗${NC}"
        echo -e "${WHITE}║${CYAN}                 CONFIGURACIÓN AVANZADA                         ${WHITE}║${NC}"
        echo -e "${WHITE}╠════════════════════════════════════════════════════════════════╣${NC}"
        echo -e "${WHITE}║ ${YELLOW}1)${NC} 🔧 Configurar aliases tácticos                           ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}2)${NC} 🛡️  Configurar firewall (UFW)                            ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}3)${NC} 📁 Crear estructura de directorios                       ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}4)${NC} 🔑 Configurar SSH keys                                   ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}5)${NC} 🌐 Configurar proxychains                                ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}6)${NC} 📝 Ver logs del sistema                                  ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}0)${NC} ← Volver                                                 ${WHITE}║${NC}"
        echo -e "${WHITE}╚════════════════════════════════════════════════════════════════╝${NC}"
        echo
        echo -ne "${WHITE}Selecciona una opción: ${NC}"
        
        read -r choice
        
        case $choice in
            1) setup_aliases ;;
            2) configure_firewall ;;
            3) create_directory_structure ;;
            4) configure_ssh_keys ;;
            5) configure_proxychains ;;
            6) view_logs ;;
            0) return ;;
            *) echo -e "${RED}[!] Opción inválida${NC}" ;;
        esac
        
        if [[ $choice != 0 ]]; then
            echo -e "\n${GREEN}[*] Presiona Enter para continuar...${NC}"
            read -r
        fi
    done
}

# Configurar aliases útiles
setup_aliases() {
    echo -e "${BLUE}[*] Configurando aliases tácticos...${NC}"
    
    local alias_file="/root/.bash_aliases"
    
    cat > "$alias_file" << 'EOF'
# KaliToolsManager - Aliases Tácticos

# Reconocimiento rápido
alias quickscan='nmap -sS -O -T4'
alias fastscan='nmap -F'
alias stealthscan='nmap -sS -T1 -f'
alias vulnscan='nmap --script vuln'

# Web enumeration
alias dirfuzz='ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u'
alias webfuzz='ffuf -w /usr/share/wordlists/wfuzz/general/common.txt -u'

# Metasploit shortcuts
alias msfconsole='msfconsole -q'
alias msfdb='msfdb reinit'

# Network
alias ports='netstat -tulanp'
alias listening='lsof -i -P -n | grep LISTEN'
alias connections='netstat -an | grep ESTABLISHED'

# System
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
alias ..='cd ..'
alias ...='cd ../..'
alias h='history'
alias c='clear'

# Git shortcuts
alias gs='git status'
alias ga='git add'
alias gc='git commit'
alias gp='git push'
alias gl='git log --oneline'

# Process management
alias psg='ps aux | grep'
alias topcpu='ps auxf | sort -nr -k 3 | head -10'
alias topmem='ps auxf | sort -nr -k 4 | head -10'

# Disk usage
alias df='df -h'
alias du='du -ch'
alias free='free -m'

# Quick updates
alias update='apt update && apt upgrade'
alias install='apt install'
alias search='apt search'

# Log monitoring
alias tailauth='tail -f /var/log/auth.log'
alias tailsys='tail -f /var/log/syslog'
EOF

    echo -e "${GREEN}[✓] Aliases configurados en $alias_file${NC}"
    echo -e "${CYAN}[*] Ejecuta 'source ~/.bashrc' para activarlos${NC}"
    log_action "Aliases tácticos configurados"
}

# Configurar firewall
configure_firewall() {
    echo -e "${BLUE}[*] Configurando UFW firewall...${NC}"
    
    # Instalar UFW si no está
    apt install -y ufw &>/dev/null
    
    # Configuración básica
    ufw --force reset
    ufw default deny incoming
    ufw default allow outgoing
    
    # Permitir SSH
    ufw allow ssh
    
    # Permitir puertos comunes para herramientas
    ufw allow 80/tcp    # HTTP
    ufw allow 443/tcp   # HTTPS
    ufw allow 4444/tcp  # Metasploit default
    ufw allow 8080/tcp  # Proxy/Web alt
    ufw allow 9392/tcp  # OpenVAS
    
    # Activar firewall
    ufw --force enable
    
    echo -e "${GREEN}[✓] Firewall configurado y activado${NC}"
    ufw status verbose
    log_action "Firewall UFW configurado"
}

# Crear estructura de directorios
create_directory_structure() {
    echo -e "${BLUE}[*] Creando estructura de directorios táctica...${NC}"
    
    local base_dir="/root/arsenal"
    
    # Crear directorios principales
    mkdir -p "$base_dir"/{recon,exploits,payloads,loot,reports,wordlists,scripts}
    mkdir -p "$base_dir"/recon/{domains,ips,ports,vulns}
    mkdir -p "$base_dir"/exploits/{windows,linux,web,mobile}
    mkdir -p "$base_dir"/payloads/{shells,backdoors,persistence}
    mkdir -p "$base_dir"/loot/{credentials,hashes,files,screenshots}
    mkdir -p "$base_dir"/reports/{pentest,red-team,forensics}
    mkdir -p "$base_dir"/scripts/{automation,post-exploit,cleanup}
    
    # Crear archivos README
    for dir in "$base_dir"/*; do
        if [[ -d "$dir" ]]; then
            echo "# $(basename "$dir" | tr '[:lower:]' '[:upper:]')" > "$dir/README.md"
            echo "Directorio para $(basename "$dir")" >> "$dir/README.md"
        fi
    done
    
    # Crear script de navegación rápida
    cat > "$base_dir/navigate.sh" << 'EOF'
#!/bin/bash
# Script de navegación rápida

case $1 in
    recon) cd /root/arsenal/recon ;;
    exploits) cd /root/arsenal/exploits ;;
    payloads) cd /root/arsenal/payloads ;;
    loot) cd /root/arsenal/loot ;;
    reports) cd /root/arsenal/reports ;;
    scripts) cd /root/arsenal/scripts ;;
    *) echo "Uso: source navigate.sh [recon|exploits|payloads|loot|reports|scripts]" ;;
esac
EOF
    
    chmod +x "$base_dir/navigate.sh"
    
    echo -e "${GREEN}[✓] Estructura de directorios creada en $base_dir${NC}"
    echo -e "${CYAN}[*] Usa 'source /root/arsenal/navigate.sh <directorio>' para navegar${NC}"
    log_action "Estructura de directorios táctica creada"
}

# Configurar SSH keys
configure_ssh_keys() {
    echo -e "${BLUE}[*] Configurando SSH keys...${NC}"
    
    local ssh_dir="/root/.ssh"
    mkdir -p "$ssh_dir"
    chmod 700 "$ssh_dir"
    
    if [[ ! -f "$ssh_dir/id_rsa" ]]; then
        echo -e "${BLUE}[*] Generando nueva clave SSH...${NC}"
        ssh-keygen -t rsa -b 4096 -f "$ssh_dir/id_rsa" -N ""
        echo -e "${GREEN}[✓] Clave SSH generada${NC}"
    else
        echo -e "${YELLOW}[*] Clave SSH ya existe${NC}"
    fi
    
    # Configurar SSH config básico
    cat > "$ssh_dir/config" << 'EOF'
Host *
    ServerAliveInterval 60
    ServerAliveCountMax 3
    StrictHostKeyChecking no
    UserKnownHostsFile /dev/null
    LogLevel QUIET
EOF
    
    chmod 600 "$ssh_dir/config"
    
    echo -e "${GREEN}[✓] SSH configurado${NC}"
    echo -e "${CYAN}[*] Clave pública:${NC}"
    cat "$ssh_dir/id_rsa.pub"
    log_action "SSH keys configuradas"
}

# Configurar proxychains
configure_proxychains() {
    echo -e "${BLUE}[*] Configurando proxychains...${NC}"
    
    apt install -y proxychains4 &>/dev/null
    
    # Backup de configuración original
    [[ -f /etc/proxychains4.conf ]] && cp /etc/proxychains4.conf /etc/proxychains4.conf.bak
    
    cat > /etc/proxychains4.conf << 'EOF'
# Proxychains-NG config
strict_chain
proxy_dns
remote_dns_subnet 224
tcp_read_time_out 15000
tcp_connect_time_out 8000
localnet 127.0.0.0/255.0.0.0
localnet 10.0.0.0/255.0.0.0
localnet 172.16.0.0/255.240.0.0
localnet 192.168.0.0/255.255.0.0

[ProxyList]
# Tor
socks5 127.0.0.1 9050

# Add your proxies here
# Example: socks5 127.0.0.1 1080
EOF
    
    echo -e "${GREEN}[✓] Proxychains configurado${NC}"
    echo -e "${CYAN}[*] Edita /etc/proxychains4.conf para añadir tus proxies${NC}"
    log_action "Proxychains configurado"
}

# Ver logs del sistema
view_logs() {
    echo -e "${BLUE}[*] Mostrando logs del KaliToolsManager...${NC}"
    
    if [[ -f "$LOGFILE" ]]; then
        echo -e "${CYAN}=== ÚLTIMAS 20 ENTRADAS ===${NC}"
        tail -20 "$LOGFILE"
        echo
        echo -e "${CYAN}=== ESTADÍSTICAS ===${NC}"
        echo -e "${YELLOW}Total de entradas:${NC} $(wc -l < "$LOGFILE")"
        echo -e "${YELLOW}Instalaciones:${NC} $(grep -c "Instalado:" "$LOGFILE" 2>/dev/null || echo 0)"
        echo -e "${YELLOW}Actualizaciones:${NC} $(grep -c "Actualización" "$LOGFILE" 2>/dev/null || echo 0)"
        echo -e "${YELLOW}Primer registro:${NC} $(head -1 "$LOGFILE" 2>/dev/null | cut -d']' -f1 | tr -d '[' || echo 'N/A')"
        echo -e "${YELLOW}Último registro:${NC} $(tail -1 "$LOGFILE" 2>/dev/null | cut -d']' -f1 | tr -d '[' || echo 'N/A')"
    else
        echo -e "${YELLOW}[!] No hay logs disponibles${NC}"
    fi
}

# Menú principal
main_menu() {
    while true; do
        show_banner
        echo -e "${WHITE}╔════════════════════════════════════════════════════════════════╗${NC}"
        echo -e "${WHITE}║${CYAN}                        MENÚ PRINCIPAL                           ${WHITE}║${NC}"
        echo -e "${WHITE}╠════════════════════════════════════════════════════════════════╣${NC}"
        echo -e "${WHITE}║ ${YELLOW}1)${NC} 📦 Instalar por categorías                               ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}2)${NC} 🔧 Instalar herramienta individual                       ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}3)${NC} 🚀 Actualización completa del sistema                    ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}4)${NC} 📊 Estado del sistema                                    ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}5)${NC} 🛡️  Gestión de servicios                                 ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}6)${NC} ⚙️  Configuración avanzada                               ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}7)${NC} 💾 Crear backup del sistema                              ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}8)${NC} 📋 Mostrar herramientas disponibles                      ${WHITE}║${NC}"
        echo -e "${WHITE}║ ${YELLOW}9)${NC} ❌ Salir                                                 ${WHITE}║${NC}"
        echo -e "${WHITE}╚════════════════════════════════════════════════════════════════╝${NC}"
        echo
        echo -ne "${WHITE}Selecciona una opción: ${NC}"
        
        read -r choice
        
        case $choice in
            1) category_menu ;;
            2) individual_menu ;;
            3) full_system_update ;;
            4) system_status ;;
            5) service_management ;;
            6) advanced_config ;;
            7) backup_system ;;
            8) show_available_tools ;;
            9) exit_program ;;
            *) echo -e "${RED}[!] Opción inválida${NC}" ;;
        esac
    done
}

# Mostrar herramientas disponibles
show_available_tools() {
    show_banner
    echo -e "${WHITE}╔════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${WHITE}║${CYAN}                   HERRAMIENTAS DISPONIBLES                      ${WHITE}║${NC}"
    echo -e "${WHITE}╚════════════════════════════════════════════════════════════════╝${NC}"
    
    echo -e "\n${RED}🔍 RECONOCIMIENTO Y OSINT${NC}"
    for tool in "${!RECON_TOOLS[@]}"; do
        echo -e "  ${CYAN}•${NC} $tool"
    done
    
    echo -e "\n${YELLOW}🛡️ ESCANEO Y ANÁLISIS DE VULNERABILIDADES${NC}"
    for tool in "${!VULN_TOOLS[@]}"; do
        echo -e "  ${CYAN}•${NC} $tool"
    done
    
    echo -e "\n${RED}⚔️ EXPLOTACIÓN Y POST-EXPLOTACIÓN${NC}"
    for tool in "${!EXPLOIT_TOOLS[@]}"; do
        echo -e "  ${CYAN}•${NC} $tool"
    done
    
    echo -e "\n${PURPLE}🔓 CRACKING Y FUERZA BRUTA${NC}"
    for tool in "${!CRACK_TOOLS[@]}"; do
        echo -e "  ${CYAN}•${NC} $tool"
    done
    
    echo -e "\n${BLUE}🌐 WEB & CLOUD OFFENSIVE${NC}"
    for tool in "${!WEB_TOOLS[@]}"; do
        echo -e "  ${CYAN}•${NC} $tool"
    done
    
    echo -e "\n${GREEN}📡 ANÁLISIS DE TRÁFICO Y FORENSE${NC}"
    for tool in "${!FORENSICS_TOOLS[@]}"; do
        echo -e "  ${CYAN}•${NC} $tool"
    done
    
    echo -e "\n${CYAN}📦 EXFILTRACIÓN Y MANIPULACIÓN DE DATOS${NC}"
    for tool in "${!EXFIL_TOOLS[@]}"; do
        echo -e "  ${CYAN}•${NC} $tool"
    done
    
    echo -e "\n${WHITE}💣 PAYLOADS${NC}"
    for tool in "${!PAYLOAD_TOOLS[@]}"; do
        echo -e "  ${CYAN}•${NC} $tool"
    done
    
    echo -e "\n${GREEN}[*] Presiona Enter para continuar...${NC}"
    read -r
}

# Función de salida
exit_program() {
    echo -e "\n${BLUE}[*] Finalizando KaliToolsManager...${NC}"
    log_action "KaliToolsManager finalizado"
    echo -e "${GREEN}[✓] Gracias por usar KaliToolsManager${NC}"
    echo -e "${CYAN}[*] Mantén tu arsenal actualizado${NC}"
    exit 0
}

# Script principal
main() {
    # Verificaciones iniciales
    check_privileges
    initialize_system
    
    # Mostrar información inicial
    log_action "KaliToolsManager iniciado"
    
    # Ejecutar menú principal
    main_menu
}

# Manejo de señales
trap 'echo -e "\n${RED}[!] Interrumpido por el usuario${NC}"; exit_program' SIGINT SIGTERM

# Ejecutar script principal
main "$@"

# Estado del sistema
system_status() {
    show_banner
    echo -e "${WHITE}╔════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${WHITE}║${CYAN}                      ESTADO DEL SISTEMA                        ${WHITE}║${NC}"
    echo -e "${WHITE}╠════════════════════════════════════════════════════════════════╣${NC}"
    
    # Información del sistema
    echo -e "${WHITE}║ ${YELLOW}Sistema:${NC} $(lsb_release -d | cut -f2)"
    echo -e "${WHITE}║ ${YELLOW}Kernel:${NC} $(uname -r)"
    echo -e "${WHITE}║ ${YELLOW}Arquitectura:${NC} $(uname -m)"
    echo -e "${WHITE}║ ${YELLOW}Fecha:${NC} $(date '+%Y-%m-%d %H:%M:%S')"
    
    # Espacio en disco
    local disk_usage=$(df -h / | awk 'NR==2{print $5}')
    echo -e "${WHITE}║ ${YELLOW}Uso de disco /:${NC} $disk_usage"
    
    # Memoria
    local mem_info=$(free -h | awk 'NR==2{printf "Usado: %s / Total: %s", $3, $2}')
    echo -e "${WHITE}║ ${YELLOW}Memoria:${NC} $mem_info"
    
    # Herramientas instaladas
    local installed_count=0
    for category_tools in RECON_TOOLS VULN_TOOLS EXPLOIT_TOOLS CRACK_TOOLS WEB_TOOLS FORENSICS_TOOLS EXFIL_TOOLS PAYLOAD_TOOLS; do
        declare -n ref=$category_tools
        for package in "${ref[@]}"; do
            if dpkg -l "$package" &>/dev/null; then
                ((installed_count++))
            fi
        done
    done
    
    echo -e "${WHITE}║ ${YELLOW}Herramientas instaladas:${NC} $installed_count"
    
    # Última actualización
    if [[ -f "$LOGFILE" ]]; then
        local last_update=$(grep "Actualización" "$LOGFILE" | tail -1 | cut -d']' -f1 | tr -d '[')
        echo -e "${WHITE}║ ${YELLOW}Última actualización:${NC} ${last_update:-'N/A'}"
    fi
    
    echo -e "${WHITE}╚════════════════════════════════════════════════════════════════╝${NC}"
    echo -e "\n${GREEN}[*] Presiona Enter para continuar...${NC}"
    read -r
}
