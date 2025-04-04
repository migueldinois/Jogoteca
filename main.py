import time 
import random
import adivinhacao
import parouimparcomandor
import tabuada
import festa
import time
import jokenpo2
import elefante


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

while True:
    time.sleep(2)
    print("""
    ################################################      
    # ESCOLHA SEU JOGO                             #
    ################################################
    #   1 - Jogo de advinhação                     #
    #   2 - Par ou impar                           #               
    #   3 - Tabuadinha                             #
    #   4 - Verificador de festinha                #
    #   5 - Jokenpo                                #
    #   6 - Elefante Musica                        #
    #   0 - SAIR                                   #
    ################################################
    """, )
    
    opcaodejogo = int(input("Qual jogo você quer jogar?"))
    if opcaodejogo == 0:
        print("Espero que tenha se divertido!, até mais.")
        break

    elif opcaodejogo == 1:
        adivinhacao.jogoadivinhacao()
    elif opcaodejogo == 2:
        parouimparcomandor.parouimpar2()
    elif opcaodejogo == 3:
        tabuada.tabuada()
    elif opcaodejogo == 4:
        festa.festinha()
    elif opcaodejogo == 5:
        jokenpo2.jokenpo()
    elif opcaodejogo == 6:
        elefante.elefante()

