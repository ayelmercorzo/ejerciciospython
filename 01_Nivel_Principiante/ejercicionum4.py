# Se desea realizar un programa en Python que permita ingresar n números enteros positivos y cuando se
# Ingrese un numero negativo debe mostrar en pantalla el siguiente reporte.

# a. Total de números ingresados
# b. Total de números pares ingresados
# c. Promedio de los números pares
# d. Promedio de los números impares
# e. Cuantos números son menores que 10
# f. Cuantos números están entre 20 y 50
# g. Cuantos números son mayores que 100
import os
Total_de_números_ingresados = int(input("¿Cuántos números quieres ingresar?: "))

# Variables para contar y calcular estadísticas
numeros_par = 0
totalDePares = 0
numeros_impar = 0
totalDeImpares = 0
numerosMayorA10 = 0
numerosEntre20_50 = 0
numerosMayorA100 = 0


for i in range(Total_de_números_ingresados):
    numero = int(input("Digite un número: "))
    
    if numero < 10:
        numerosMayorA10 += 1
    if 20 <= numero <= 50:
        numerosEntre20_50 += 1
    if numero > 100:
        numerosMayorA100 += 1
    if numero % 2 == 0:
        numeros_par += 1
        totalDePares += numero
    else:
        numeros_impar += 1
        totalDeImpares += numero

if numeros_par > 0:
    Promedio_de_los_números_pares = totalDePares / numeros_par
if numeros_impar > 0:
    Promedio_de_los_números_impares = totalDeImpares / numeros_impar

os.system('cls')

print(f"Total de números ingresados: {Total_de_números_ingresados}")
print(f"Total de números pares ingresados: {numeros_par}")
print(f"Promedio de los números pares: {Promedio_de_los_números_pares}")
print(f"Promedio de los números impares: {Promedio_de_los_números_impares}")
print(f"Cuantos números son menores que 10: {numerosMayorA10}")
print(f"Cuantos números están entre 20 y 50: {numerosEntre20_50}")
print(f"Cuantos números son mayores que 100: {numerosMayorA100}")


