import random

def parouimpar2():
    escolha = int(input("Escolha entre ímpar ou par, 1 para par e 2 para ímpar"))
    numero_bot = random.randint(1, 10)
    numero = int(input("Escolha um numero de dedos"))
    soma = numero_bot + numero


    if ((escolha == 1) and (soma % 2 == 0)) or ((escolha == 2) and (soma % 2 >1)):
        print(f"Nossos números somados deram {soma} tu ganhaste")

    else:
        print("Nossos números somados deram {soma} tu perdeu bobinho")

if __name__ == "__main__":
    parouimpar2()

