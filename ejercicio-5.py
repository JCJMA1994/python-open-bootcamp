# Escribe una función que pueda decirte si un número (número entero) es primo o no.

numero = int(input("Ingresa un numero: "))

def numero_primo(numero):

    if numero > 1:
        contador = 0
        inicial = 2
        while inicial < numero and contador == 0:
            resto = numero % inicial
            if resto == 0:
                contador+=1
            inicial+=1
        if contador == 0:
            return f"El numero {numero} es PRIMO"
        else:
            return f"El numero {numero} no PRIMO"
    else:
        return f"El numero {numero} no PRIMO"


print(numero_primo(numero))
