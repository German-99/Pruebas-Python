Valido=False

email=input("Introduce tun email: ")

for i in range(len(email)):
    if email[i]=="@":
        Valido=True

if Valido:
    print("Email corrcto")

else:
    print("Email incorrecto")