ciudades = []

def registrar_ciudad(nombre_ciudad, cantidad_sismos):
    ciudades[nombre_ciudad] = [0] * cantidad_sismos
    return f"Se ha registrado la ciudad '{nombre_ciudad}' con {cantidad_sismos} sismos a registrar."

def obtener_sismos_por_ciudad(nombre_ciudad):
    if nombre_ciudad in ciudades:
        return ciudades[nombre_ciudad]
    else:
        return None
