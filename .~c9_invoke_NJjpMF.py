# Un comentario de una sola línea 
# ESTO SE VA A IGNORAR

"""
UN COMENTARIO MULTILINEA
ESTO 
TAMBIÉN
SE
IGNORA
"""

### Tipos de datos en python

#### Números: Operaciones aritméticas

## int entero integer
## un número natural que puede estar entre -n a n

## Debemos almacenarlo en una variable

"""
 La variable es la representación de un valor
 el nombre es un identificador

 NO puedo llamar a una variable incumpliendo
 
 * NO puede iniciar con un número: 2variable
 * NO puede tener caracteres especiales: varieb"#af 
 * NO puede contener espacios: valor total
 * NO puede ser una palabra reservada (for, while, or, try, except, etc)

 SI puedo:
 * Utilizar números en medio o al final: variable2 o var2iable
 * Utilizar guión bajo: variable_total
 * Sólo llamarse guión bajo: _
 * Diferenciar entre mayúsculas y minúsculas: num NUM
 
"""
# Python intuye el tipo de dato
# Para nombrar una variable debo asignar un valor así:
# identificador = valor

num = 2
num2 = 10

print(num) # son diferentes
print(num2)

# vemos el tipo de dato con type()
print(type(num)) # <class 'int'>

resultado = num + num2

print(resultado)


# Forma práctica de imprimir con variables
# Uso del f-string


print(f"Hola, realicé una operación tatata")
