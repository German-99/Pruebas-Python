import random

"""answer = input("Are we there yet? ")

while answer.lower() != "yes":
  answer = input("Are we there yet? ")"""

"""answer = input("Are we there yet? ")

while answer:

  if answer.lower() == "Yes":
    break
  else:
    answer = input("Are we there yet? ")"""

"""for i in range(10, 0, -1):
  print (i)
print("Happy New Year! ")"""


while True:
  numero = int(input("What is the total (2-12)?"))
  numero_aleatorio_1 = random.randint(1, 6)  
  numero_aleatorio_2 = random.randint(1, 6) 
  numero_final = numero_aleatorio_1 + numero_aleatorio_2
  print(f"Numero final es {numero_final}")
  if numero == numero_final:
    print("You got it!")
    print (f"El numero del dado es {numero_final}")
    print (f"El numero elegido es {numero}")
    break

"""# Generate the number for each dice roll before the loop
numero_aleatorio_1 = random.randint(1, 6)
numero_aleatorio_2 = random.randint(1, 6)
numero_final = numero_aleatorio_1 + numero_aleatorio_2

numero = int(input("What is the total (2-12)? "))

# Keep the while loop to persist until the user guesses correctly
while numero != numero_final:
    numero = int(input("What is the total (2-12)? "))

print("You got it!")
print (f"El numero del dado es {numero_final}")
print (f"El numero elegido es {numero}")"""