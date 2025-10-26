from FarewellWindow import Farewell
from Game_AdivinaElNumero import game_adivina_el_numero
from Game_AdivinaLaPalabra import game_adivina_la_palabra
def OptionsGame(Name):
    print(f"Ok {Name}, Escoge tu juego")
    print("1. Adivina el número")
    print("2. Adivina la palabra")
    print("3. Salir")
    match input():
        case "1":
            game_adivina_el_numero()
        case "2":
            game_adivina_la_palabra()  
        case "3":
            return Farewell(Name)
        case _:
            print("Opción no válida. Por favor, intenta de nuevo.")
            return OptionsGame(Name)