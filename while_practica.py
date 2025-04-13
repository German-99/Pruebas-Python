import math

print("Programa de raiz cuadrada")
numero=int(input("Introduce un numero por favor: "))

intentos=0

while numero<0:
    print("No se puede hallar la raiz cuadrada de un numero negativo")

    if intentos==2:
        print("Has consumido demaciados intentos. programa finalizado")
        break

    numero=int(input("Introduce un numero por favor: "))
    if numero<0:
        intentos=intentos+1

if intentos<2:
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es "  + str(solucion))



"""
edad=int(input("Introduce la edad: "))

while edad<5 or edad>100:
    print("Has introducido una edad incorrecta. vuelve a interntarlo")
    edad=int(input("Introduce la edad: "))

print("Gracias por colaborar")
print("La edad del aspitrante es: " + str(edad))

"""