# Master en Ciberseguridad

## Seguridad Web

### Conocimientos útiles
- Docker
- HTML + CSS
- Javascript
- Git

### HTTP proxies

#### Locales
Soporte SSL para inspeccionar tráfico cifrado.

- **Burp Suite:** suite completa de seguridad web, auditoría, bug bounting, cara
- **ZAP** (Zed Attack Proxy): del proyecto OWASP, open source - https://www.zaproxy.org
- **Nikto**: Escáner open source para recon y vulnerabilidades - https://github.com/sullo/nikto

### Recon

#### Activo y pasivo
**Recon**: Obtener info.

**Pasiva**: No genera ruido, huella ni intención hostil. 
Obtener dirección IP, whois, OSINT.

### User-Agent e IP origen
1. Se empieza por un Dominio.
2. Scripts para determinar versión del cliente y dependencia de tipo.
3. **Cambiar nuestro origen respecto de la IP:**
   Pasar por un proxy (como Tor) o tener una máquina en una localización geográfica.
   Ese proxy o máquina es la IP que conecta con el objetivo.
    Otras veces, es DNS determinada.

**¿Por qué?** Si una app movil es una vist web, al cargar la versión móvil da acceso a API autorizadas para la versión móvil que confían en la app, y nos da acceso a endpoints que en versión desktop necesitarían autenticación.
Muchas API móviles relajan la seguridad en móvil (piensan que "nadie va a mirar aquí")

#### User-Agent
**User-Agent** (agente/cliente web): 
- Cabecera que viaja en las peticiones de nuestro cliente, recogidas por el servidor.
- Definido en un RFC importante (https://www.rfc-editor.org/rfc/rfc9110.html#name-user-agent)
- Posee información sobre el que visita la web, versión de su navegador su sistema operativo, arquitectura, versión de sistema, motor de renderizado y versión.

#### Cambiar User-Agent

##### Plugin para navegador
Instalando un complemento y eligiendo user-agent de la lista o añadiendo nosotros uno.

##### dev-tools del navegador
Herramientas de desarrollo del navegador: Permiten indicarle que se haga pasar por distintos tipos de dispositivos móviles.

##### curl
Herramienta de línea de comandos curl.

### Dominios, Redes e IP

#### Dominio
Presencia más común en la web.
Establecer relación dominio-ip: Consulta DNS (por ejemplo con dig)

##### Dig
Dig hace consulta tipo "A"
(equivalente a: 'dig -t A <dominio>')

'-t' cambia el tipo de consulta

'-t mx' pregunta si posee intercambiador de correo asociaddo

'-t any' da todos los registros asociados a ese dominio

##### Los dominios cambian de IP (pero no a corto plazo)
No cambia en corto plazo (posee las mismas direcciones asoaciadas en corto plazo)
Cada respuesta DNS va acompañda de TTL (time to live), duración en caché de la respuesta, que al cumplir ya no es fiable y debe refrescarse.
Configuración: Round-Robin (va cambiando de IP circularmente), balanceo de carga, etc.
Nuevo servidor debería tener mismo contenido salvo que existe sistema de sincronización que no haya indexado la nueva carga.

##### Whois
Whois es un protocolo. Su info se mantiene en BBDD administradas por autoridades y delegados. Parte del IANA y jerarquicamente por registros por continentes: ARIN, APNIC, LACNIC, RIPE, etc.
Whois se usa también para info de IPs: a quién pertenece y quién administra esa red.
La información de registro identifica al Admin de dominios, direcciones IP y redes.
Normalmente aparece el registrador (empresa que registra dominio), no el registrante (quien compra el registro del dominio)
Info de interés: Servidores DNS del dominio, fecha de registro, actualización, caducidad (deben renovarse)
Si la organización es grande: Localizar bloque de IPs al que pertence la IP que apunta a un dominio para investigara las máquinas activas en ese bloque y realizar consulta de nombres inversa.

##### Subdominios (Dominios de tercer nivel, TLD)
Si ya tenemos un grupo de dominios asociados a una organización, toca expandir consultas a los subdominios o dominios de tercer nivel.
TLD no están registrados en ningún lado, solo se configura el DNS para cuando llegue una consulta, responda de una u otra forma.

###### Consulta Web
Buscamos contenido indexado en la web.

**Dorks**: Operadores en los buscadores.

###### Consultas DNS masivas (DNS enumeration)
Interrogar los servidores DNS usando listas de subdominios y variando tipo de consulta DNS (A, NS, MX...)

Herramientas:
- **bucle "for"** en bash con host o dig.
- **dnsrecon**:https://github.com/darkoperator/dnsrecon
- **amass**:https://github.com/owasp-amass/amass
amass tambien para descubrimientos DNS y activos en más fuentes de información

**Registro Wildcard**: Cualquier consulta de subdominio tiene una respuesta.
Todos los subdominios que probemos tendrán una respuesta bálida pero no necesariamente útil.

###### Transferencias de zona
- **Transferencia de zona**: Copiar "zonas" de un servidor DNS (maestro) a otro (secundario).
      Transferencia de zona abierta = raro.
- **Zonas:** Conjunto de registros del mismo dominio.
      (ejemplo: consultas de dominio en las que dig nos da el registro A, AAAA, MX...)

###### Consulta inversa de dominio (reverse DNS lookup)
Cuando tenemos el bloque de IPs, vemos si responde a consultas inversas.
- **Consultas inversas**: Tenemos una IP y preguntamos al servidor DNS si posee registro para ella.
      Normalmente responderá, no con dominio real, sino con uno sintético (pseudo-dominio).

- **dnsrecon**: Consultas masivas.

###### Certificados SSL
Si el servidor expone un certificado en un puesto, lo examinamos para encontrar campos (CN, canonical name) de su dominio.

###### Certificate Transparency Logs
Para evidenciar certificados digitales, hay un sistema abierto donde se publican los certificados.
Podemos realizar una consulta a cualquiera de estos logs para encontrar certificados digitales (y subdominios) asociados a un dominio.

###### Consultas DNS pasivos
Son servidores y servicios que "escuchan" peticiones DNS realizadas por clientes y guardan la consulta. Se trata de capturar tráfico DNS de origen y su respuesta.
Se usan en honeypots, sandboxes, etc.
**¿Para qué?** Para vender la info, con el tiempo se va acumulando una BBDD util de consultas en el tiempo de un dominio y subdominios.

Se extraen colateralmente: 
- **archive.org**

Consultas pasivas:
- **subfinder**: Herramienta opensource para consultas pasivas - https://github.com/projectdiscovery/subfinder

##### Infraestructura Web
Ya tenemos un listado de dominios que mapean sobre IPs.
Hemos identificado los bloques y redes del objetivo (su presencia)
Ahora desactivaremos el "gran angular" y nos enfocamos en objetivos concretos: modelo de servidor web, versión de jQuery, etc. para raspar vulnerabilidades.

1. Establecemos contacto con el servidor.
2. Cualquier petición va a ser registrada, y si tiene patrón de ataque, encenderá una luz roja en la Defensa (SIEM) del objetivo.
3. Iremos aún volando por debajo del radar

##### Modo manual
Observar modelo y servidor web (a priori con la cabecera "Server" de respuesta):
**'curl -l <url>**

La mayoría de sitios están en servidores de terceros que ya tienen cabeceras por defecto.

##### Examen de páginas de error, trazas de ejecución o páginas típicas de servidores web por defecto
Buscar mediante:
###### **dorks**
######- **nmap**: Escáner de puertos originalmente, con LUA (motor de scripts) ahora es suite o framework recon (recomendado usar grep)
Ej: 'nmap www.campusciberseguridad.com -p443 --script httpserver-header'
###### Extensiones de navegador
- Wappalyzer
