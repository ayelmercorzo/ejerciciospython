ciudades = {}

def registroCiudad():
    nameCity = input('Digite el nombre de la ciudad: ')
    while True:
        try:
            cantidadSismos = int(input('Digite la cantidad de sismos a registrar para esta ciudad: '))
            if cantidadSismos > 0:
                ciudades[nameCity] = [0] * cantidadSismos
                print(f'Se ha registrado la ciudad \'{nameCity}\' con {cantidadSismos} sismos a registrar.')
                break
            print('La cantidad de sismos debe ser mayor que cero.')
        except ValueError:
            print('Digite un número válido para la cantidad de sismos.')

def registroSismo():
    ciudad = input('Digite el nombre de la ciudad para registrar el sismo: ')
    if ciudad in ciudades:
        sismos = ciudades[ciudad]
        for i, sismo in enumerate(sismos):
            while True:
                try:
                    magnitud = float(input(f'Digite la magnitud del sismo {i + 1}: '))
                    sismos[i] = magnitud
                    print(f'Sismo {i + 1} registrado para la ciudad \'{ciudad}\' con magnitud {magnitud}.')
                    break
                except ValueError:
                    print('Digite un número válido para la magnitud del sismo.')
    else:
        print(f'La ciudad \'{ciudad}\' no ha sido registrada.')

def searchSismo():
    ciudad = input('Digite el nombre de la ciudad para ver los sismos registrados: ')
    if ciudad in ciudades:
        sismos = ciudades[ciudad]
        print(f'Sismos registrados para la ciudad \'{ciudad}\':')
        for i, magnitud in enumerate(sismos):
            print(f'  Sismo {i + 1}: Magnitud {magnitud}')
    else:
        print(f'La ciudad \'{ciudad}\' no ha sido registrada.')

def informe_de_peligro():
    for ciudad, sismos in ciudades.items():
        if sismos:
            prom = sum(sismos) / len(sismos)
            peligro = 'Amarillo (Sin peligro)' if prom < 2.5 else ('Naranja (peligro medio)' if 2.5 <= prom <= 4.5 else 'Rojo (peligro alto)')
            print(f'Ciudad: {ciudad} - prom de sismos: {prom:.2f} - peligro: {peligro}')
        else:
            print(f'Ciudad: {ciudad} - Sin sismos registrados.')
