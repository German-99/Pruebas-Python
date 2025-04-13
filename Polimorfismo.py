class coche():
    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")

class moto():
    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")

class camion():
    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")


def desplazaminetoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=camion()

desplazaminetoVehiculo(miVehiculo)