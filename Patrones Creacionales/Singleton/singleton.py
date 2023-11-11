class Singleton:

    def __init__(self):

        self.__singleton = None

    def getSingleton(self):

        if self.__singleton == None:
            self.__singleton = Singleton()

        return self.__singleton

    def saySomething(self):
        print('Hola, soy el unico Singleton')

if __name__ == '__main__':

    singleton = Singleton().getSingleton()

    singleton.saySomething()