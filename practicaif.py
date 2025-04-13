print("Programa de evaluacion de notas")

nota_alumno=input("Introduce la nota del alumno: ")

def evaluacion(nota):
    Valoracion="aprobado"
    if nota<5:
        Valoracion="Reprobado"
    return Valoracion

print(evaluacion(int(nota_alumno)))