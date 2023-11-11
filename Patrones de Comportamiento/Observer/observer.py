class Publisher:                        #? SUJETO

    def __init__(self):
        self.subscribers = set()        # crea un conjunto vacio self.subscribers donde no hay elementos repetidos

    def register(self, who):
        self.subscribers.add(who)
   

    def unregister(self, who):
        self.subscribers.discard(who)

    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)

#!---------------------------------------------

class Revista(Publisher):                   #? SUJETO CONCRETO
    def __init__(self, *args):
        Publisher.__init__(self, *args)

    def publicar_una_revista(self):
        self.dispatch("se ha publicado una nueva revista")

#!---------------------------------------------

class Subscriber:                       #? OBSERVADOR               
    def __init__(self, name):   
        self.name = name

    def update(self, message):
        print('\n{} recibio el mensaje "{}"'.format(self.name, message))

#!---------------------------------------------

class MySubscriber(Subscriber):         #? OBSERVADOR CONCRETO
    def __init__(self, *args):
        Subscriber.__init__(self, *args,)

#!---------------------------------------------

if __name__ == "__main__":

    ole = Revista()

    rumbos = Revista()

    juan = MySubscriber("Juan")

    luis = MySubscriber("Luis")

    ole.register(juan)

    rumbos.register(luis)

    ole.publicar_una_revista()

    rumbos.publicar_una_revista()

