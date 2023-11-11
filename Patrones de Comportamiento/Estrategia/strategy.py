from abc import ABC, abstractmethod

## Interface 
class Estrategia(ABC):
    @abstractmethod
    def elegir(self):
        pass

## Estrategias Concretas
class Piedra(Estrategia):
    ## metodo de la interface
    def elegir(self):
        return "Piedra"

class Papel(Estrategia):
    def elegir(self):
        return "Papel"

class Tijeras(Estrategia):
    def elegir(self):
        return "Tijeras"

## Clase Contexto
class Juego:
    def __init__(self, Estrategia):
        self.Estrategia = Estrategia

    def play(self, jugador):
        s1 = self.Estrategia.elegir()
        s2 = jugador.Estrategia.elegir()
        if s1 == s2:
            print("Empate!")
        elif s1 == "Piedra":
            if s2 == "Tijeras":
                print("Jugador 1 gana!")
            else:
                print("Jugador 2 gana!")
        elif s1 == "Tijeras":
            if s2 == "Papel":
                print("Jugador 1 gana!")
            else:
                print("Jugador 2 gana!")
        elif s1 == "Papel":
            if s2 == "Piedra":
                print("Jugador 1 gana!")
            else:
                print("Jugador 2 gana!")

if __name__ == '__main__':
    ## Jugador 1 elije su estrategia
    jugador1 = Juego(Papel())

    # Jugador 2 elije su estrategia
    jugador2 = Juego(Piedra())

    # Luego de que el jugador 2 elije, se juega
    jugador1.play(jugador2)