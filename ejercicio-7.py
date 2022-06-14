# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
# - Color
# - Ruedas
# - Puertas
# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
# - Velocidad
# - Cilindrada
# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

class Vehiculo:

    def __init__(self, color, rueda, puerta):
        self.color = color
        self.rueda = rueda
        self.puerta = puerta

    def __str__(self):
        return f"""
        Vehiculo
        Color: {self.color}
        # Rueda: {self.rueda}
        #Puerta: {self.puerta}"""


class Coche(Vehiculo):

    def __init__(self, color, rueda, puerta, velocidad, cilindrada):
        Vehiculo.__init__(self, color, rueda, puerta)
        self.color = color
        self.rueda = rueda
        self.puerta = puerta
        self.velocidad = velocidad
        self.cilindrada = cilindrada


    def __str__(self):
        return f"""
        Coche
        Color: {self.color}
        # Rueda: {self.rueda}
        #Puerta: {self.puerta}
        Velocidad: {self.velocidad}
        Cilindrada: {self.cilindrada}"""


coche = Coche("Rojo", 4, 4, "120 km/h", 100)
print(coche)