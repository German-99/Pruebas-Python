from rich.console import Console
from rich.table import Table

console = Console()

import random
nombres = []

while True:
    print("Menu")
    print("1. Agregar personas")
    print("2. Mostrar lista")
    print("3. Eliminar persona")
    print("4. Sacar nombre")
    print("5. Salir")

    for i in range(1, 6):
     for j in range(1, 6):
      print(i * j) 
    
    try:
       numero = int(input("ingrese numero: "))
    except ValueError:
       print("Error: Ingrese un número válido.")
       continue 

    if numero == 1:
     nombre = input("Ingresa un nombre: ")
     nombres.append(nombre)

    elif numero == 2:
        table = Table()
        table.add_column("Nombres", style="magenta")
        for nombre in nombres:
         table.add_row(nombre)
        console.print(table)


    elif numero == 3:
        if len(nombres) == 0:
            print("No hay ningun nombre en la lista")
            continue
        
        nombre_eliminar = input("Nombre a eliminar: ").strip()
        if nombre_eliminar.lower() in [nombre.lower() for nombre in nombres]:
           for nombre in nombres:
                if nombre.lower() == nombre_eliminar.lower():
                    nombres.remove(nombre)
                    print(f"{nombre} ha sido eliminado.")
        else:
            print("Error: Ese nombre no está en la lista.")

    elif numero == 4:
        if len(nombres) < 2:
            print("No hay suficientes nombres en la lista para sacar un nombre.")
            continue
        
        while True:
         persona_seleccion = input("\nEscribe el nombre de la persona que sacará otro nombre: ").strip()
         # Validar si el nombre existe en la lista original (sin importar mayúsculas)
         if persona_seleccion.lower() in [nombre.lower() for nombre in nombres]:
            break  # Si el nombre es válido, salir del bucle
         else:
            print("Error: Ese nombre no está en la lista. Inténtalo de nuevo.")

            # Filtrar nombres sin convertirlos a minúsculas
        nombres_filtrados = [nombre for nombre in nombres if nombre.lower() != persona_seleccion.lower()]

         # Elegir un nombre aleatorio si quedan opciones
        if nombres_filtrados:
            nombre_aleatorio = random.choice(nombres_filtrados)
            print(f" {persona_seleccion} sacó a: {nombre_aleatorio}")

        else:
          print(" No hay más nombres disponibles para elegir.")

    elif numero == 5:
        print(" Gracias por usar el modulo.")
        break
        
    else:
        print("Opción no válida. Inténtelo de nuevo.")
        


    
    
    
"""table = Table(title="Lista de Personas")
table.add_column("Nombre", style="magenta")
for nombre in nombres:
    table.add_row(nombre)
console.print(table)

while True:
    persona_seleccion = input("\nEscribe el nombre de la persona que sacará otro nombre: ").strip()

    # Validar si el nombre existe en la lista original (sin importar mayúsculas)
    if persona_seleccion.lower() in [nombre.lower() for nombre in nombres]:
        break  # Si el nombre es válido, salir del bucle
    else:
        print("Error: Ese nombre no está en la lista. Inténtalo de nuevo.")

# Filtrar nombres sin convertirlos a minúsculas
nombres_filtrados = [nombre for nombre in nombres if nombre.lower() != persona_seleccion.lower()]


# Elegir un nombre aleatorio si quedan opciones
if nombres_filtrados:
    nombre_aleatorio = random.choice(nombres_filtrados)
    print(f" {persona_seleccion} sacó a: {nombre_aleatorio}")
else:
    print(" No hay más nombres disponibles para elegir.")"""

""""
butterflies = 10
beetles = 12
ladybugs = 20

print('I caught ' + str(butterflies) + ' 🦋 butterflies!')
print('I caught ' + str(beetles) + ' 🪲 beetles!')
print('I caught ' + str(ladybugs) + ' 🐞 ladybugs!')

total = butterflies + beetles + ladybugs

print('I caught ' + str(total) + ' total bugs!')"""