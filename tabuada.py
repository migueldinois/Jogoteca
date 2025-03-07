import random 

def tabuada():
    print("""
        ################################################
        #                ⋆ 1 - Fácil (1 a 10)          #
        ################################################  
        """)
    nivel = int(input("Qual nivel você quer jogar?"))
    numero1 = random.randint(1, 10)
    numero2 = random.randint(1, 10)
    resultado = numero1 * numero2

    if nivel == 1:
        print("Você escolheu o nível facil!")
        print(f"Desafio: {numero1}x{numero2}")
        resposta = int(input("Qual o resultado dessa conta?: "))

        if resposta == resultado:
            print("Você acertou!, parábens!")
        else:
            print(f"Você errou, era: {resultado}")

if __name__ == "__main__":
    tabuada()

    