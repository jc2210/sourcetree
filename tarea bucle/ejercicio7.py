contraseña="contraseña"
intentos = 5

while intentos > 0:
    entrada = input("Introduce la contraseña: ")
    if entrada == contraseña:
        print("Contraseña correcta.")
        break
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")
        intentos -= 1