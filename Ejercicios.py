print("Seleccion de ejercicios")
print("1. Crea un programa que pida dos números por teclado. El programa tendrá una función llamada “DevuelveMax” encargada de devolver el número más alto de los dos introducidos.")
print("2. Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos deberán ser almacenados en una lista y mostrar en consola el mensaje: “Los datos personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por teclado). ")
print("3. Crea un programa que pida tres números por teclado. El programa imprime en consola la media aritmética de los números introducidos.")
selseccion_ejercicio=int(input("Itroduce numero de ejrcicio: "))
if selseccion_ejercicio == 1:
    num1=int(input("Introduce primer numero: "))
    num2=int(input("Introduce segundo numero: "))

    def Devuelvemax(n1, n2):
        if n1<n2:
            print(n2)
        elif n2<n1:
            print(n1)
        else:
            print("Son iguales")
        
    print("El numero más grande es: ")
    Devuelvemax(num1, num2)
    
elif selseccion_ejercicio==2:
    Nombre=(input("Introduce nombre: "))
    Direccion=(input("Introduce direccion: "))
    Telefono=int(input("Introduce telefono: "))
    milista=[Nombre, Direccion, Telefono]

    print("Mis datos personales son: "+milista[0]+" "+milista[1]+" "+str(milista[2]))

elif selseccion_ejercicio==3:
    numarri1=int(input("Introduce el primer numero: "))
    numarit2=int(input("Introduce el primer numero: "))
    numarit3=int(input("Introduce el primer numero: "))
    media=(numarri1+numarit2+numarit3)/3
    print("La media es: ")
    print(media)
else:
    print("No existe esta opcion")



