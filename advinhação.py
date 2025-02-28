# Jogo de adivinhação.
# Desenvolvido por Miguel Dinois

#Niveis
#Facil 1 a 10
#Medio 1 a 20
#Dificil 1 a 100
#Senai 1 a 1000

import random

print("""
################################################
#  ⋆ 1 - Fácil (1 a 10)                         #
#  ✧ 2 - Médio (1 a 20)                        #               
#  ☆ 3 - Difícil (1 a 100)                     #
#  ★ 4 - Senai (1 á 1000)                      #
################################################
""")

escolhendonivel = int(input("Qual nivel você gostaria de jogar?"))
valormaximo = 0


# Nivel Noob
if escolhendonivel == 1:
    print("Você escolheu o Nivel Noob!")
    valormaximo = 10

# Nivel Médio
elif escolhendonivel == 2:
    print("Você escolheu o Nivel Médio!")
    valormaximo = 20

# Nivel Difícil
elif escolhendonivel == 3:
    print("Você escolheu o Nivel Difícil!")
    valormaximo = 100

# Nivel Senai
elif escolhendonivel == 4:
    print("Você escolheu o Nivel Senai!")
    valormaximo = 1000
else:
    print("Você deve escolher uma dificuldade entre 1 e 4")

numero = random.randint(1, valormaximo)
escolha = int(input(f"Escolha um numero entre 1 á {valormaximo}"))

if escolha == numero:
        print("Parabéns!, você acertou!")   
else:
        print(f"Você errou!, o número era: {numero}")
    



