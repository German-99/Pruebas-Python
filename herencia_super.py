class Persona():
    def __init__(self, nombre, edad, Lugar_residencia):
        self.nombre=nombre

        self.edad=edad

        self.lugar_residencia=Lugar_residencia

    def Descripcion(self):
        print(" Nombre: ", self.nombre, " Edad: ", self.edad, " Residencia: ", self.lugar_residencia )

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario=salario
        self.antiguedad=antiguedad

    def Descripcion(self):
        super().Descripcion()

        print(" Salario: ", self.salario, " Antiguedad ", self.antiguedad)


Manuel=Persona("Manuel", 55, "Colombia")

Manuel.Descripcion()   

print(isinstance(Manuel, Empleado))



    