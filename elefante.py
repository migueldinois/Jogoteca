def elefante():
    contador = 1
    elefantes = int(input("Até que número você quer contar?: "))
    texto = "incomodam, "

    while contador <= elefantes:
        if contador % 2 != 0:
            print(f"{contador} Elefante(s) incomodam muita gente")
        else:
            print(f"{contador} Elefante(s) {texto * contador}muito mais! ")
        contador += 1
if __name__ == "__main__":
    elefante()
        