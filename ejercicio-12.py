#En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo,
# haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.
import pickle
from pickle import *

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

vehiculo = Vehiculo("Negro", 4, 4)
print(vehiculo)

file = open('vehiculos.json', 'wb')

pickle.dump(vehiculo, file, protocol=pickle.HIGHEST_PROTOCOL)
file.close()

file = open('vehiculos.json', 'rb')
load_vehiculo = pickle.load(file)
print(load_vehiculo)
