import time
import pyautogui as pt  # pip install pyautogui


TOTAL_RODADAS = 200  # 100 ciclos de ataque (dragão + você)


def atacar_dragao():
    rodada = 0

    pt.press('Right')  # Virar para a direita

    for _ in range(8):
        pt.press('Up')  # Ajustar Angulo para cima

    while rodada < TOTAL_RODADAS:
        time.sleep(6.2)  # Tempo do ataque do dragão (implícito)

        pt.typewrite('by239')  # Seu ataque
        pt.keyDown('space')
        time.sleep(1.9)
        pt.press('space')
        time.sleep(6.8)

        rodada += 2  # Cada ciclo conta como 2 rodadas
        print(f"Rodadas:{rodada}/{TOTAL_RODADAS}")

    print("Automação finalizada após 200 rodadas.")


if __name__ == "__main__":
    atacar_dragao()
