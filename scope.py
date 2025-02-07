planet = "Earth" #global variable

def printPlanet():
    planet = "Mars" #local variable, only known to printPlanet function

    print(f"Planet inside function : {planet}")


def changeGlobal():
    global planet
    planet = 'Jupiter'
    print(f"Updated gloabl : {planet}")


printPlanet()
print(f"Planet outside function : {planet}")
planet = "Saturn"
print(f"Updated planet : {planet}")
changeGlobal()

PI = 3.14

print(f"Constant PI : {PI}")
