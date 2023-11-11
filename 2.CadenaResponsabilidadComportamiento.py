from colorama import init, Fore, Style
from abc import ABC, abstractstaticmethod

init(autoreset=True)
# -----------------Manejador Abstracto

class Cumpleanios(ABC): 
    @abstractstaticmethod
    def set_sucesor(sucesor):
        pass

    @abstractstaticmethod
    def set_cantidad(cantidad):
        pass 

#------------------Manejadores Concretos, vamos a tener 3 de ellos

class Anios(Cumpleanios): #----------------------------------AÑOS
    def __init__(self):
        self._sucesor = None

    def set_sucesor(self, sucesor):
        self._sucesor = sucesor #Aca definimos el siguiente manejador de la cadena

    def set_cantidad(self, cantidad):
        if cantidad >= 365:
            num = cantidad // 365 #Nos devuelve el cociente 
            resto = cantidad % 365 #Nos devuelve el resto

            print("Faltan " + Fore.MAGENTA + f"{num} anios" + Fore.WHITE +" para el cumpleaños") #Printeo el cociente

            if resto != 0:  #Si el resto nos da diferente de cero, pasaría al siguiente manejador de la cadena
                self._sucesor.set_cantidad(resto) #Le paso el resto al siguiente manejador como cantidad
        else:
            self._sucesor.set_cantidad(cantidad)

class Meses(Cumpleanios): #---------------------------------------Mes
    def __init__(self):
        self._sucesor = None

    def set_sucesor(self, sucesor):
        self._sucesor = sucesor  #Aca definimos el siguiente manejador de la cadena

    def set_cantidad(self, cantidad):
        if cantidad >= 30:
            num = cantidad // 30  #Nos devuelve el cociente
            resto = cantidad % 30  #Nos devuelve el resto

            print("Faltan " + Fore.GREEN + f"{num} meses" + Fore.WHITE + " para el cumpleaños") #Printeo el cociente

            if resto != 0:  #Si el resto nos da diferente de cero, pasaría al siguiente manejador de la cadena
                self._sucesor.set_cantidad(resto)
        else:
            self._sucesor.set_cantidad(cantidad)

class Dias(Cumpleanios): #-------------------------------------------Dia
    def __init__(self):
        self._sucesor = None

    def set_sucesor(self, sucesor):
        self._sucesor = sucesor  #Aca definimos el siguiente manejador de la cadena

    def set_cantidad(self, cantidad):
        if cantidad >= 1:
            num = cantidad // 1  #Nos devuelve el cociente
            resto = cantidad % 1  # Nos devuelve el resto
            
            print("Faltan " + Fore.BLUE + f"{num} dias" + Fore.WHITE + " para el cumpleaños") # Printeo el cociente

            if resto != 0:  #Si el resto nos da diferente de cero, pasaría al siguiente manejador de la cadena
                self._sucesor.set_cantidad(resto)
        else:
            self._sucesor.set_cantidad(cantidad)

#----------------------------------------------------Orden de la cadena
class Cuenta_cadena:
    def __init__(self):
        self.cadena1 = Anios()
        self.cadena2 = Meses()
        self.cadena3 = Dias()

        self.cadena1.set_sucesor(self.cadena2)
        self.cadena2.set_sucesor(self.cadena3)

#-------------------------------------------------------El MAIN
if __name__ == "__main__":
    edad = Cuenta_cadena()
    cantidad = int(input("Ingresar la cantidad de dias: "))
   
    if cantidad == 0:
        print(Fore.MAGENTA + "F" + Fore.GREEN + "e" + Fore.YELLOW + "l" + Fore.RED +
              "i" + Fore.CYAN + "z" + Fore.BLUE + " C" + Fore.MAGENTA + "u" + Fore.GREEN + "m" + Fore.YELLOW + "p" + Fore.RED + "l" + Fore.CYAN + "e" + Fore.BLUE + "a" + Fore.MAGENTA + "ñ" + Fore.GREEN + "o" + Fore.RED + "s" + Fore.LIGHTBLUE_EX + "!" + Fore.LIGHTGREEN_EX + "!" + Fore.LIGHTMAGENTA_EX + "!")
        exit()
    else:
        edad.cadena1.set_cantidad(cantidad)
