milla_en_km = 0.621

planeta1 = input("¿Cuál es la distancia del sol a tu primer planeta?")
planeta2 = input("¿Cuál es la distancia del sol a tu segundo planeta?")
planeta1_km = int(planeta1)
planeta2_km = int(planeta2)
print("Distancia entre tu primer y segundo planetas:")
diferencia = abs(planeta1_km - planeta2_km)
print(f"En metros: {diferencia} kilómetros")
print(f"En millas: {round(diferencia * milla_en_km)} millas")