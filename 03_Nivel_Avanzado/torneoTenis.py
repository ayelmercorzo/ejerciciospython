class Jugador:
    def __init__(self, jugadorIdentificacion, nombre, edad, categoria):

        self.jugadorIdentificacion = jugadorIdentificacion
        self.categoria = categoria
        self.nombre = nombre
        self.edad = edad
        self.plusPoints = 0
        self.gamesplayed = 0
        self.wonPlayes = 0
        self.lostGames = 0        

class torneoTenis:
    def __init__(self):
        self.categoria = {'Novato': [], 'Intermedio': [], 'Avanzado': []}

    def registroDeJugador(self, jugadorIdentificacion, nombre, edad, categoria):
        jugador = Jugador(jugadorIdentificacion, nombre, edad, categoria)
        if categoria in self.categoria.keys():
            if (categoria == 'Novato' and 15 <= edad <= 16) or \
               (categoria == 'Intermedio' and 17 <= edad <= 20) or \
               (categoria == 'Avanzado' and edad > 20):
                self.categoria[categoria].append(jugador)
                print(f"{nombre} se registro correctamente en la categoria: {categoria}")
            else:
                print(f"{nombre} Es muy joven o viejo para ser novato, intermedio o avanzado")
        else:
            print("No se encuentra la categoria")

    def inicioDeTorneo(self):
        for categoria, jugadores in self.categoria.items():
            if len(jugadores) < 5:
                print(f"Faltan jugadores en la categoria: {categoria} para comenzar")
            else:
                print(f"Comenzo el torneo de la categoria: {categoria}")

    def registrar_partido(self, id_winningPlayer, id_losingPlayer, punt_ganador, punt_perdedor):
        winningPlayer = None
        losingPlayer = None

        for categoria, jugadores in self.categoria.items():
            for jugador in jugadores:
                if jugador.jugadorIdentificacion == id_winningPlayer:
                    winningPlayer = jugador
                elif jugador.jugadorIdentificacion == id_losingPlayer:
                    losingPlayer = jugador

        if winningPlayer is not None and losingPlayer is not None:
            winningPlayer.gamesplayed += 1
            losingPlayer.gamesplayed += 1
            winningPlayer.wonPlayes += 1
            losingPlayer.lostGames += 1
            winningPlayer.plusPoints += punt_ganador - punt_perdedor
            print("El juego fue registrado correctamente")
        else:
            print("No hay ningun registro de ese jugador")

    def showStatistics(self):
        for categoria, jugadores in self.categoria.items():
            print(f"categoria: {categoria} ")
            print("| ID | Jugador | Partidos Jugados | Partidos Ganados | Partidos Perdidos | punt a Favor |")
            for jugador in jugadores:
                print(f"""|{jugador.jugadorIdentificacion}| |{jugador.nombre}| |{jugador.gamesplayed}| |{jugador.wonPlayes}| |{jugador.lostGames}| |{jugador.plusPoints}|""")

    def obtencionDeGanadorCtg(self, categoria):
        if categoria in self.categoria.keys():
            jugadores_categoria = self.categoria[categoria]
            if jugadores_categoria:
                ganador = max(jugadores_categoria, key=lambda jugador: jugador.plusPoints)
                print(f"Hay un ganador en esta categoria: {categoria} es {ganador.nombre} con {ganador.plusPoints} puntos a favor!")
            else:
                print(f"No hay jugadores en esta categoria: {categoria}.")
        else:
            print("La categoria no existe")

def regis_jugador_manualmente(torneo):
    jugadorIdentificacion = int(input("A seguir la opcion, ingresa la identificacion del jugador: "))
    nombre = input("Cual es el nombrebre del jugador: ")
    edad = int(input("Escriba los edad que tiene: "))
    categoria = input("Escribe como esta en las opciones: (Novato/Intermedio/Avanzado) ")
    torneo.registroDeJugador(jugadorIdentificacion, nombre, edad, categoria)