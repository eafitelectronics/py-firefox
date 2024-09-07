import requests
import time
import subprocess

# Tiempo en segundos para cambiar de pestaña
TIME = 20

# URLs de las pestañas
URL_1 = "https://www.example.com"
URL_2 = "https://www.example.org"

# Función para verificar la conexión a Internet
def check_internet_connection(url="http://www.google.com", timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        # Si el código de estado es 200, hay conexión a Internet
        return response.status_code == 200
    except requests.ConnectionError:
        return False

# Espera hasta que haya conexión a Internet
while not check_internet_connection():
    print("Esperando conexión WiFi...")
    time.sleep(5)

# Cerrar cualquier instancia previa de Firefox
subprocess.call(["pkill", "firefox"])

# Esperar un momento para asegurarse de que Firefox se haya cerrado completamente
time.sleep(2)

# Comando para abrir Firefox en modo privado con un perfil específico
subprocess.Popen(["firefox", "--new-instance", URL_1, URL_2])

# Esperar un tiempo para asegurarse de que Firefox se haya abierto
time.sleep(5)

# Identificar la ventana de Firefox
window_id = subprocess.check_output(["xdotool", "search", "--onlyvisible", "--class", "firefox"]).decode().strip()

# Activar la ventana, y activar el modo pantalla completa con F11 en un único comando
subprocess.Popen(["xdotool", "windowactivate", window_id, "key", "F11"])

# Esperar un momento para asegurarse de que el modo pantalla completa se haya activado
time.sleep(2)

# Función para cambiar de pestaña
def switch_tabs(window_id):
    subprocess.Popen(["xdotool", "windowactivate", window_id, "key", "ctrl+Tab"])

# Cambiar de pestaña cada 20 segundos
try:
    while True:
        switch_tabs(window_id)
        time.sleep(TIME)
except KeyboardInterrupt:
    print("Script detenido.")
