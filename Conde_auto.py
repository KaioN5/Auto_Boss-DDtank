import time
import pyautogui as pt

TOTAL_RODADAS = 200


def atacar_conde():
    rodada = 0

    # Ajuste único de ângulo no início da batalha
    for _ in range(25):
        pt.press('up')

    while rodada < TOTAL_RODADAS:
        time.sleep(6)  # Espera após entrar no evento

        # Alternar a direção do ataque
        if rodada % 4 == 0:
            # Conde ataca pela esquerda → você vira para a direita
            pt.press('left')
        else:
            # Conde ataca pela direita → você vira para a esquerda
            pt.press('right')

        # ATAQUE
        pt.typewrite('by239')
        pt.keyDown('space')
        time.sleep(3)
        pt.keyUp('space')
        time.sleep(6.2)

        rodada += 2  # Cada ciclo conta como 2 unidades
        print(f"Rodadas:{rodada}/{TOTAL_RODADAS}")

    # pt.alert("O conde foi derrotado!")


if __name__ == "__main__":
    atacar_conde()
