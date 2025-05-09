# "as" pra salvar o nome mais curto
import forca as f

f.bem_vindo()

palavra_secreta = f.palavra_aleatoria()



tracos = f.montar_tracos(palavra_secreta)
print(*tracos)

letras_erradas = 0
while True:
    
    f.desenhar_forca(letras_erradas)
    letra = f.perguntar_letra()

    if letra in palavra_secreta:
        tracos = f.verificar_letra(tracos,palavra_secreta,letra)
    else:
        print("Você errou +1 letra")
        letras_erradas = letras_erradas + 1
        
       
    
    print(*tracos)

    if "_" not in tracos:
        print("Você ganhou!")
        break
    if letras_erradas == 6:
        print("Você perdeu bbzao")
        print(f"A palavra era {palavra_secreta}")
        break   