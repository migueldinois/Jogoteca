import random
import time
import winsound as w


lista_palavras = [ "escola", "janela", "teclado", "cinema", "musica", "planeta", "cadeira", "garrafa", 
                   "caderno", "cidade", "boneca", "relogio", "tapete", "sorriso", "segredo", "aventura",
                     "floresta", "montanha", "piscina", "espelho", "caneta", "tesoura", "pintura", "abraço", 
                     "desejo", "saudade", "silencio", "passeio", "receita", "fantasia", "presente", "lembrança", 
                     "cuidado", "carinho", "respeito", "verdade", "justiça", "liberdade", "amizade", "familia", 
                     "trabalho", "estudo", "viagem", "esporte", "lazer", "paixao", "cultura", "historia", "futuro",
                       "passado", "presente", "sonho", "magia", "beleza", "força", "sabedoria", "coragem", "bondade",
                         "alegria", "tristeza", "raiva", "medo", "calma", "festa", "dança", "teatro", "poema", "livro", 
                         "filme", "jogo", "radio", "televisão", "internet", "computador", "celular", "fotografia", "pintura", 
                         "escultura", "arquitetura", "jardim", "praia", "rio", "lago", "chuva", "vento", "sol", "lua", "estrela",
                           "nuvem", "terra", "fogo", "ar", "planta", "animal", "pessoa", "mundo", "tempo", "lugar", "banana", "maça" ]

# Funcoes
def escolher_palavra():
  palavra = random.choice(lista_palavras)
  return palavra
def imprimir_forca(erros):
  if erros == 0:
    print(f"""
    _____
    |   |
    |
    |
    |
    |
    |
    |  
    | {"— " * letras}
  """)
  if erros == 1:
    print(f"""
    _____
    |   |
    |   O
    |
    |
    |
    |
    |  
    | {"— " * letras}
  """)
    if erros == 2:
      print(f"""
      _____
      |   |
      |   O
      |   |
      |   |
      |
      |
      |  
      | {"— " * letras}
    """)
    if erros == 3:
      print(f"""
      _____
      |   |
      |   O
      |   |
      |   |
      |  / 
      |
      |  
      | {"— " * letras}
    """)
    if erros == 4:
      print(f"""
      _____
      |   |
      |   O
      |   |
      |   |
      |  / \\
      |
      |  
      | {"— " * letras}
    """)
    if erros == 5:
      print(f"""
      _____
      |   |
      |   O
      |   |\\
      |   |
      |  / \\
      |
      |  
      | {"— " * letras}
    """)
    if erros == 6:
      print(f"""
      _____
      |   |
      |   O
      |  /|\\
      |   |
      |  / \\
      |
      |  
      | {"— " * letras}
    """)

palavra = escolher_palavra()
letras = len(palavra)

input("SEJA BEM VINDO AO JOGO DA FORCA!, PRESSIONE ENTER PARA COMEÇAR!")






