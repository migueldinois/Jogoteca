import random

def jokenpo():
    print("""

        Bem vindo ao pedra, papel, tesoura!
        Jogue com seu oponente e tente ganhar!

    """)

    pontos_user = 0
    pontos_bot = 0

    while True:
        # Escolhendo as opções, tanto do bot quanto do usúario!
        opcoes = ["PEDRA", "PAPEL", "TESOURA"]
        opcao_bot = random.choice(opcoes)
        opcao_jogador = input("Escolha entre Pedra, Papel ou Tesoura").upper()
        # Verificando as opcoes!
        while opcao_jogador not in opcoes:
            print("Opção Invalida!")
            opcao_jogador = input("Escolha entre Pedra, Papel ou Tesoura").upper()
        print(f"Você escolheu: {opcao_jogador}")
        print(f"Oponente escolheu: {opcao_bot}")
        #Empate
        if opcao_bot == opcao_jogador:
            print("EMPATE!")
        #Ganhos possiveis
        elif (opcao_jogador == "PEDRA" and opcao_bot == "TESOURA") or (opcao_jogador == "PAPEL" and opcao_bot == "PEDRA") or (opcao_jogador == "TESOURA" and opcao_bot == "PAPEL"):
            print("Você ganhou 1 ponto!")
            pontos_user += 1
        #Perdeu
        else:
            print("Seu oponente ganhou!")
            pontos_bot += 1
        #Placar
        print(f"""Placar atual:
            
            BOT    |   VOCÊ
            ({pontos_bot})           ({pontos_user})
            
            """)
        # Vendo quem ganhou a melhor de 3
        if pontos_user == 3:
            print("Parabéns!, você ganhou!")
            break
        if pontos_bot == 3:
            print("O seu oponente ganhou!, você perdeu!")
            break
        
if __name__ == "__main__":
    jokenpo()