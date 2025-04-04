import random

print("""

    Bem vindo ao pedra, papel, tesoura!
    Jogue com seu oponente e tente ganhar!

""")


opcoes = ["PEDRA", "PAPEL", "TESOURA"]
opcao_bot = random.choice(opcoes)
pontosbot = 0
pontosjogador = 0

opcao_jogador = input("Escolha entre PEDRA, PAPEL e TESOURA!").upper()
while opcao_jogador not in opcoes:
    print("Opção Invalida")
    opcao_jogador = input("Escolha entre PEDRA, PAPEL OU TESOURA!").upper()
print(f"Você escolheu {opcao_jogador}")
print(f"Seu jogador escolheu {opcao_bot}")


while (pontosbot <= 3 ) or (pontosjogador <= 3):
    
    #Empate   
    if opcao_jogador == opcao_bot:
        print("Mesma escolha!, empate!")
        print(f"PLACAR VOCÊ: {pontosjogador} BOT: {pontosbot}")
        opcao_bot = random.choice(opcoes)
        opcao_jogador = input("Escolha entre PEDRA, PAPEL e TESOURA!").upper()
        while opcao_jogador not in opcoes:
            print("Opção Invalida")
            opcao_jogador = input("Escolha entre PEDRA, PAPEL OU TESOURA!").upper()
        print(f"Você escolheu {opcao_jogador}")
        print(f"Seu jogador escolheu {opcao_bot}")

    #Ganho Pedra
    elif opcao_jogador == "PEDRA" and opcao_bot == "TESOURA":
        print("Você venceu, parabéns!")
        pontosjogador = pontosjogador + 1
        print(f"PLACAR VOCÊ: {pontosjogador} BOT: {pontosbot}")
        opcao_bot = random.choice(opcoes)
        opcao_jogador = input("Escolha entre PEDRA, PAPEL e TESOURA!").upper()
        while opcao_jogador not in opcoes:
            print("Opção Invalida")
            opcao_jogador = input("Escolha entre PEDRA, PAPEL OU TESOURA!").upper()
        print(f"Você escolheu {opcao_jogador}")
        print(f"Seu jogador escolheu {opcao_bot}")
        
    #Ganho papel
    elif opcao_jogador == "PAPEL" and opcao_bot == "PEDRA":
        print("Você venceu, parabéns!")
        pontosjogador = pontosjogador + 1
        print(f"PLACAR VOCÊ: {pontosjogador} BOT: {pontosbot}")
        opcao_bot = random.choice(opcoes)
        opcao_jogador = input("Escolha entre PEDRA, PAPEL e TESOURA!").upper()
        while opcao_jogador not in opcoes:
            print("Opção Invalida")
            opcao_jogador = input("Escolha entre PEDRA, PAPEL OU TESOURA!").upper()
        print(f"Você escolheu {opcao_jogador}")
        print(f"Seu jogador escolheu {opcao_bot}")
        
    #Ganho tesoura
    elif opcao_jogador == "TESOURA" and opcao_bot == "PAPEL":
        print("Você venceu, parabéns!")
        pontosjogador = pontosjogador + 1
        print(f"PLACAR VOCÊ: {pontosjogador} BOT: {pontosbot}")
        opcao_bot = random.choice(opcoes)
        opcao_jogador = input("Escolha entre PEDRA, PAPEL e TESOURA!").upper()
        while opcao_jogador not in opcoes:
            print("Opção Invalida")
            opcao_jogador = input("Escolha entre PEDRA, PAPEL OU TESOURA!").upper()
        print(f"Você escolheu {opcao_jogador}")
        print(f"Seu jogador escolheu {opcao_bot}")

        
    else:
        print("Você perdeu, seu but!")
        pontosbot = pontosbot + 1
        print(f"PLACAR VOCÊ: {pontosjogador} BOT: {pontosbot}")
        opcao_bot = random.choice(opcoes)
        opcao_jogador = input("Escolha entre PEDRA, PAPEL e TESOURA!").upper()
        while opcao_jogador not in opcoes:
            print("Opção Invalida")
            opcao_jogador = input("Escolha entre PEDRA, PAPEL OU TESOURA!").upper()
        print(f"Você escolheu {opcao_jogador}")
        print(f"Seu jogador escolheu {opcao_bot}")
        
            
    if pontosbot == 3:
        print("Você perdeu!")
        print(f"Placar final: bot: {pontosbot} você: {pontosjogador}")
        break
    if pontosjogador == 3:
        print("Você ganhou!")
        print(f"Placar final: bot: {pontosbot} você: {pontosjogador}")
        break

        