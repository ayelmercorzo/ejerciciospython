from dependencia import Dependencia
from dispositivo import Dispositivo
from emisiones import calcular_emisiones_co2
import os

dependencias = []

factor_emision_colombia = 126 / 1000 

def registrar_dependencia():
    nombre = input("Digite el nombre de la dependencia a registrar: ")
    dependencias.append(Dependencia(nombre))
    print("La dependencia se registró con éxito.")

def registrar_consumo():
    nombre = input("En que dependencia quiere registrar consumo: ")
    for dependencia in dependencias:
        if dependencia.nombre == nombre:
            nombre_dispositivo = input("Escriba el nombre del dispositivo: ")
            potencia_w = float(input("Gasto en potencia del dispositivo en Watts: "))
            dependencia.registrar_dispositivo(Dispositivo(nombre_dispositivo, potencia_w))
            print("El consumo fue registrado con éxito.")
            
            return
            
    print("La dependencia no fue encontrada.")

def mostrar_informacion_dependencia(dependencia):
    consumo_kwh = dependencia.calcular_consumo_kwh()
    print(f"Dependencia: {dependencia.nombre}")
    print(f"Consumo de electricidad (kWh): {consumo_kwh:.2f}")
    emisiones_co2 = calcular_emisiones_co2(consumo_kwh, factor_emision_colombia)
    print(f"Emisiones de CO2 (tCO2eq): {emisiones_co2:.2f}")

def dependencia_mayor_co2():
    if not dependencias:
        print("No hay dependencias registradas.")
        return
    os.system('cls')
    print("LA DEPENDENCIA QUE PRODUCE MAYOR CO2 ES: ")
    mayor_emisiones = max(dependencias, key=lambda d: d.calcular_consumo_kwh())
    mostrar_informacion_dependencia(mayor_emisiones)

def main():
    os.system("cls")
    opciones = {
        "1": registrar_dependencia,
        "2": registrar_consumo,
        "3": lambda: [mostrar_informacion_dependencia(dependencia) for dependencia in dependencias],
        "4": dependencia_mayor_co2
    }
    os.system("cls")
    while True:
        print("\n---Menú principal---")
        print("1. Registrar una dependencia")
        print("2. Registrar consumo por dependencia")
        print("3. Ver CO2 producido por dependencia")
        print("4. Dependencia que produce mayor CO2")
        print("5. Salir")

        opcion = input("Digita la opcion a realizar:__  ")

        if opcion == "5":
            print("Vuelva pronto")
            break
        
        accion = opciones.get(opcion)
        if accion:
            accion()
        else:
            print("La opción que escogiste no es válida. ingresa una opción valida.")

if __name__ == "__main__":
    main()
