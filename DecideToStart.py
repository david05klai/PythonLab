from Welcome import PlayerName
from MenuGame import OptionsGame
from FarewellWindow import Farewell

def Desicion():
    Name = PlayerName()
    print(f"Ok {Name}, ¿Deseas iniciar el juego)?")
    print("1. Sí")
    print("2. No")
    match input():
        case "1":
            return OptionsGame(Name) 
        case "2":
            return Farewell(Name)
        case _:
            print("Opción no válida. Por favor, intenta de nuevo.")
            return Desicion()
