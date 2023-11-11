from abc import *

# CLASES OBJETIVO

class Conectable(ABC):

    @abstractmethod
    def estaEncendida(self):
        pass

    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

class Lampara(Conectable):

    encendida = False

    def estaEncendida(self):
        return self.encendida

    def encender(self):
        self.encendida = True

    def apagar(self):
        self.encendida = False

class Computadora(Conectable):

    encendida = False

    def estaEncendida(self):
        return self.encendida

    def encender(self):
        self.encendida = True

    def apagar(self):
        self.encendida = False

# ADAPTABLE

class Calculator:

    on = False

    def isOn(self):
        return self.on

    def turnOn(self):
        self.on = True

    def turnOff(self):
        self.on = False

# ADAPTADOR

class AdaptadorCalculadora(Conectable):

    calculadora = Calculator()

    def estaEncendida(self):
        return self.calculadora.isOn()

    def encender(self):
        self.calculadora.turnOn()

    def apagar(self):
        self.calculadora.turnOff()

if __name__ == '__main__':

    # Lista de dispositivos, donde calculadora tiene una interfaz incompatible
    '''
    conectables = [Lampara(), Computadora(), Calculator()]

    for disp in conectables:
        disp.encender()
        print(f'{disp.__class__.__name__} encendida? {disp.estaEncendida()}')
        disp.apagar()
        print(f'{disp.__class__.__name__} encendida? {disp.estaEncendida()}')
    '''

    # Esto va a dar un error debido a la interfaz incompatible de Calculator
    # Pero si cambiamos el dispositivo por el adaptador

    conectables = [Lampara(), Computadora(), AdaptadorCalculadora()]

    for disp in conectables:
        disp.encender()
        print(f'{disp.__class__.__name__} encendida? {disp.estaEncendida()}')
        disp.apagar()
        print(f'{disp.__class__.__name__} encendida? {disp.estaEncendida()}')