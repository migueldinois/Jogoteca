import random 
import time


def bem_vindo():
     print("""
           ♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛
            ♛ BEM VINDO AO JOGO DA FORCA! ♛
           ♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛


""")


def palavra_aleatoria():
      arquivo = open("palavras.txt", "r") # a funcao open ela abre um arquivo e escolhe o que vai fazer com ela Ler = r escrever = w acrescentar = a 
      lista_palavras = arquivo.read().split() # arquivo.read le o arquivo aberto e corta com o split, separando cada palavra com enter, ou algo que esteja dentro da funcao slip
      arquivo.close()
      palavra_escolhida = random.choice(lista_palavras)
      return palavra_escolhida.upper()

def desenhar_forca(erros):
      if erros == (0):
            print("""
                        ___________
                        |          |
                        |         
                        |      
                        |
                        |
                        |
                                    
                              """)

      elif erros == (1):
            print("""
                        ___________
                        |          |
                        |         😉
                        |      
                        |
                        |
                        |
                              
                              """)


      elif erros == (2):
            print("""
                        ___________
                        |          |
                        |         🤨
                        |          |
                        |
                        |
                        |
                              
                              """)

      elif erros == (3):
            print("""
                        ___________
                        |          |
                        |         😐
                        |          |
                        |           \\
                        |
                        |
                              
                              """)

      elif erros == (4):
            print("""
                        ___________
                        |          |
                        |         😶
                        |          |
                        |         / \\
                        |
                        |
                              
                              """)

      elif erros == (5):
            print("""
                        ___________
                        |          |
                        |         😭
                        |          |\\
                        |         / \\
                        |
                        |
                              
                              """)


      elif erros == (6):
            print("""
                        ___________
                        |          |
                        |         😨
                        |         /|\\
                        |         / \\
                        |
                        |
                              
                              """)

def perguntar_letra():
     letra = input("chute uma letra: ") #fala pro usuario digitar uma letra
     letra = letra.upper() #deixar a letra em maiusculo
     quantidade = int(len(letra))
     while True:
          resposta = letra
          if len(resposta) != 1 and resposta.isalpha() == False:  #isalpha = se está no alfabeto usa assim A.isalpha ou variavel no lugar do A 
               letra = input("resposta invalida, digite uma letra: ")
          else:
               return letra.upper()

def montar_tracos(palavra) -> list[str]:
     tracos = []
     contador = 0
     qtdeletras = len(palavra)
     while contador < qtdeletras:
          tracos.append("_")
          contador += 1
     return tracos

def verificar_letra(tracos,palavra,letra) -> list[str]:
     contador = 0
     for percorrida in palavra:
          if percorrida == letra:
               tracos[contador] = letra
          contador = contador + 1
     return tracos

def fim_de_jogo(resultado):
     if resultado == desenhar_forca(0):
          fim_de_jogo == "VITORIA"

     if resultado == desenhar_forca(6):
          fim_de_jogo == "GAMEOVER"
          
