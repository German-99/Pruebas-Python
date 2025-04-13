print("Programa de becas")
distnacia_escuela=int(input("Introduce la distancia de la escuela en KM: "))
print(distnacia_escuela)

numero_hermanos=int(input("introduce el numero de hermanos: "))
print(numero_hermanos)

salario_familiar=int(input("Introduce salario familiar: "))
print(salario_familiar)

if distnacia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
    print("tienes derecho a beca")

else:
    print("No tienes derecho a beca")
