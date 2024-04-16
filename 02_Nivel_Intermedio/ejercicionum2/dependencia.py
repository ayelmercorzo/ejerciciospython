from dispositivo import Dispositivo

class Dependencia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.dispositivos = []

    def registrar_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)

    def calcular_consumo_kwh(self):
        consumo_total_kwh = 0
        for dispositivo in self.dispositivos:
            consumo_total_kwh += dispositivo.potencia_w / 1000
        return consumo_total_kwh
