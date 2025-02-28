# Jogo de adivinhação.
# Desenvolvido por Miguel Dinois

#Niveis
#Facil 1 a 10
#Medio 1 a 20
#Dificil 1 a 100
#Senai 1 a 1000

import random

print("""
      

    ⋆ 1 - Facil (1 a 10)
    ✧ 2 - Médio (1 a 20)
    ☆ 3 - Difícil (1 a 100)
    ★ 4 - Senai (1 á 1000)

""")

escolhendonivel = int(input("Qual nivel você gostaria de jogar?"))

# Nivel Noob
if escolhendonivel == 1:
    print("Você escolheu o Nivel Noob!")
    numero = random.randint(1, 10)
    escolha = int(input("Escolha um número de 1 a 10!"))
    if escolha == numero:
        print("Parabéns!, você acertou!")   
    else:
        print(f"Você errou!, o número era: {numero}")

# Nivel Médio
elif escolhendonivel == 2:
    print("Você escolheu o Nivel Médio!")
    numero = random.randint(1, 20)
    escolha = int(input("Escolha um número de 1 a 20!"))
    if escolha == numero:
        print("Parabéns!, você acertou!")   
    else:
        print(f"Você errou!, o número era: {numero}")

# Nivel Difícil
elif escolhendonivel == 3:
    print("Você escolheu o Nivel Difícil!")
    numero = random.randint(1, 100)
    escolha = int(input("Escolha um número de 1 a 100!"))
    if escolha == numero:
        print("Parabéns!, você acertou!")   
    else:
        print(f"Você errou!, o número era: {numero}")

# Nivel Difícil
elif escolhendonivel == 4:
    print("Você escolheu o Nivel Senai!")
    numero = random.randint(1, 1000)
    escolha = int(input("Escolha um número de 1 a 1000!"))
    if escolha == numero:
        print("Parabéns!, você acertou!")   
    else:
        print(f"Você errou!, o número era: {numero}")
else:
    print("Você deve escolher uma dificuldade entre 1 e 4")



