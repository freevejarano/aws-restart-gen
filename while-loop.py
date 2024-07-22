import random

print("Bienvenidxs al programa adivinador 🔮🧙‍♂️")
print("Las reglas son simples, pienso un número y tú adivinas")


number = random.randint(1,10) # Simulará la acción de "pienso en un número"

isGuessRight = False # Variable bool

# Mientras que "esCorrecto" no sea verdad sigo con el juego
while isGuessRight != True:
    guess = int(input("Ingresa un número: "))
    
    if guess == number:
        isGuessRight = True
        print("Yeiii, adivinaste, no hay premio, pero felicidades 🎉")
    else:
        print("Intenta otra vez")
    
        
"""
Un condicional puede verse con

if
if elif
if elif else
if else

"""