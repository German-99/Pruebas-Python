print("Verificacion de acceso")
nota_ususariu=int(input("Introduce tu nota: "))
if nota_ususariu<5:
    print("Insuficiente")

elif nota_ususariu<6:
    print("Suficiente")

elif nota_ususariu<7:
    print("Bien")

elif nota_ususariu<9:
    print("Notable")

else:
    print("Sobresaliente")

print("Programa Finalizado")