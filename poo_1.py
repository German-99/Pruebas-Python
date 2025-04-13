class Coche():
    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmmarcha=False

    def arrancar(self,arrancamos):
        self.__enmmarcha=arrancamos

        if(self.__enmmarcha):
            chequeo=self.__chequeo_interno()

        if(self.__enmmarcha and chequeo):
            return "El coche esta en marcha"

        elif(self.__enmmarcha and chequeo==False):
            return "Algo salio mal, no podemos avanzar"
        
        else:
            return "El coche esta parado"

    def estado(self):
        print("El coche tiene " , self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, "y un largo de ", self.__largoChasis)

    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina="ok"
        self.acceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.acceite=="ok" and self.puertas=="cerradas"):
           
            return True
        
        else:

            return False 


miCoche=Coche()

print(miCoche.arrancar(True))

miCoche.estado()

print(miCoche.chequeo_interno())

print("-----------A continuacion creamos el segundo objeto------------")
miCoche2=Coche()

print(miCoche2.arrancar(False))

miCoche2.estado()