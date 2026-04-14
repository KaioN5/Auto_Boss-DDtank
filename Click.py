import time
import pyautogui # pip install pyautogui

# Aguarda 3 segundos antes de capturar a posição do mouse
print("Posicione o mouse onde deseja capturar. Aguarde 3 segundos...")
time.sleep(5)

# Captura a posição do mouse
x, y = pyautogui.position()

# Exibe a posição
print(f"A posição atual do mouse é: X={x}, Y={y}")
