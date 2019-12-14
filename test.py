# import math

# Pedir al usuario la altura
print("Ingrese la altura en metros del pozo (en metros):")
# Creo la variable altura entero
altura = int( input() )

# Pedir al usuario el avanze
print("Ingrese la cantidad de metros que avanza de dia (en metros):")
# Crear la variable avanza
avanza = int( input() )

# Pedir al usuario el avanze
print("Ingrese la cantidad de mets que cae de noche (en metros):")
# Crear la variable avanza
retroceso = int( input() )

# Falta determinar el algoritmo a usar
salida = altura + avanza - retroceso

print("Se tardo en salir:")
print(salida)