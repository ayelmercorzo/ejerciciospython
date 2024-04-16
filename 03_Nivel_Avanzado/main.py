from torneoTenis import torneoTenis, Jugador, regis_jugador_manualmente
def main():
    torneo = torneoTenis()
    while True:
        
        
        print("\n\t\t\t  Menú ")
        print("\t __________________________________________")
        print("\t | 1. Registrar un jugador                |")
        print("\t | 2. Iniciar el torneo                   |")
        print("\t | 3. Registrar resultado de un partido   |")
        print("\t | 4. Mostrar las estadísticas            |")
        print("\t | 5. Obtener el ganador de una categoría |")
        print("\t | 6. Salir                               |")
        print("\t |________________________________________|")
        print(" ")
        opc = input("elige una opcion dentro de (1-6): ")

        continuar = input("¿Desea registrar un jugador? (s/n): ")

        if opc == "1":
            regis_jugador_manualmente(torneo)
        elif opc == "2":
            torneo.inicioDeTorneo()
        elif opc == "3":
            id_winningPlayer = int(input("Escribe el ID del jugador ganador: "))
            id_losingPlayer = int(input("Escribe el ID del jugador perdedor: "))
            punt_ganador = int(input("Caules fueron los punt del jugador ganador: "))
            punt_perdedor = int(input("Cuales fueron los punt del jugador perdedor: "))
            torneo.registrar_partido(id_winningPlayer, id_losingPlayer, punt_ganador, punt_perdedor)
        elif opc == "4":
            torneo.showStatistics()
        elif opc == "5":
            categoria = input("¿Escoge la categoría en la que quieres conocer al ganador?: ")
            torneo.obtener_ganador_catego(categoria)
        elif opc == "6":
            print("¡Haz finalizado, hasta luego!")
            break
        else:
            print("La pción que ingresaste no es válida. Coloca una opción del 1 al 6 de lo contrario sera erroneo.")

if __name__ == "__main__":
    main()