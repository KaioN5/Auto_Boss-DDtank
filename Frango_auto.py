import time
import pyautogui as pt


TOTAL_RODADAS = 200  # 100 ciclos de ataque (Frango + você)


def atacar_frango():
    rodada = 0

    pt.press('Right')  # Virar para a direita

    for _ in range(8):
        pt.press('Up')  # Ajustar Angulo para cima

    while rodada < TOTAL_RODADAS:
        time.sleep(6.2)  # Tempo do ataquedo Frango (implícito)

        pt.typewrite('239')  # Seu ataque
        pt.keyDown('space')
        time.sleep(3)
        pt.press('space')
        time.sleep(5.9)

        rodada += 2  # cada ciclo conta como 2 rodadas
        print(f"rodadas:{rodada}/{TOTAL_RODADAS}")

    print("Automação finalizada após 200 rodadas.")


if __name__ == "__main__":
    atacar_frango()
