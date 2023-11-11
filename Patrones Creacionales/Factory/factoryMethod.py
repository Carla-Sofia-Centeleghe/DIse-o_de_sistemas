from abc import *
import math

#* CREATORS

# CREADOR ABSTRACTO
class TrianguloFactory(ABC): 

    @abstractmethod
    def createTriangulo(self):
        pass

# CREADORES CONCRETOS
class IsoscelesFactory(TrianguloFactory):

    def createTriangulo(self, ladoA:int, ladoB:int, ladoC:int):
        return Isosceles(ladoA, ladoB, ladoC)

class EscalenoFactory(TrianguloFactory):

    def createTriangulo(self, ladoA:int, ladoB:int, ladoC:int):
        return Escaleno(ladoA, ladoB, ladoC)

class EquilateroFactory(TrianguloFactory):

    def createTriangulo(self, ladoA:int, ladoB:int, ladoC:int):
        return Equilatero(ladoA, ladoB, ladoC)

#* PRODUCTS

# PRODUCTO ABSTRACTO
class Triangulo(ABC):
    
    def __init__(self, ladoA:int, ladoB:int, ladoC:int):
        
        self.ladoA = ladoA 
        self.ladoB = ladoB
        self.ladoC = ladoC

    @abstractmethod
    def getDescription(self):
        return "Es un triangulo"

    @abstractmethod
    def getSuperficie(self):
        P = self.ladoA + self.ladoB + self.ladoC
        S = P / 2
        return math.sqrt(S*(S-self.ladoA)*(S-self.ladoB)*(S-self.ladoC))


# PRDUCTOS CONCRETOS
class Isosceles(Triangulo):

    def getDescription(self):
        return "Es un triangulo Isosceles, es decir, tiene 2 lados iguales"

    def getSuperficie(self):
        return super().getSuperficie()

class Escaleno(Triangulo):

    def getDescription(self):
        return "Es un triangulo Escaleno, es decir, tiene los 3 lados distintos"

    def getSuperficie(self):
        return super().getSuperficie()

class Equilatero(Triangulo):

    def getDescription(self):
        return "Es un triangulo Equilatero, es decir, tiene los 3 lados iguales"

    def getSuperficie(self):
        return super().getSuperficie() # super() da acceso a metodos y propiedades de una clase padre

def main():

    escalenoFactory = EscalenoFactory()
    isoscelesFactory = IsoscelesFactory()
    equilateroFactory = EquilateroFactory()

    escaleno = escalenoFactory.createTriangulo(4,5,6)
    isosceles = isoscelesFactory.createTriangulo(4,4,6)
    equilatero = equilateroFactory.createTriangulo(4,4,4)

    print(escaleno.getDescription())
    print(escaleno.getSuperficie())
    print(isosceles.getDescription())
    print(isosceles.getSuperficie())
    print(equilatero.getDescription())
    print(equilatero.getSuperficie())

if __name__ == '__main__':

    main()