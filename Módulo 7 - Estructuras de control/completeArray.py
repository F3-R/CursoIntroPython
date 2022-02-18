new_planet = ''
planets = []
while new_planet.lower() != 'done':
    if(new_planet):
        planets.append(new_planet)
    new_planet = input("Inserta tu planeta: ")

for planet in planets:
    print("Planeta ", planet)