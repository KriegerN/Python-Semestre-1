'''
#Declarando variables de tipo texto
name='Nico'

nombre = 'Nicolás'

print('Hola soy',name)

#Declarando variable de tipo númerico
edad = 19

print('Mi edad es',edad)

print('Hola soy '+nombre+' y tengo '+str(edad)+' años')

#No se puede concadenar diferentes tipos de datos con +, por lo que se transforma el dato de edad a string.
#Es recomendable utilizar el signo + para unirlos, y a diferencia de la coma , no agrega espacios por lo que hay que añadirlos

print(f"Hola mi nombre es {nombre} y tengo {edad} años")
#Desde las ultimas versiones de python se puede usar los corchetes {} para poner las variables y asi hacerlo más amigable.
nombre='Andrés'

#Se asigna nuevamente la variable nombre pero también se puede crear otra con nombre1 si es necesario tener ambas.

print('Hola mi nuevo nombre es:',nombre)

#Se usa input para pedir datos

nombre1 = input('¿Cual es tu nombre?: \n')

print('Su nombre es:',nombre1)

#El \n sirve para bajar una linea.
#El identificador de una variable es su nombre.

ciudad, region, pais, year = "Puerto Montt", "Los Lagos", "Chile", 2023
#Se puede asignar varias variables a la vez, separandolas por comas.
print(f"Hola vivo en {ciudad}, en la región de {region}, en el país de {pais}, y es el año {year}")
'''