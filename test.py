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
#salida = altura + avanza - retroceso
dia =  0 
recorrido = 0 
while ( recorrido <= altura ) :
    print( "dia:" )
    print(dia) 
    print("recorrio:")
    print(recorrido)
    recorrido = recorrido + avanza - retroceso
    dia = dia + 1
    if(dia > 100) :
        print("100 dias la rana se murio")
        break

print("-------")
print("Se tardo en salir:")
print(dia)# import math

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
#salida = altura + avanza - retroceso
dia =  0 
recorrido = 0 
while ( recorrido <= altura ) :
    print( "dia:" )
    print(dia) 
    print("recorrio:")
    print(recorrido)
    recorrido = recorrido + avanza - retroceso
    dia = dia + 1
    if(dia > 100) :
        print("100 dias la rana se murio")
        break

print("-------")
print("Se tardo en salir:")
print(dia)