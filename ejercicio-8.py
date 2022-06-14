# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga
# como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos,
# imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return f"ALUMNO \nNombre: {self.nombre} \nNota: {self.nota}"


    def is_aprobado(self, nota):
        if self.nota >= 10.5:
            return "Condicion: APROBADO"
        else:
            return "Condicion: DESAPROBADO"


nombre = "Jose Carlos Joao"
nota = 15

alumno =Alumno(nombre, nota)

print(alumno)
print(alumno.is_aprobado(nota))