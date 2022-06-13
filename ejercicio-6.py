# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

anio = int(input("Ingrese un anio: "))

def anio_bisiesto(anio):
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 ==0):
        return f"Anio: {anio} ES BISIESTO"
    else:
        return f"Anio: {anio} NO ES BISIESTO"


print(anio_bisiesto(anio))