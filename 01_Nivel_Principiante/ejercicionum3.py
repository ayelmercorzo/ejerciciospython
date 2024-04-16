# 3. Teniendo en cuenta el punto 2 se requiere tener el registro de 20 estudiantes y poder determinar
# el estado de salud de la comunidad estudiantil. El programa debe mostrar el siguiente reporte:}

# a. Cuantos estudiantes se encuentran en el peso ideal.
# b. Cuantos estudiantes se encuentran en obesidad grado I
# c. Cuantos estudiantes se encuentran en obesidad grado II
# d. Cuantos estudiantes se encuentran en obesidad grado III
# e. Cuantos estudiantes se encuentran en Sobrepeso
import os
os.system('cls')

peso_ideal = 0
obesidad_grado_I = 0
obesidad_grado_II = 0
obesidad_grado_III = 0
sobrepeso = 0

estudiantes = int(input("Cuantos estudiantes desea ingresar: "))

for i in range(0,estudiantes,1):
    print ("Estudiante "+str(i+1)+ "")
    peso = float(input("Ingrese el peso en kg: "))
    altura = float(input("Ingrese la altura en m: "))

    IMC = peso/(altura**2)

    if IMC >= 25.0 and IMC <= 29.9:
        sobrepeso += 1
    elif IMC >= 18.5 and IMC <= 24.9:
        peso_ideal += 1
    elif IMC >= 30 and IMC <= 34.9:
        obesidad_grado_I += 1
    elif IMC >= 35 and IMC <= 39.9:
        obesidad_grado_II += 1
    elif IMC >= 40:
        obesidad_grado_III += 1

print("El total de estudiantes en el peso ideal es: ", peso_ideal)

print("El total de estudiantes en el peso sobrepeso es: ", sobrepeso)

print("El total de estudiantes en el peso obesidad 1 es: ", obesidad_grado_I)

print("El total de estudiantes en el peso obesidad 2 es: ", obesidad_grado_II)
    
print("El total de estudiantes en el peso obesidad 3 es: ", obesidad_grado_III)    