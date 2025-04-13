salario_presidente=int(input("Introduce el salrio de presidente: "))
print("salario presidente: " + str(salario_presidente))

salario_director=int(input("Introduce el salrio de director: "))
print("salario director: " + str(salario_director))

salario_jefe=int(input("Introduce el salrio de jefe de area "))
print("salario jefe de area: " + str(salario_jefe))

salario_admin=int(input("Introduce el salrio de administrativo: "))
print("salario administrativo: " + str(salario_admin))

if salario_admin<salario_jefe<salario_director<salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo falla en la empresa")