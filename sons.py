import winsound
import time


def win():
    winsound.PlaySound("win.wav", winsound.SND_FILENAME) #Entre "" o caminho do som e depois os argumentos, que seria que tipo de arquivo é "winsound.SND_FILENAME" para falar q é som

def lose():
        winsound.PlaySound("lose.wav", winsound.SND_FILENAME) # SND FILE NAME SERia para falar que e um arquivo de som!
def noob():
        winsound.PlaySound("noob.wav", winsound.SND_FILENAME) # SND FILE NAME SERia para falar que e um arquivo de som!
def medio():
        winsound.PlaySound("medio.wav", winsound.SND_FILENAME) # SND FILE NAME SERia para falar que e um arquivo de som!
def dificil():
        winsound.PlaySound("dificil.wav", winsound.SND_FILENAME) # SND FILE NAME SERia para falar que e um arquivo de som!



if __name__ == "__main__":
    lose()
    