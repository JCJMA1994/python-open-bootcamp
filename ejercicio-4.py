#Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y
# otra función que calcule el área de un círculo recibiendo el radio del mismo.

altura = float(input("Ingrese la altura para el triangulo: "))
base = float(input("Ingrese la base para el triangulo: "))

radio =  float(input("Ingrese el radio para el circulo: "))

def area_triangulo(altura, base):
    return (base * altura)/ 2

def area_circulo(radio):
    return 3.14 * radio**2

print(f"Area Triangulo: {area_triangulo(altura, base)}")
print(f"Area Circulo: {area_circulo(radio)}")