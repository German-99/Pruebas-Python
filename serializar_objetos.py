import pickle

class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):

        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena)

coche1=Vehiculos("KIA", "K3")

coche2=Vehiculos("Ford", "Raptor")

coche3=Vehiculos("Honda", "Civic")

coches=[coche1, coche2, coche3]

fichero=open("loscoches", "wb")

pickle.dump(coches, fichero)

fichero.close()

del (fichero)
