print("Seleccion de ejercicios")
print("1. Crea un programa que pida números infinitamente. Los números introducidos deben ser cada vez mayores El programa finalizará cuando se introduce un número menor que el anterior. ")
print("2. Crea un programa que pida números positivos indefinidamente. El programa termina  cuando se introduce un número negativo. Finalmente el programa muestras la suma de todos los números introducidos ”. ")
selseccion_ejercicio=int(input("Itroduce numero de ejrcicio: "))
if selseccion_ejercicio == 1:
    num1=int(input("Introduce un numero: "))
    num2=int(input("Introduce un numero mayor que " + str(num1) + ": "))
    while num1 < num2:
        num1 = num2
        num2 = int(input("Escriba un numero mayor que " + str(num1) + ": "))
    print()
    print( num2, "no es mayor que", num1)
    
elif selseccion_ejercicio==2:
    numero = int(input("Introduce un numero: "))
    suma = 0
   
    while numero > 0:
        suma=suma+numero
        numero = int(input("Introduce otro numero: "))
    
    print("La suma de los numeroes es: " + str(suma))
    
    
else:
    print("No existe esta opcion")