# Jogo de adivinhação.
# Desenvolvido por Miguel Dinois
# 
import random

numero = random.randint(1, 10) 
chute = int(input("Chute um numero de 1 a 10: "))

if chute == numero:
    print(f"Você acertou!, parabéns!")
else:
    print(f"Errou!, o número era: {numero}")

