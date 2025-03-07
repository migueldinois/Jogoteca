def festinha():

    dia = input("Que dia é hoje?")
    idade = int(input("Qual a sua idade"))

    if ((dia == "Sabado") or (dia == "Domingo")) and (idade >= 18) :
            print("Bora festejar papi, beber até o talo.")
    else: 
            print("Os guri de porto alegre, vai tomar só suco na baia.")

if __name__ == "__main__":
       festinha()