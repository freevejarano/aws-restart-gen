"""

----  Calculadora automática de 2 números ----

Vamos a solicitar al usuario 2 números
y a realizar todas las operaciones posibles (+, -, *, /, //, %, **)
mostrando los resultados de una forma clara

"""

num = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))

suma = num + num2
resta = num - num2
mult = num * num2
div = num / num2
div_entera = num // num2
modulo = num % num2
exponente = num ** num2