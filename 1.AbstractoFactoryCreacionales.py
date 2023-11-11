from __future__ import annotations
from colorama import init, Fore, Style
from abc import ABC, abstractmethod

init(autoreset=True)

#---------------------------------Fabrica Abstracta
class Galeria_arte(ABC):
    @abstractmethod
    def crear_cuadro(self):
        pass

    @abstractmethod
    def crear_estatua(self):
        pass

#-------------------------------------Fabrica Concreta 1, CUBISMO
class FabricaCubismo(Galeria_arte):

    def crear_cuadro(self):
        return cuadro_cubismo()

    def crear_estatua(self):
        return estatua_cubismo()

#-------------------------------------Fabrica Concreta 2, REALISMO
class FabricaRealismo(Galeria_arte):

    def crear_cuadro(self):
        return cuadro_realismo()

    def crear_estatua(self):
        return estatua_realismo()

#---------------------------------------Producto Abstracto 1, CUADRO
class Cuadro(ABC):

    @abstractmethod
    def funcion_cuadro(self):
        pass

#---------------------------------------Producto Concreto 1.1, Cuadro
class cuadro_cubismo(Cuadro):
    def funcion_cuadro(self):
        return "Cuadro " + Fore.MAGENTA + "Cubismo" + Fore.WHITE + ", chica linda"

#-----------------------------------------Producto Concreto 1.2, Cuadro
class cuadro_realismo(Cuadro):
    def funcion_cuadro(self):
        return "Cuadro " + Fore.GREEN + "Realismo" + Fore.WHITE + ", prendieron las luces del boliche"

#-------------------------------------------Producto Abstracto 2, ESTATUA
class Estatua(ABC):

    @abstractmethod
    def funcion_estatua(self):
        pass

#--------------------------------------------Productos Concretos 2.1, Estatua
class estatua_cubismo (Estatua):
    def funcion_estatua(self):
        return "Estatua " + Fore.MAGENTA + "Cubismo" + Fore.WHITE + ", la bella durmiente"

#---------------------------------------------Productos Concretos 2.2, Estatua
class estatua_realismo(Estatua):
    def funcion_estatua(self):
        return "Estatua " + Fore.GREEN + "Realismo" + Fore.WHITE + ", ella ronca"

#-----------------------------CLASE CLIENTE, el es el que utiliza los metodos abstractos, como si fueran concretos
class cliente:
    def client_code(self, Galeria_arte):
   
        Cuadro = Galeria_arte.crear_cuadro()
        Estatua = Galeria_arte.crear_estatua()
    
        print(Cuadro.funcion_cuadro())
        print(Estatua.funcion_estatua())

#------------------------------------El MAIN
if __name__ == "__main__": 

    c = cliente()
    print(Fore.MAGENTA + "F A B R I C A   D E   C U B I S M O")
    c.client_code(FabricaCubismo())
    print("\n")
    print(Fore.GREEN + "F A B R I C A   D E    R E A L I S M O") 
    c.client_code(FabricaRealismo())


       