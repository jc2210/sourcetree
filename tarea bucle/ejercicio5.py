cantidad_invertir= float(input("Escribe la cantidad que quieres invertir:"))
interes_anual= float(input("Introduce el interes anual (%):"))
numero_años= int(input("Introduce numero de años:"))

for i in range(1,numero_años +1):
    cantidad_invertir *= (1 + (interes_anual / 100))
    print(f"Año {i}: {cantidad_invertir: .2f}")