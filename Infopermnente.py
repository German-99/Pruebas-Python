import pickle

class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("se ha creado una persona nueva con el nombre de ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)
    
class ListaPersonas:

    personas=[]

    def __init__(self):

        ListaDePersonas=open("ficheroExterno", "ab+")
        ListaDePersonas.seek(0)

        try:
            self.personas=pickle.load(ListaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))

        except:
            print("El fichero esta vacio")

        finally:
            ListaDePersonas.close()
            del(ListaDePersonas)

    def agregarPersonas(self,  p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def  guardarPersonasEnFicheroExterno(self):
        ListaPersonas=open("ficheroExterno","wb")
        pickle.dump(self.personas, ListaPersonas)
        ListaPersonas.close()
        del(ListaPersonas)

    def mostrarInfoficheroexterno(self):
        print("La informacion del fichero externo es la siguiente:")
        for p in self.personas:
            print(p)

milista=ListaPersonas()
persona=Persona("Ana", "Femenino", 20)
milista.agregarPersonas(persona)
milista.mostrarInfoficheroexterno()
