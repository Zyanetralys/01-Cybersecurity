#!/bin/bash

# =============================================================================
# NmapTool - Herramienta de Automatización de Nmap para Kali Linux
# Autor: Herramienta automatizada para pentesting
# Versión: 1.0
# =============================================================================

# Colores para la terminal
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color

# Variables globales
TARGET=""
OUTPUT_DIR="nmap_results"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Banner de la herramienta
show_banner() {
    clear
    echo -e "${CYAN}
╔══════════════════════════════════════════════════════════════════════════╗
║                              ${WHITE}NMAP TOOL${CYAN}                                  ║
║                   ${YELLOW}Herramienta de Automatización de Nmap${CYAN}                   ║
║                           ${GREEN}Para Kali ${CYAN}                               ║
║                                                                          ║
║  ${WHITE}Desarrollada para facilitar el uso de Nmap en pentesting${CYAN}             ║
╚══════════════════════════════════════════════════════════════════════════╝
${NC}"
}

# Verificar si Nmap está instalado
check_nmap() {
    if ! command -v nmap &> /dev/null; then
        echo -e "${RED}[ERROR] Nmap no está instalado.${NC}"
        echo -e "${YELLOW}Instalando Nmap...${NC}"
        sudo apt update && sudo apt install nmap -y
    fi
}

# Crear directorio de salida
create_output_dir() {
    if [ ! -d "$OUTPUT_DIR" ]; then
        mkdir -p "$OUTPUT_DIR"
        echo -e "${GREEN}[INFO] Directorio de resultados creado: $OUTPUT_DIR${NC}"
    fi
}

# Validar IP o dominio
validate_target() {
    local target="$1"
    
    # Verificar si es una IP válida
    if [[ $target =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]; then
        return 0
    fi
    
    # Verificar si es un rango CIDR válido
    if [[ $target =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/[0-9]{1,2}$ ]]; then
        return 0
    fi
    
    # Verificar si es un dominio válido
    if [[ $target =~ ^[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*$ ]]; then
        return 0
    fi
    
    return 1
}

# Obtener target del usuario
get_target() {
    while true; do
        echo -e "${YELLOW}Introduce el objetivo (IP, dominio o rango CIDR):${NC}"
        read -p "Target: " TARGET
        
        if validate_target "$TARGET"; then
            echo -e "${GREEN}[INFO] Target válido: $TARGET${NC}"
            break
        else
            echo -e "${RED}[ERROR] Target inválido. Intenta de nuevo.${NC}"
        fi
    done
}

# Menú principal
show_main_menu() {
    echo -e "${WHITE}
╔══════════════════════════════════════════════════════════════════════════╗
║                            MENÚ PRINCIPAL                                ║
╠══════════════════════════════════════════════════════════════════════════╣
║  ${CYAN}1.${WHITE} Escaneos Básicos                                                ║
║  ${CYAN}2.${WHITE} Escaneos Avanzados                                              ║
║  ${CYAN}3.${WHITE} Detección de Servicios y Versiones                             ║
║  ${CYAN}4.${WHITE} Escaneos de Vulnerabilidades                                   ║
║  ${CYAN}5.${WHITE} Evasión de Firewalls                                           ║
║  ${CYAN}6.${WHITE} Scripts NSE Personalizados                                     ║
║  ${CYAN}7.${WHITE} Configurar Target                                              ║
║  ${CYAN}8.${WHITE} Ver Resultados Anteriores                                      ║
║  ${CYAN}9.${WHITE} Acerca de                                                      ║
║  ${CYAN}0.${WHITE} Salir                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝"

    if [ ! -z "$TARGET" ]; then
        echo -e "${GREEN}Target actual: $TARGET${NC}"
    else
        echo -e "${RED}No hay target configurado${NC}"
    fi
    echo ""
}

# Menú de escaneos básicos
basic_scans_menu() {
    while true; do
        clear
        show_banner
        echo -e "${WHITE}
╔══════════════════════════════════════════════════════════════════════════╗
║                          ESCANEOS BÁSICOS                               ║
╠══════════════════════════════════════════════════════════════════════════╣
║  ${CYAN}1.${WHITE} Ping Scan (Descubrimiento de hosts)                            ║
║  ${CYAN}2.${WHITE} Port Scan Básico (Top 1000 puertos)                           ║
║  ${CYAN}3.${WHITE} TCP Connect Scan                                               ║
║  ${CYAN}4.${WHITE} TCP SYN Scan (Stealth)                                         ║
║  ${CYAN}5.${WHITE} UDP Scan                                                       ║
║  ${CYAN}6.${WHITE} Scan de todos los puertos TCP                                 ║
║  ${CYAN}7.${WHITE} Fast Scan (Top 100 puertos)                                   ║
║  ${CYAN}8.${WHITE} Intense Scan                                                   ║
║  ${CYAN}0.${WHITE} Volver al menú principal                                       ║
╚══════════════════════════════════════════════════════════════════════════╝"
        
        if [ ! -z "$TARGET" ]; then
            echo -e "${GREEN}Target actual: $TARGET${NC}"
        else
            echo -e "${RED}¡Configure un target primero!${NC}"
        fi
        
        read -p "Selecciona una opción: " choice
        
        if [ -z "$TARGET" ] && [ "$choice" != "0" ]; then
            echo -e "${RED}[ERROR] Debe configurar un target primero.${NC}"
            read -p "Presiona Enter para continuar..."
            continue
        fi
        
        case $choice in
            1) ping_scan ;;
            2) basic_port_scan ;;
            3) tcp_connect_scan ;;
            4) tcp_syn_scan ;;
            5) udp_scan ;;
            6) all_ports_scan ;;
            7) fast_scan ;;
            8) intense_scan ;;
            0) break ;;
            *) echo -e "${RED}Opción inválida${NC}"; sleep 2 ;;
        esac
    done
}

# Menú de escaneos avanzados
advanced_scans_menu() {
    while true; do
        clear
        show_banner
        echo -e "${WHITE}
╔══════════════════════════════════════════════════════════════════════════╗
║                         ESCANEOS AVANZADOS                              ║
╠══════════════════════════════════════════════════════════════════════════╣
║  ${CYAN}1.${WHITE} OS Detection                                                   ║
║  ${CYAN}2.${WHITE} Traceroute                                                     ║
║  ${CYAN}3.${WHITE} IPv6 Scan                                                      ║
║  ${CYAN}4.${WHITE} Scan con fragmentación de paquetes                            ║
║  ${CYAN}5.${WHITE} Scan con decoy (señuelos)                                     ║
║  ${CYAN}6.${WHITE} Scan a través de proxy SOCKS                                  ║
║  ${CYAN}7.${WHITE} Idle Scan                                                      ║
║  ${CYAN}8.${WHITE} FTP Bounce Scan                                               ║
║  ${CYAN}0.${WHITE} Volver al menú principal                                       ║
╚══════════════════════════════════════════════════════════════════════════╝"
        
        if [ ! -z "$TARGET" ]; then
            echo -e "${GREEN}Target actual: $TARGET${NC}"
        else
            echo -e "${RED}¡Configure un target primero!${NC}"
        fi
        
        read -p "Selecciona una opción: " choice
        
        if [ -z "$TARGET" ] && [ "$choice" != "0" ]; then
            echo -e "${RED}[ERROR] Debe configurar un target primero.${NC}"
            read -p "Presiona Enter para continuar..."
            continue
        fi
        
        case $choice in
            1) os_detection ;;
            2) traceroute_scan ;;
            3) ipv6_scan ;;
            4) fragmentation_scan ;;
            5) decoy_scan ;;
            6) proxy_scan ;;
            7) idle_scan ;;
            8) ftp_bounce_scan ;;
            0) break ;;
            *) echo -e "${RED}Opción inválida${NC}"; sleep 2 ;;
        esac
    done
}

# Funciones de escaneos básicos
ping_scan() {
    echo -e "${YELLOW}[INFO] Ejecutando Ping Scan...${NC}"
    local output_file="$OUTPUT_DIR/ping_scan_${TIMESTAMP}.txt"
    nmap -sn "$TARGET" | tee "$output_file"
    echo -e "${GREEN}[INFO] Resultados guardados en: $output_file${NC}"
    read -p "Presiona Enter para continuar..."
}

basic_port_scan() {
    echo -e "${YELLOW}[INFO] Ejecutando escaneo básico de puertos (Top 1000)...${NC}"
    local output_file="$OUTPUT_DIR/basic_scan_${TIMESTAMP}.txt"
    nmap "$TARGET" | tee "$output_file"
    echo -e "${GREEN}[INFO] Resultados guardados en: $output_file${NC}"
    read -p "Presiona Enter para continuar..."
}

tcp_connect_scan() {
    echo -e "${YELLOW}[INFO] Ejecutando TCP Connect Scan...${NC}"
    local output_file="$OUTPUT_DIR/tcp_connect_${TIMESTAMP}.txt"
    nmap -sT "$TARGET" | tee "$output_file"
    echo -e "${GREEN}[INFO] Resultados guardados en: $output_file${NC}"
    read -p "Presiona Enter para continuar..."
}

tcp_syn_scan() {
    echo -e "${YELLOW}[INFO] Ejecutando TCP SYN Scan (Stealth)...${NC}"
    local output_file="$OUTPUT_DIR/tcp_syn_${TIMESTAMP}.txt"
    sudo nmap -sS "$TARGET" | tee "$output_file"
    echo -e "${GREEN}[INFO] Resultados guardados en: $output_file${NC}"
    read -p "Presiona Enter para continuar..."
}

udp_scan() {
    echo -e "${YELLOW}[INFO] Ejecutando UDP Scan (puede tomar tiempo)...${NC}"
    local output_file="$OUTPUT_DIR/udp_scan_${TIMESTAMP}.txt"
    sudo nmap -sU --top-ports 1000 "$TARGET" | tee "$output_file"
    echo -e "${GREEN}[INFO] Resultados guardados en: $output_file${NC}"
    read -p "Presiona Enter para continuar..."
}

all_ports_scan() {
    echo -e "${YELLOW}[INFO] Escaneando todos los puertos TCP (1-65535)...${NC}"
    echo -e "${RED}[ADVERTENCIA] Este escaneo puede tomar mucho tiempo${NC}"
    read -p "¿Continuar? (y/N): " confirm
    if [[ $confirm =~ ^[Yy]$ ]]; then
        local output_file="$OUTPUT_DIR/all_ports_${TIMESTAMP}.txt"
        nmap -p- "$TARGET" | tee "$output_file"
        echo -e "${GREEN}[INFO] Resultados guardados en: $output_file${NC}"
    fi
    read -p "Presiona Enter para continuar..."
}

fast_scan() {
    echo -e "${YELLOW}[INFO] Ejecutando Fast Scan (Top 100 puertos)...${NC}"
    local output_file="$OUTPUT_DIR/fast_scan_${TIMESTAMP}.txt"
    nmap -F "$TARGET" | tee "$output_file"
    echo -e "${GREEN}[INFO] Resultados guardados en: $output_file${NC}"
    read -p "Presiona Enter para continuar..."
}

intense_scan() {
    echo -e "${YELLOW}[INFO] Ejecutando Intense Scan...${NC}"
    local output_file="$OUTPUT_DIR/intense_scan_${TIMESTAMP}.txt"
    sudo nmap -T4 -A -v "$TARGET" | tee "$output_file"
    echo -e "${GREEN}[INFO] Resultados guardados en: $output_file${NC}"
    read -p "Presiona Enter para continuar..."
}

# Funciones de escaneos avanzados
os_detection() {
    echo -e "${YELLOW}[INFO] Ejecutando detección de OS...${NC}"
    local output_file="$OUTPUT_DIR/os_detection_${TIMESTAMP}.txt"
    sudo nmap -O "$TARGET" | tee "$output_file"
    echo -e "${GREEN}[INFO] Resultados guardados en: $output_file${NC}"
    read -p "Presiona Enter para continuar..."
}

traceroute_scan() {
    echo -e "${YELLOW}[INFO] Ejecutando traceroute...${NC}"
    local output_file="$OUTPUT_DIR/traceroute_${TIMESTAMP}.txt"
    nmap --traceroute "$TARGET" | tee "$output_file"
    echo -e "${GREEN}[INFO] Resultados guardados en: $output_file${NC}"
    read -p "Presiona Enter para continuar..."
}

ipv6_scan() {
    echo -e "${YELLOW}[INFO] Ejecutando IPv6 scan...${NC}"
    local output_file="$OUTPUT_DIR/ipv6_scan_${TIMESTAMP}.txt"
    nmap -6 "$TARGET" | tee "$output_file"
    echo -e "${GREEN}[INFO] Resultados guardados en: $output_file${NC}"
    read -p "Presiona Enter para continuar..."
}

fragmentation_scan() {
    echo -e "${YELLOW}[INFO] Ejecutando scan con fragmentación...${NC}"
    local output_file="$OUTPUT_DIR/fragmentation_${TIMESTAMP}.txt"
    sudo nmap -f "$TARGET" | tee "$output_file"
    echo -e "${GREEN}[INFO] Resultados guardados en: $output_file${NC}"
    read -p "Presiona Enter para continuar..."
}

decoy_scan() {
    echo -e "${YELLOW}[INFO] Ejecutando scan con decoys...${NC}"
    local output_file="$OUTPUT_DIR/decoy_scan_${TIMESTAMP}.txt"
    sudo nmap -D RND:10 "$TARGET" | tee "$output_file"
    echo -e "${GREEN}[INFO] Resultados guardados en: $output_file${NC}"
    read -p "Presiona Enter para continuar..."
}

proxy_scan() {
    echo -e "${YELLOW}[INFO] Para scan a través de proxy SOCKS...${NC}"
    read -p "Introduce la IP del proxy SOCKS: " proxy_ip
    read -p "Introduce el puerto del proxy SOCKS: " proxy_port
    local output_file="$OUTPUT_DIR/proxy_scan_${TIMESTAMP}.txt"
    proxychains nmap "$TARGET" | tee "$output_file"
    echo -e "${GREEN}[INFO] Resultados guardados en: $output_file${NC}"
    read -p "Presiona Enter para continuar..."
}

idle_scan() {
    echo -e "${YELLOW}[INFO] Para Idle scan necesitas una máquina zombie...${NC}"
    read -p "Introduce la IP de la máquina zombie: " zombie_ip
    local output_file="$OUTPUT_DIR/idle_scan_${TIMESTAMP}.txt"
    sudo nmap -sI "$zombie_ip" "$TARGET" | tee "$output_file"
    echo -e "${GREEN}[INFO] Resultados guardados en: $output_file${NC}"
    read -p "Presiona Enter para continuar..."
}

ftp_bounce_scan() {
    echo -e "${YELLOW}[INFO] FTP Bounce Scan...${NC}"
    read -p "Introduce la IP del servidor FTP: " ftp_ip
    local output_file="$OUTPUT_DIR/ftp_bounce_${TIMESTAMP}.txt"
    nmap -b "$ftp_ip" "$TARGET" | tee "$output_file"
    echo -e "${GREEN}[INFO] Resultados guardados en: $output_file${NC}"
    read -p "Presiona Enter para continuar..."
}

# Ver resultados anteriores
view_results() {
    clear
    show_banner
    echo -e "${WHITE}Resultados anteriores en el directorio: $OUTPUT_DIR${NC}"
    echo ""
    
    if [ -d "$OUTPUT_DIR" ] && [ "$(ls -A $OUTPUT_DIR)" ]; then
        ls -la "$OUTPUT_DIR"
        echo ""
        read -p "Introduce el nombre del archivo a ver (o Enter para volver): " filename
        if [ ! -z "$filename" ] && [ -f "$OUTPUT_DIR/$filename" ]; then
            less "$OUTPUT_DIR/$filename"
        fi
    else
        echo -e "${YELLOW}No hay resultados anteriores.${NC}"
    fi
    
    read -p "Presiona Enter para continuar..."
}

# Acerca de
about() {
    clear
    show_banner
    echo -e "${WHITE}
╔══════════════════════════════════════════════════════════════════════════╗
║                              ACERCA DE                                  ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  ${CYAN}NmapTool v1.0${WHITE}                                                        ║
║                                                                          ║
║  Herramienta de automatización de Nmap diseñada para facilitar          ║
║  las tareas de reconocimiento y pentesting en Kali Linux.               ║
║                                                                          ║
║  ${YELLOW}Características:${WHITE}                                                    ║
║  • Interfaz interactiva y amigable                                      ║
║  • Múltiples tipos de escaneo                                           ║
║  • Guardado automático de resultados                                    ║
║  • Validación de targets                                                ║
║  • Scripts NSE integrados                                               ║
║                                                                          ║
║  ${GREEN}¡Úsala responsablemente y solo en sistemas autorizados!${WHITE}            ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝"

    read -p "Presiona Enter para continuar..."
}

# Función principal
main() {
    check_nmap
    create_output_dir
    
    while true; do
        clear
        show_banner
        show_main_menu
        
        read -p "Selecciona una opción: " choice
        
        case $choice in
            1) basic_scans_menu ;;
            2) advanced_scans_menu ;;
            3) echo -e "${YELLOW}Funcionalidad en desarrollo...${NC}"; sleep 2 ;;
            4) echo -e "${YELLOW}Funcionalidad en desarrollo...${NC}"; sleep 2 ;;
            5) echo -e "${YELLOW}Funcionalidad en desarrollo...${NC}"; sleep 2 ;;
            6) echo -e "${YELLOW}Funcionalidad en desarrollo...${NC}"; sleep 2 ;;
            7) get_target ;;
            8) view_results ;;
            9) about ;;
            0) 
                echo -e "${GREEN}¡Gracias por usar NmapTool!${NC}"
                exit 0
                ;;
            *) 
                echo -e "${RED}Opción inválida${NC}"
                sleep 2
                ;;
        esac
    done
}

# Verificar si se ejecuta con permisos de root para algunas funciones
if [[ $EUID -ne 0 ]]; then
    echo -e "${YELLOW}[ADVERTENCIA] Algunas funciones requieren permisos de root.${NC}"
    echo -e "${YELLOW}Para funcionalidad completa, ejecuta: sudo $0${NC}"
    sleep 3
fi

# Ejecutar función principal
main
