import winsound as w # Frameyork para emitir sons
import random 
import time

sons = [300, 500, 800, 1000]
sequencia = []
contador = 0
indice = 0 
qnt = len(sequencia)

# Mensagens de boas vindas e ensinando
print("Bem vindo ao jogo!, seu objetivo é memorizar a sequência que irá tocar os sons!, Boa sorte amigo!")
print("Frequência de 1 (Mais aguda) a 4 (Mais grave)")

input("Pressione enter para ir para a próxima página")

# Mostrando as frequencias
print("Preste atenção que iria te mostrar o som e seus números!, está em ordem 0,1,2,3")
time.sleep(2)
for primeiro in sons: #for = percorrer, indo de 1 em 1
    print(f"Som {contador}:")
    w.Beep(primeiro, 500) # esse for primeiro seria que PARA primeiro (variavel descartavel), dentro de sons IN, ele vai fazer isso 4 vezes pois tem 4 itens na lista
    contador += 1
    time.sleep(0.5)

while True:
    input("Pressione Enter se estiver preparado para o desafio!")
    # Escolhendo frequencia aleatoria 
    som_escolhido = random.choice(sons)
    sequencia.append(som_escolhido) # Adicionar a frequecia aleatoria a lista sequencia


    for som in sequencia:
        w.Beep(som_escolhido, 500)
        time.sleep(0.5)

        # Perguntando ao usuario a sequencia que tocou?
    chute = input("Qual a sequência que tocou agora? Ex: 0123")

    vencedor = True
    for numero in chute:
        numero = int(numero)
        if chute == qnt: # Len é para saber a quantidade de palavras que tem na lista (numeros ou palavras)
            if sons[numero] != sons[indice]:
                print(f"Você errou a frequência {chute}!")
                vencedor = False
            
        indice += 1
    if vencedor == False:
        print("Você Perdeu!")
        break


    if vencedor == True:
        print("Parábens!, você acertou a sequencia!")
        



