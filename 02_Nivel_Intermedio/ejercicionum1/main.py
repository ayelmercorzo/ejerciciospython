import os
from ciudades import registrar_ciudad, obtener_sismos_por_ciudad
from sismos import registrar_sismo
from informe import generar_informe_de_riesgo

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while True:
        opcion = input('Opción: ')
        if opcion in opciones:
            return opcion
        else:
            print('Opción incorrecta, vuelva a intentarlo.')

def registrar_ciudad_menu():
    nombre_ciudad = input("Ingrese el nombre de la ciudad: ")
    cantidad_sismos = int(input("Ingrese la cantidad de sismos a registrar para esta ciudad: "))
    print(registrar_ciudad(nombre_ciudad, cantidad_sismos))

def registrar_sismo_menu():
    ciudad = input("Ingrese el nombre de la ciudad para registrar el sismo: ")
    index = int(input("Ingrese el índice del sismo: ")) - 1
    magnitud = float(input("Ingrese la magnitud del sismo: "))
    print(registrar_sismo(ciudad, index, magnitud))

def buscar_sismos_por_ciudad_menu():
    ciudad = input("Ingrese el nombre de la ciudad para ver los sismos registrados: ")
    sismos = obtener_sismos_por_ciudad(ciudad)
    if sismos:
        print(f"Sismos registrados para la ciudad '{ciudad}':")
        for i, magnitud in enumerate(sismos):
            print(f"  Sismo {i + 1}: Magnitud {magnitud}")
    else:
        print(f"La ciudad '{ciudad}' no ha sido registrada.")

def informe_de_riesgo_menu():
    informe = generar_informe_de_riesgo()
    for info in informe:
        print(info)

def salir():
    print('Saliendo...')
    os.system('cls' if os.name == 'nt' else 'clear')
    exit()

def menu_principal():
    opciones = {
        '1': ('Registrar Ciudad', registrar_ciudad_menu),
        '2': ('Registrar Sismo', registrar_sismo_menu),
        '3': ('Buscar Sismos por ciudad', buscar_sismos_por_ciudad_menu),
        '4': ('Informe de riesgo', informe_de_riesgo_menu),
        '5': ('Salir', salir),
    }

    while True:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        opciones[opcion][1]()
        input("Presione Enter para continuar...")

if __name__ == '__main__':
    menu_principal()
