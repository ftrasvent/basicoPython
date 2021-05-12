soles = input("¿Cuántos soles peruanos tienes?: ")
soles = float(soles)
valor_dolar = 3.85
dolares = soles / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")