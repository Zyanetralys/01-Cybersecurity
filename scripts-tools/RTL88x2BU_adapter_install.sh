#!/bin/bash

echo "🛠️  Instalación del driver RTL88x2BU"

# Actualiza repos y paquetes necesarios
echo "📦 Instalando dependencias..."
sudo apt update && sudo apt install -y build-essential dkms git linux-headers-$(uname -r)

# Clonar repositorio del driver
echo "📥 Clonando driver desde GitHub..."
git clone https://github.com/RinCat/RTL88x2BU-Linux-Driver.git
cd RTL88x2BU-Linux-Driver || exit

# Compilar e instalar
echo "⚙️ Compilando e instalando el driver..."
make && sudo make install

# Cargar el módulo
echo "🔌 Activando el módulo 88x2bu..."
sudo modprobe 88x2bu

# Verificar que la interfaz aparece
echo "📡 Buscando interfaz Wi-Fi..."
ip a | grep wlan

echo "✅ Instalación completada. Si no ves wlan0, reinicia la VM y ejecuta: sudo modprobe 88x2bu"