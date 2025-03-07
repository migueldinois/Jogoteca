import random

def parouimpar2():
    escolha = int(input("Escolha entre ímpar ou par, 1 para par e 2 para ímpar"))
    numero_bot = random.randint(1, 10)
    numero = 0

    if escolha == 1: #PAR
        print(f"Você escolheu PAR!")
        numero = int(input("Escolha um número de dedos: "))
        soma = numero + numero_bot 
        print(f"Seu número:{numero}, Número do inimigo: {numero_bot}, Soma: {soma}")
        if escolha == 1 and soma % 2 == 0:
            print(f"Você ganhou! a soma dos numeros é PAR! ({soma})") 
        else:
            print(f"Você perdeu! a soma dos numeros é ímpar! ({soma})") 
    elif escolha == 2: #ÍMPAR
        print(f"Você escolheu ÍMPAR!")
        numero = int(input("Escolha um número de dedos: "))
        soma = numero + numero_bot 
        print(f"Seu número:`{numero}, Número do inimigo: {numero_bot}, Soma: {soma}")
        if escolha == 2 and soma % 2 > 0:
            print(f"Você ganhou! a soma dos numeros é ímpar! ({soma})") 
        else:
            print(f"Você perdeu! a soma dos numeros é PAR! ({soma})") 
        
    else:
        print("Escolha uma seleção existente.")

if __name__ == "__main__":
    parouimpar2()

