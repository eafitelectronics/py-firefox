# Python + Firefox

Este programa permite cambiar de pestaña cada 20 segundos en Firefox y usando una Raspberry Pi 4 o superior.

## Requisitos

- [Raspberry Pi 4 o superior](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/)
- [Python 3.11](https://www.python.org/downloads/)
- [Firefox](https://www.mozilla.org/es-ES/firefox/new/)
- [xdotool](https://atareao.es/software/utilidades/xdotool-simulando-raton-y-teclado/)

## Instalación

1. Instalar xdotool

   ```bash
   sudo apt update
   sudo apt install xdotool
   ```

2. Clonar el repositorio en el escritorio

   ```bash
   cd ~/Desktop
   git clone URL
   ```

   Reemplazar URL por la URL del repositorio

3. Modificar el archivo `py-firefox.py` para agregar las URLs de las pestañas que se quieren abrir

   ```python
   URL1 = "https://www.google.com"
   URL2 = "https://www.youtube.com"
   ```

   (Opcional) Modificar el tiempo de espera en la línea 6

   ```python
   TIEMPO = 20
   ```

4. Dar permisos de ejecución al archivo `py-firefox.py`

   ```bash
   chmod +x py-firefox.py
   ```

5. Crear ambiente virtual de Python e instalar las dependencias

   ```bash
   cd py-firefox
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

6. Crear un archivo de inicio automático para el script de Python en la carpeta `~/.config/autostart/` con el nombre `py-firefox.desktop`

   ```bash
   cd ~/.config/
   mkdir autostart
   nano py-firefox.desktop
   ```

   Pegar el siguiente contenido y reemplazar `TU_USUARIO` por el nombre de usuario de la Raspberry Pi

   ```desktop
   [Desktop Entry]
   Type=Application
   Exec=/home/TU_USUARIO/Desktop/py-firefox/env/bin/python /home/TU_USUARIO/Desktop/py-firefox/py-firefox.py
   Hidden=false
   NoDisplay=false
   X-GNOME-Autostart-enabled=true
   Name[en_US]=Autostart Py-Firefox Script
   Name=Autostart Py-Firefox Script
   Comment=Start Python script on boot
   ```

   Guardar y salir con `Ctrl + O` y `Ctrl + X`

7. Reiniciar la Raspberry Pi
   ```bash
   sudo reboot
   ```
   El script se ejecutará automáticamente al iniciar sesión
