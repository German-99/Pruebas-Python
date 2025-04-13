print("Asignaturas optativas")
print("Asignatura optativas: Informatica grafica - pruebas de software - Usablilidad")
opcion=input("Escribe la asignatura escogida: ")
asignatura=opcion.lower()

if asignatura in("informatica grafica", "pruebas de software", "usabilidad"):

    print("Asignatura elegida " + asignatura)

else:
    print("La asignatura escogida no esta contemplada")
