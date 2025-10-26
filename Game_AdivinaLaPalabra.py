def game_adivina_la_palabra():
    print("Bienvenido al juego de Adivina la Palabra!")
    print("Jugador 1, igrese un palabra secreta")
    word_secret = input("Palabra secreta: ")
    
    print("Jugador 2, intenta adivinar la palabra: ")
    attempt = input()
    while attempt != word_secret:
        print("Incorrecto, intenta de nuevo")
        attempt = input()
    else:
        print("¡Felicidades! Has adivinado la palabra: ")