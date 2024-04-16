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
            id_winningPlayer = int(input("Digite la identificacion del jugador ganador: "))
            id_losingPlayer = int(input("Digite la identificacion del jugador perdedor: "))
            punt_ganador = int(input("Ingresa los puntos a favor del jugador ganador: "))
            punt_perdedor = int(input("Ingresa los puntos a favor del jugador perdedor: "))
            torneo.registrar_partido(id_winningPlayer, id_losingPlayer, punt_ganador, punt_perdedor)
        elif opc == "4":
            torneo.showStatistics()
        elif opc == "5":
            categoria = input("Elige la categoria que quieres ver el ganador: ")
            torneo.obtener_ganador_catego(categoria)
        elif opc == "6":
            print("Termino El Codigo")
            break
        else:
            print("El numero que ingresaste no existe. Ingresa un numero entre (1-6)")

if __name__ == "__main__":
    main()