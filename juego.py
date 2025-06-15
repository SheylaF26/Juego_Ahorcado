print("_______________________")
print("|  JUEGO DE AHORCADO  |")
print("|  ADIVINA LA PALABRA |")
print("-----------------------")
print("PISTA: la palabra es de 4 letras")

palabra_secreta = "carro"
letras_adivinadas = []
intentos = 6  # Puedes cambiar esto si quieres más o menos vidas

while intentos > 0:
    letra = input("Ingresa una letra: ").lower()

    if letra in palabra_secreta:
        if letra not in letras_adivinadas:
            letras_adivinadas.append(letra)
            print("¡Bien! La letra está en la palabra.")
        else:
            print("Ya habías adivinado esa letra.")
    else:
        intentos -= 1
        print(f"Letra incorrecta. Te quedan {intentos} intentos.")

    # Mostrar el progreso de la palabra
    progreso = ""
    for letra_secreta in palabra_secreta:
        if letra_secreta in letras_adivinadas:
            progreso += letra_secreta + " "
        else:
            progreso += "_ "
    print("Palabra:", progreso.strip())

    # Verificar si ganó
    if all(letra in letras_adivinadas for letra in palabra_secreta):
        print("🎉 ¡Felicidades! Adivinaste la palabra:", palabra_secreta.upper())
        break
else:
    print("Te quedaste sin intentos. La palabra era:", palabra_secreta.upper())