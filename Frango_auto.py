import time
import pyautogui as pt  # pip install pyautogui


TOTAL_RODADAS = 100  # 100 ciclos de ataque (Frango + você)


def atacar_frango():
    """Executa o ataque automático Frango o Conde em DDTank."""
    rodada = 0

    pt.press('Right')  # Virar para a direita

    for _ in range(8):
        pt.press('Up')  # Ajustar Angulo para cima

    try:
        while rodada < TOTAL_RODADAS:
            time.sleep(6)  # Tempo do ataque Frango (implícito)

            pt.typewrite('by239')  # Seu ataque
            pt.keyDown('space')
            time.sleep(1.9)
            pt.press('space')
            time.sleep(5.0)

            rodada += 2  # cada ciclo conta como 2 rodadas
            print(f"rodadas:{rodada}/{TOTAL_RODADAS}")

    except KeyboardInterrupt:
        print(
            f"Automação interrompida em {rodada}/{TOTAL_RODADAS} rodadas (KeyboardInterrupt).")
        return

    print("Automação finalizada após 200 rodadas.")


if __name__ == "__main__":
    try:
        atacar_frango()
    except KeyboardInterrupt:
        print("Execução interrompida pelo usuário (KeyboardInterrupt) no nível principal.")
