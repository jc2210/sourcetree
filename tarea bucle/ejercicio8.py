frase = input("Escribe una frase:")
letra = input("Introduzca una letra:")
conteo = 0

for caracter in frase:
    if caracter == letra:
        conteo += 1

print(f"La letra '{letra}' aparece '{conteo}' veces en la frase.")
