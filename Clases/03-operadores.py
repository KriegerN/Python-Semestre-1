'''
"""  01----------OPERADORES ARITMETICOS------------  """
#Declarando variables de tipo entero
a=20
b=5
c=4
d=20
"""  02-----------OPERACIONES BASICAS--------------  """
x = 2 + 3 # Suma
print(x)  # salida: 5

y = 7 - 4 # Resta
print(y)  # salida: 3

z = 5 * 6 # Multiplicación
print(z)  # salida: 30

f = 10 / 2 # División
print(f)  # salida: 5.0

g = 10 // 3 # División entera
print(g)  # salida: 3

h = 2 ** 3 # Potencia o elevado
print(h)  # salida: 8

o = 7 % 3 # Módulo
print(o)  # salida: 1

#Declarando variables de tipo flotantes
tiempo=5.39 #tiempo en SEGUNDOS
gravedad=9.81 #la aceleracion de gravedad (METRO POR SEGUNDOS CUADRADO)

#Operaciones aritmeticas con flotantes
velocidad=gravedad*tiempo
print(f"La velocidad del objeto en caida libre es de: {velocidad} m/s")
print("La velocidad del objeto en caida libre es de: {:.2f}".format(velocidad),"m/s")
print(f"La velocidad del objeto en caida libre es de: {velocidad:.2f} m/s")
print("La velocidad del objeto en caida libre es de:","%.2f" % velocidad,"m/s")

#Declarando variables de tipo compleja
c1= 4 + 3j
print(type(c1))

#Creando un numero complejo con complex
c2= complex(3, -5)
print("El numero complejo es:",c2)

print(c2.real) #Obteniendo la parte real del numero complejo
print(c2.imag) #Obteniendo la parte imaginaria del numero complejo

#¿Se puede realizar esta operación? ¿Multiplicar un string por un entero?
print("Hola" * 5)
#Y la siguiente multiplicación?
"""print("Hola" * 3.5*2) """ #No por que nos pasamos un poco poniendo enteros, flotantes y string.
# Y esta?
print("Hola" * (int((10*2)/5)),"\n") #Si, porque da un numero entero y no se dejan flotantes

#Y por ultimo esta?
#print("Hola" + 20)
print("Hola" + str(20))
"""########### 02-OPERADORES DE COMPARACION ##########"""

#Comparando terminos numericos
print("Comparando números")
print(a==b) #Igual a
print(a != b) #Desigual a 
print(a > b) #Mayor a
print(a < b) #Menor a
print(c >= d) #Mayor o igual a
print(c <= d) #Menor o igual a
print("\n")

#Comparando cadenas de caracteres
animal_domestico="gato"
animal_salvaje="leopardo"
print("Comparando cadenas de caracteres")
print(animal_domestico == animal_salvaje) # Igual a
print(animal_domestico != animal_salvaje) # Desigual a
print(animal_domestico > animal_salvaje) # Mayor a
print(animal_domestico < animal_salvaje) # Menor a
print(animal_salvaje >= animal_domestico) # Mayor o igual a
print(animal_salvaje <= animal_domestico) # Menor o igual a
'''
bencina = True
encendido = True
edad = 19

#Utilizando el operador AND
if bencina and encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

#Utilizando el operador OR 
if bencina or encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

#Utilizando el operador NOT junto al AND
if not bencina and encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")
