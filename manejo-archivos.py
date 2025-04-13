from io import open

archivo_texto=open("archivo.txt", "r+") #lectura y escritura la r+


#print(archivo_texto.readlines())

lista_texto=archivo_texto.readlines();

lista_texto[1]="Esta linea ha sido incluida desde el exterior \n"

archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close()

"""
archivo_texto.write("\n sienpre es bue dia para estudiar python")
archivo_texto.close()
"""

"""
frase="Estupendo dia para estudiar python \n en sabado"

archivo_texto.write(frase)

archivo_texto.close()
"""

"""
texto=archivo_texto.read()

archivo_texto.close()

print(texto)
"""
"""
lineas_texto=archivo_texto.readlines()

archivo_texto.close()

print(lineas_texto[0])
"""
