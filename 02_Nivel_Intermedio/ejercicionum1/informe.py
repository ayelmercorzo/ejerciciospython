def generar_informe_de_riesgo():
    informe = []
    for ciudad, sismos in ciudad.items():
        if len(sismos) > 0:
            promedio = sum(sismos) / len(sismos)
            if promedio < 2.5:
                riesgo = "Amarillo (Sin riesgo)"
            elif 2.5 <= promedio <= 4.5:
                riesgo = "Naranja (Riesgo medio)"
            else:
                riesgo = "Rojo (Riesgo alto)"
            informe.append(f"Ciudad: {ciudad} - Promedio de sismos: {promedio:.2f} - Riesgo: {riesgo}")
        else:
            informe.append(f"Ciudad: {ciudad} - Sin sismos registrados.")
    return informe
