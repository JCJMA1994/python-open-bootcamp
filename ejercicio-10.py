import time

hora = time.strftime('%H')
minutos = time.strftime('%M')

if int(hora) >= 19:
    print("Hora de IRSE A CASA")
else:
    print(f"Quedan {18 - int(hora)} horas y {59 - int(minutos)} minutos")