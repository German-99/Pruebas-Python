contador=0
mi_email=input("Introduce tu direccion de email: ")

for i in mi_email:
    if(i=="@" or i=="."):
        contador=contador+1

if contador==2:
    print("Email es correcto")
else:
    print("Email no es correcto")