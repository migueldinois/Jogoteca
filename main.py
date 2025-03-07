import time 
import random
import adivinhacao
import parouimparcomandor
import tabuada
import festa



print("""

    
 ╦╔═╗╔═╗╔═╗╔╦╗╔═╗╔═╗╔═╗
 ║║ ║║ ╦║ ║ ║ ║╣ ║  ╠═╣
╚╝╚═╝╚═╝╚═╝ ╩ ╚═╝╚═╝╩ ╩

██████  ██ ██    ██ ██ ██████  ████████  █████        ███████ ███████ 
██   ██ ██ ██    ██ ██ ██   ██    ██    ██   ██       ██      ██      
██   ██ ██ ██    ██ ██ ██████     ██    ███████ █████ ███████ █████   
██   ██ ██  ██  ██  ██ ██   ██    ██    ██   ██            ██ ██      
██████  ██   ████   ██ ██   ██    ██    ██   ██       ███████ ███████ 
                                                                      
                                                                      

      

""")

print("""
################################################      
# ESCOLHA SEU JOGO                             #
################################################
#   1 - Jogo de advinhação                     #
#   2 - Par ou impar                           #               
#   3 - Tabuadinha                             #
#   4 - Verificador de festinha                #
################################################
""", )

opcaodejogo = int(input("Qual jogo você quer jogar?"))

if opcaodejogo == 1:
    adivinhacao.jogoadivinhacao()
elif opcaodejogo == 2:
    parouimparcomandor.parouimpar2()
elif opcaodejogo == 3:
    tabuada.tabuada()
elif opcaodejogo == 4:
    festa.festinha()

