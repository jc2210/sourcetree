edad = int(input("Por favor, ingresa tu edad: "))
ingresos_mensuales = int(input("Por favor, ingresa tus ingresos mensuales en €:"))

if edad > 16 and ingresos_mensuales >= 1000:
    print("Debes tributar.")
else:
    print("No necesitas tributar.")

