# El centro de salud de campuslands desea realizar un programa que le permita calcular el IMC de los
# Estudiantes nuevos.

# El programa debe mostrar el nombre del estudiante, la edad, el imc y la categoría según el IMC obtenido

import os
os.system('cls')
print("Nuestro centro de salud (Campuslands)le da la bienvenida a nuestro programa")
print("Queremos saber el indice de masa corporal de nuestros estudiantes nuevos")
print(" ")

nombre= input("Digite el nombre del estudiante: ")
edad= input("Edad del estudiante: ")
print(" ")
peso= float(input("ingrese el peso en kg: "))
altura = float(input("ingrese la altura en metros: "))

IMC = float(peso / (altura **2))

if IMC >= 18.5 and IMC <= 24.9:
    print(" ")
    print(f"el estudiante {nombre} con edad {edad} su imc es {IMC} y su peso es NORMAL")
elif IMC >= 25 and IMC <= 29.9:
    print(" ")
    print(f"el estudiante {nombre} con edad {edad} su imc es {IMC} y su peso es es SOBREPESO")
elif IMC >= 30 and IMC <= 34.9:
    print(" ")
    print(f"el estudiante {nombre} con edad {edad} su imc es {IMC} y su peso es OBESIDAD I")
elif IMC >= 30 and IMC <= 34.9:
    print(" ")
    print(f"el estudiante {nombre} con edad {edad} su imc es {IMC} y su peso es OBESIDAD II")
elif IMC > 40:
    print(" ")
    print(f"el estudiante {nombre} con edad {edad} su imc es {IMC} y su peso es OBESIDAD III")
