import random
import time


def parouimpar():
    escolha_par_ou_impar = int(input("Escolha entre ímpar ou Par (1 para par e 2 para ímpar): "))
    numero_bot = random.randint(1, 10)
    numero_player = int(input("Escolha um número de 1 a 10: "))

    resultado = numero_bot + numero_player

    print(f"Seu número: {numero_player} numero do inimigo: {numero_bot}, Soma: {resultado}")
    if escolha_par_ou_impar == 1:
        print("Você escolheu PAR!, iniciando jogo...")
        time.sleep(2)
        if resultado % 2 == 0:
            print(f"Você ganhou!, o número {resultado} é PAR!")
        else:
            print(f"Você perdeu!, o número {resultado} é ímpar!")
    if escolha_par_ou_impar == 2:
        print("Você escolheu ímpar!!, iniciando jogo...")
        time.sleep(2)
        if resultado % 2 > 0:
            print(f"Você ganhou!, o número {resultado} é ímpar")
        else:
            print(f"Você perdeu!, o número {resultado} PAR!")


if __name__ == "__main__":
    parouimpar()

