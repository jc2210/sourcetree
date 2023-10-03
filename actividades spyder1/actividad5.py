dia_semana = input("Por favor, ingresa un día de la semana en minúsculas: ")

if dia_semana == "lunes":
    print("Es el primer día laboral de la semana.")
    
elif dia_semana == "viernes":
    print("Por fin es viernes")
    
elif dia_semana == "sabado" or dia_semana == "domingo":
    print("Es fin de semana")
    
else:
    print("No reconocemos ese día de la semana.")

