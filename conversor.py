def conversor(tipo_moneda, valor_dolar):
    moneda_origen = input("¿Cuántos " + tipo_moneda +  " tienes?: ")
    moneda_origen = float(moneda_origen)
    dolares = moneda_origen / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

menu = """"
Bienvenido al conversor de monedas 💰 - by FT!!!

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos
4 - Soles
5 - Euros
6 - Bolivares

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("Pesos colombianos", 3875)
elif opcion == 2:
    conversor("Pesos argentinos", 65)
elif opcion == 3:
    conversor("Pesos mexicanos", 24)
elif opcion == 4:
    conversor("Soles", 3.85)
elif opcion == 5:
    conversor("Euros", 1.21)
elif opcion == 6:
    conversor("Bolivares", 250000)
else:
    print("Ingresa una opción correcta por favor")
