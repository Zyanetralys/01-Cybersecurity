#!/usr/bin/env bash
# cme_tool_advanced.sh - Herramienta completa CME con RPG feedback para entrenamiento Nirith
# Autora: Zyanetralys (Nirith)
# Uso: Solo en entornos autorizados (laboratorio / CTF / pentest con contrato).

set -euo pipefail
IFS=$'\n\t'

# --- Configuración base ---
BASE_DIR="${HOME}/.cme_tool_adv"
PROFILES_DIR="${BASE_DIR}/profiles"
LOG_DIR="${BASE_DIR}/logs"
REPORTS_DIR="${BASE_DIR}/reports"
POINTS_FILE="${BASE_DIR}/points.dat"
FEEDBACK_LOG="${BASE_DIR}/feedback.log"

CONFIRM_PHRASE="Confirmo que usaré la herramienta únicamente en entornos donde tengo permiso explícito (mi laboratorio, CTFs autorizados o pentests con contrato) y asumo toda la responsabilidad legal y ética por su uso. Nirith"

mkdir -p "${PROFILES_DIR}" "${LOG_DIR}" "${REPORTS_DIR}"

# Variables globales
AUTHORIZED=false
CURRENT_PROFILE=""
POINTS=0

log() {
  echo "[$(date -Iseconds)] $*" >> "${LOG_DIR}/cme_tool.log"
}

feedback() {
  # Mensajes RPG personalizados de Nirith/Athena
  local type="$1"
  local msg="$2"
  local prefix
  case "$type" in
    success) prefix="✅ [Nirith] - " ;;
    warning) prefix="⚠ [Athena] - " ;;
    error) prefix="❌ [Nirith] - " ;;
    info) prefix="ℹ [Athena] - " ;;
    *) prefix="-- [Sys] - " ;;
  esac
  echo "${prefix}${msg}"
  echo "$(date '+%Y-%m-%d %H:%M:%S') | ${type^^} | ${msg}" >> "$FEEDBACK_LOG"
}

increment_points() {
  local pts=$1
  POINTS=$((POINTS + pts))
  echo "$POINTS" > "$POINTS_FILE"
}

load_points() {
  if [[ -f "$POINTS_FILE" ]]; then
    POINTS=$(<"$POINTS_FILE")
  else
    POINTS=0
  fi
}

profile_path() {
  local name="$1"
  echo "${PROFILES_DIR}/${name}.conf"
}

create_default_profile() {
  local name="$1"
  local path
  path=$(profile_path "${name}")
  cat > "${path}" <<EOF
NAME=${name}
AUTHORIZED_EXECUTION=false
TARGETS=""
USERS=""
PASSWORDS=""
DOMAIN=""
MODULES=""
FLAGS=""
EOF
  chmod 600 "${path}"
  log "Perfil creado: ${name}"
  feedback info "Perfil ${name} creado."
  echo "Perfil ${name} creado."
}

list_profiles() {
  ls -1 "${PROFILES_DIR}"/*.conf 2>/dev/null | xargs -n1 basename 2>/dev/null | sed 's/\.conf$//' || true
}

load_profile() {
  local name="$1"
  local path
  path=$(profile_path "${name}")
  if [[ ! -f "$path" ]]; then
    feedback error "Perfil no encontrado: $name"
    return 1
  fi
  # shellcheck disable=SC1090
  set -a
  source "$path"
  set +a
  CURRENT_PROFILE="$name"
  feedback info "Perfil $name cargado."
  log "Perfil cargado: $name"
  return 0
}

save_profile_var() {
  local name="$1" var="$2" val="$3"
  local path
  path=$(profile_path "$name")
  if grep -q "^${var}=" "$path"; then
    sed -i "s|^${var}=.*|${var}=${val}|" "$path"
  else
    echo "${var}=${val}" >> "$path"
  fi
  log "Perfil $name: ${var} set a ${val}"
}

prompt() {
  local msg="$1"
  read -r -p "$msg " REPLY
  echo "$REPLY"
}

prompt_default() {
  local msg="$1" default="$2"
  read -r -p "$msg [$default]: " REPLY
  echo "${REPLY:-$default}"
}

confirm_strict() {
  echo
  echo "!!! ADVERTENCIA: Esta operación puede ser destructiva o intrusiva !!!"
  echo "Para continuar, pega EXACTAMENTE la frase de confirmación:"
  echo
  echo "$CONFIRM_PHRASE"
  echo
  read -r -p "Frase: " userphrase
  [[ "$userphrase" == "$CONFIRM_PHRASE" ]]
}

authorize_execution() {
  echo "Para habilitar la ejecución real, escribe la siguiente frase EXACTA:"
  echo
  echo "$CONFIRM_PHRASE"
  echo
  read -r -p "> " user_input
  if [[ "$user_input" == "$CONFIRM_PHRASE" ]]; then
    AUTHORIZED=true
    feedback success "Autorización concedida para esta sesión."
    log "Autorización concedida."
  else
    feedback error "Frase incorrecta. Ejecución real NO autorizada."
    log "Autorización fallida."
  fi
}

edit_profile_interactive() {
  local profile="$1"
  local path
  path=$(profile_path "$profile")
  if [[ ! -f "$path" ]]; then
    feedback error "Perfil no existe: $profile"
    return
  fi
  echo "Editando perfil: $profile"
  echo "Valores actuales:"
  cat "$path"
  echo
  echo "Introduce valores (ENTER para mantener actual):"

  local val

  val=$(prompt_default "TARGETS (IPs, rango o hosts separados por coma)" "$(grep '^TARGETS=' "$path" | cut -d= -f2-)")
  save_profile_var "$profile" "TARGETS" "\"$val\""

  val=$(prompt_default "USERS (usuarios separados por coma)" "$(grep '^USERS=' "$path" | cut -d= -f2-)")
  save_profile_var "$profile" "USERS" "\"$val\""

  val=$(prompt_default "PASSWORDS (passlist o rangos separados por coma)" "$(grep '^PASSWORDS=' "$path" | cut -d= -f2-)")
  save_profile_var "$profile" "PASSWORDS" "\"$val\""

  val=$(prompt_default "DOMAIN (dominio Active Directory)" "$(grep '^DOMAIN=' "$path" | cut -d= -f2-)")
  save_profile_var "$profile" "DOMAIN" "\"$val\""

  val=$(prompt_default "MODULES (módulos CME separados por coma)" "$(grep '^MODULES=' "$path" | cut -d= -f2-)")
  save_profile_var "$profile" "MODULES" "\"$val\""

  val=$(prompt_default "FLAGS (flags extra CME)" "$(grep '^FLAGS=' "$path" | cut -d= -f2-)")
  save_profile_var "$profile" "FLAGS" "\"$val\""

  feedback success "Perfil guardado."
}

build_cme_command() {
  local profile="$1"
  load_profile "$profile" || return 1

  local cmd="cme"
  [[ -n "${TARGETS//\"/}" ]] && cmd+=" ${TARGETS//\"/}"
  [[ -n "${USERS//\"/}" ]] && cmd+=" -u ${USERS//\"/}"
  [[ -n "${PASSWORDS//\"/}" ]] && cmd+=" -p ${PASSWORDS//\"/}"
  [[ -n "${DOMAIN//\"/}" ]] && cmd+=" -d ${DOMAIN//\"/}"
  [[ -n "${MODULES//\"/}" ]] && cmd+=" --module ${MODULES//\"/}"
  [[ -n "${FLAGS//\"/}" ]] && cmd+=" ${FLAGS//\"/}"

  echo "$cmd"
}

execute_cme_command() {
  local cmd="$1"

  echo "Comando CME a ejecutar:"
  echo "$cmd"
  echo

  if ! $AUTHORIZED; then
    feedback warning "Modo seguro activo. No se ejecutará el comando."
    log "Intento ejecución CME bloqueado en modo seguro: $cmd"
    return 1
  fi

  if confirm_strict; then
    feedback info "Ejecutando comando CME..."
    log "Ejecución CME: $cmd"
    eval "$cmd"
    local ret=$?
    if [[ $ret -eq 0 ]]; then
      feedback success "Comando CME ejecutado correctamente."
      increment_points 10
      log "Ejecución correcta."
    else
      feedback error "Error ejecutando comando CME (código $ret)."
      increment_points -5
      log "Ejecución fallida."
    fi
    return $ret
  else
    feedback error "Confirmación fallida. Comando NO ejecutado."
    log "Confirmación ejecución CME fallida."
    return 1
  fi
}

view_logs() {
  if [[ ! -f "${LOG_DIR}/cme_tool.log" ]]; then
    echo "No hay logs disponibles."
    return
  fi
  echo "=== Últimas 100 líneas de logs ==="
  tail -n 100 "${LOG_DIR}/cme_tool.log"
}

show_points() {
  load_points
  echo "=== Puntos acumulados: $POINTS ==="
}

generate_report() {
  local timestamp
  timestamp=$(date '+%Y%m%d_%H%M%S')
  local report_file="${REPORTS_DIR}/report_${CURRENT_PROFILE}_${timestamp}.txt"
  {
    echo "Reporte CME Tool"
    echo "Perfil: $CURRENT_PROFILE"
    echo "Fecha: $(date)"
    echo
    echo "Puntos acumulados: $POINTS"
    echo
    echo "Últimos logs:"
    tail -n 50 "${LOG_DIR}/cme_tool.log" 2>/dev/null || echo "No logs disponibles."
  } > "$report_file"
  feedback info "Reporte generado: $report_file"
  echo "Reporte guardado en: $report_file"
}

clear_screen() {
  if command -v clear >/dev/null 2>&1; then
    clear
  else
    echo -e "\n\n"
  fi
}

main_menu() {
  load_points
  if [[ ! -f "$(profile_path default)" ]]; then
    create_default_profile default
  fi
  CURRENT_PROFILE="default"
  load_profile "$CURRENT_PROFILE" || true

  while true; do
    clear_screen
    echo "=== CME TOOL AVANZADO - Entrenamiento Nirith ==="
    echo "Perfil actual: $CURRENT_PROFILE"
    echo "Puntos acumulados: $POINTS"
    echo "Modo ejecución real: $( [[ $AUTHORIZED == true ]] && echo "ACTIVO ✅" || echo "DESACTIVADO ❌" )"
    echo
    echo "1) Seleccionar / Crear perfil"
    echo "2) Editar perfil actual"
    echo "3) Mostrar comando CME (dry-run)"
    echo "4) Ejecutar comando CME"
    echo "5) Ver logs"
    echo "6) Generar reporte"
    echo "7) Mostrar puntos acumulados"
    echo "8) Autorizar ejecución real"
    echo "9) Salir"
    echo
    read -r -p "> " choice
    case "$choice" in
      1)
        echo "Perfiles disponibles:"
        list_profiles || echo "No hay perfiles."
        read -r -p "Nombre perfil a seleccionar (o nuevo): " sel
        if [[ ! -f "$(profile_path "$sel")" ]]; then
          read -r -p "Perfil no existe. Crear $sel? (yes/no): " yn
          if [[ "$yn" == "yes" ]]; then
            create_default_profile "$sel"
          else
            feedback warning "Selección cancelada."
            continue
          fi
        fi
        load_profile "$sel" || feedback error "No se pudo cargar perfil."
        ;;
      2)
        edit_profile_interactive "$CURRENT_PROFILE"
        ;;
      3)
        build_cme_command "$CURRENT_PROFILE"
        pause() { read -rp "Pulsa ENTER para continuar..."; }
        read -rp "Pulsa ENTER para continuar..."
        ;;
      4)
        local cmd
        cmd=$(build_cme_command "$CURRENT_PROFILE")
        execute_cme_command "$cmd"
        pause() { read -rp "Pulsa ENTER para continuar..."; }
        read -rp "Pulsa ENTER para continuar..."
        ;;
      5)
        view_logs
        pause() { read -rp "Pulsa ENTER para continuar..."; }
        read -rp "Pulsa ENTER para continuar..."
        ;;
      6)
        generate_report
        pause() { read -rp "Pulsa ENTER para continuar..."; }
        read -rp "Pulsa ENTER para continuar..."
        ;;
      7)
        show_points
        pause() { read -rp "Pulsa ENTER para continuar..."; }
        read -rp "Pulsa ENTER para continuar..."
        ;;
      8)
        authorize_execution
        pause() { read -rp "Pulsa ENTER para continuar..."; }
        read -rp "Pulsa ENTER para continuar..."
        ;;
      9)
        echo "Saliendo. Que Athena y Nirith te guíen."
        exit 0
        ;;
      *)
        feedback warning "Opción inválida."
        pause() { read -rp "Pulsa ENTER para continuar..."; }
        read -rp "Pulsa ENTER para continuar..."
        ;;
    esac
  done
}

main_menu
