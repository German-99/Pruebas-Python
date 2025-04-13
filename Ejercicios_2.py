print("Seleccion de ejercicios")
print("1. Crea un programa que muestre los números impares del 1 al 100. Los números deberán aparecer una al lado del otro sin salto de línea.")
print("2. Crea un programa que pida por teclado introducir una contraseña. La contraseña no podrá tener menos de 8 caracteres ni espacios en blanco. Si la contraseña es correcta, el programa imprime “Contraseña OK”. En caso contrario imprime “Contraseña errónea”. ")
print("3. Crea un programa que evalúe si una dirección de correo electrónico es válida o no en función de si tiene “@” o “.” Hay que tener en cuenta que la dirección se considera correcta si solo tiene una “@” y si tiene uno o más “.”  ")
selseccion_ejercicio=int(input("Itroduce numero de ejrcicio: "))
if selseccion_ejercicio == 1:
    for i in range(1,100,1):
        print(i, end=" ")
    
elif selseccion_ejercicio==2:
    contra=input("Introduce contraseña: ")

    contador=0

    for i in range(len(contra)):
        if contra[i]==" ":
            contador=1
    if len(contra)<8 or contador>0:
        print("contraseña incorrecta")
    else:
        print("Contraseña correcta")


elif selseccion_ejercicio==3:
    correo=input("Introduce correo: ")
    contadorArroba=0
    contadorpunto=0
    for i in range(len(correo)):
        if correo[i]=="@":
            contadorArroba=contadorArroba+1
        if correo[i]==".":
            contadorpunto=1
    if contadorpunto==0 or contadorArroba!=1:
        print("Email incorrecto")
    else:
        print("Email correcto")
else:
    print("No existe esta opcion")