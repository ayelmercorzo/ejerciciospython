from ciudades import (
    registroCiudad,
    registroSismo,
    searchSismo,
    informe_de_peligro
)

def mostrar_menu(opciones):
    print('Ingrese una opción:')
    for tecla, valoracion in opciones.items():
        print(f' {tecla}) {valoracion[0]}')

def leer_opcion(opciones):
    while True:
        opcion = input('Seleccione:  ')
        if opcion in opciones:
            return opcion
        print('No existe la opcion, Ingrese nuevamente.')

def salir():
    print('Teminamos...')
    exit()

def menu_principal():
    opciones = {
        '1': ('Registrar Sismo', registroSismo),
        '2': ('Registrar Ciudad', registroCiudad),
        '3': ('Informe de riesgo', informe_de_peligro),
        '4': ('Buscar Sismos por ciudad', searchSismo),
        '5': ('Salir', salir),
    }

    while True:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        opciones[opcion][1]()
        input('Enter para continuar...')

if __name__ == '__main__':
    menu_principal()
