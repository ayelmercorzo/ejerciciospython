def registrar_sismo(ciudad, index, magnitud):
    if ciudad in ciudades:
        ciudades = [ciudad][index] = magnitud
        return f"Sismo {index + 1} registrado para la ciudad '{ciudad}' con magnitud {magnitud}."
    else:
        return f"La ciudad '{ciudad}' no ha sido registrada."
