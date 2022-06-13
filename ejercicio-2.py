#Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
numero_inicial = int(input("Escriba el numero inicial: "))
numero_final = int(input("Escriba el numero final: "))

while numero_final <= numero_inicial:
    numero_final = int(input("Escriba el numero final: "))


for numero_inicial in range(numero_inicial, numero_final +1):
    if numero_inicial % 2 != 0:
        print(f"Numero Impar: {numero_inicial} ")
