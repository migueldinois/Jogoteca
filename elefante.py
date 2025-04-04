def elefante():
    contador = 1
    elefantes = int(input("Até que número você quer contar?: "))
    texto = "incomodam, "

    while contador <= elefantes:
        if contador == 1:
            print(f"1 Elefante incomoda muita gente")
            contador = 2
        if contador % 2 != 0: #IMPAR
            print(f"{contador} Elefantes incomodam muita gente")
        else:
            print(f"{contador} Elefantes {texto * (contador - 1)}incomodam muito mais! ")
        contador += 1
if __name__ == "__main__":
    elefante()
        