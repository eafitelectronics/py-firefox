import requests
import time
import subprocess

# Tiempo en segundos para cambiar de pestaña
TIEMPO_1 = 60
TIEMPO_2 = 5

# URLs de las pestañas
URL_1 = "https://www.google.com"
URL_2 = "https://www.eafit.edu.co"


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
#subprocess.Popen(["firefox", "--new-instance", URL_1])

# Esperar un tiempo para asegurarse de que Firefox se haya abierto
time.sleep(10)

# Identificar la ventana de Firefox
window_id = (
    subprocess.check_output(
        ["xdotool", "search", "--onlyvisible", "--class", "firefox"]
    )
    .decode()
    .strip()
)

# Activar la ventana, y activar el modo pantalla completa con F11 en un único comando
subprocess.Popen(["xdotool", "windowactivate", window_id, "key", "F11"])

# Esperar un momento para asegurarse de que el modo pantalla completa se haya activado
time.sleep(4)

# Obtener la resolución de la pantalla para mover el cursor a la esquina inferior derecha
screen_width = (
    subprocess.check_output(["xdotool", "getdisplaygeometry"]).decode().split()[0]
)
screen_height = (
    subprocess.check_output(["xdotool", "getdisplaygeometry"]).decode().split()[1]
)

# Mover el cursor a la esquina inferior derecha
subprocess.Popen(["xdotool", "mousemove", screen_width, screen_height])


# Función para cambiar de pestaña
def switch_tabs(window_id):
    subprocess.Popen(["xdotool", "windowactivate", window_id, "key", "ctrl+Tab"])

def activate_tab(window_id, tab_id):
    subprocess.Popen(["xdotool", "windowactivate", window_id, "key", f"ctrl+{tab_id}"])

# Cambiar de pestaña cada 20 segundos
try:
    while True:
        #switch_tabs(window_id)
        activate_tab(window_id, 1)
        subprocess.Popen(["xdotool", "windowactivate", window_id, "key", "F11"])
        time.sleep(TIEMPO_1)
        activate_tab(window_id, 2)
        subprocess.Popen(["xdotool", "windowactivate", window_id, "key", "F11"])
        time.sleep(TIEMPO_2)
except KeyboardInterrupt:
    print("Script detenido.")