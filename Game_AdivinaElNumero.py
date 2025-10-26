def game_adivina_el_numero():
    print("Bienvenido al juego de Adivina el Número!")
    print("Jugador 1, igrese un número secreto")
    number_secret = input("Número secreto: ")
    
    print("Jugador 2, intenta adivinar el número")
    attempt = input()
    while attempt != number_secret:
        print("Incorrecto, intenta de nuevo")
        attempt = input()
    else:
        print("¡Felicidades! Has adivinado el número.")
