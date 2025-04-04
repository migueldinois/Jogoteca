import pyautogui

pyautogui.press("WIN")
pyautogui.write("NOTAS")
pyautogui.press("ENTER")

contador = 1
elefantes = 5
texto = "incomodam, "

while contador <= elefantes:
    if contador % 2 != 0:
        pyautogui.write(f"{contador} Elefantes incomodam muita gente \n")
    else:
        pyautogui.write(f"{contador} Elefantes {texto * contador }muito mais! \n")
    contador += 1

