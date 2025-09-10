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

**- Burp Suite:** suite completa de seguridad web, auditoría, bug bounting, cara
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
4. Pasar por un proxy (como Tor) o tener una máquina en una localización geográfica. Ese proxy o máquina es la IP que conecta con el objetivo.
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


