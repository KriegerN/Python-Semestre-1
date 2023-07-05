"---- TIPO DE DATOS ----"

# Datos de un tipo numerico

estatura = 1.71 #Real

edad= 29 #Entero

peso = 70.5 #Real

complejo = 1 + 4j #Complejo, se pone j para los complejos

print("Impresión del número complejo",complejo,"\n")

print(f"Mi estatura es de {estatura}")

# Operacion aritmetica basica para sacar el imc

imc = peso/estatura**2

# Transformando Real a Entero
print(peso)
print("Transformando un valor real a entero:",int(peso))

# Transformando un Entero a Real
print(edad)
print("Transformando Entero a Real:",float(edad))
print("Mi IMC es de:",imc)

#formateando la salida a dos decimales
print("Mi IMC es de: {:.2f}" .format(imc), "\n")

# Datos de tipo cadena de caracteres
asignatura= 'programación'

carrera= 'Ingenieria Civil en Informatica'

print('La asignatura de',asignatura,'corresponde a la carrera de',carrera)

print('La asignatura de',len(asignatura),'corresponde a la carrera de',len(carrera))

#Funciones propias de python 

#str() , int() , float() len() , type()= String es para texto, Int para enteros, float para reales, 
#y len cuenta los caracteres, por ej: "Hola"= 4


# Valores booleanos
ampolleta=False
interruptor=True

# Con type sabemos el tipo de datos que estamos tratando
print(type(ampolleta),"\n")

ampolleta='soy una ampolleta'

print(type(ampolleta),"\n")

#Podemos transformar cualquier valor a un Booleano (al igual que un string)
print(bool(0)) #0 Significa apagado por lo que es False.
print(bool("")) #Vacio por lo que dará False.
print(bool(None)) #Ninguno por lo que dará False.
print(bool("False")) #Es una cadena de texto por lo que es True.
print(bool(1)) #1 es encendido por lo que siempre va a dar True.
print("\n")

estudiantes = ['Matias', 'Marco', 'Cristobal', 'Sebastián', "Marco"]

num=[1,2,3,4,5,6]

lenguaje = ["Python"]

data= ["Osorno", {"UV": "nivel bajo", "Temp ºC": 15}, (-40.5725, -70.432)]

print(data)

print(len(data)) #Con len() podemos ver cuantos tipos de elementos, hay, deberian ser 3.

print("lista de cadena de caracteres:",estudiantes)

print("lista de números:",num)

print("lista de elementos:",lenguaje)
listamixta=[100,"Felipe",False]
print(len(listamixta)) #Para ver cuantos elementos hay en una lista

#Con .count() podemos buscar un elemento dentro de una lista y nos muestra donde está.

print(estudiantes.count("Matias"))

#Datos tipo array (objetos de tipo colección) o arreglos. Con array se gasta menos memoria que con list() pero list() es mas dinamico
#y array es mas limitado a un tipo de dato.
nueva_lista = list([11,13,14,12])
nueva_listita= [10,11,12] #Es más fácil de esta manera, y hace lo mismo que arriba. 
print("Esta es una lista vacia",nueva_lista,"\n")

# los corchetes [] se utilizan para crear una lista
# que es una colección ordenada, los elementos de la lista están separados por comas
#Como acceder a un elemento especifico en la lista? si pones -1 va del ultimo al primero, muy util para recorrer listas

print(estudiantes[0])

print(estudiantes[-1])

#Reasignar el valor de una posicion

estudiantes[0] = "Gabriela"

print(estudiantes[0],"\n")

#Se pueden sumar listas?
listas=estudiantes+num

print(listas,"\n")


#Inicializando otra lista de datos mixtos
data_asig = [10023, "Programación",1,True]

#¿Qué hace este codigo? le da nombres a los datos de la lista
cod,ramo,semestre,estado= data_asig
print(ramo,"\n")

print("Se pueden sumar las listas?",estudiantes+num) #Si, si se pueden sumar

#¿Que hacen estas funciones?
print(list("Python"))
# genera una lista de 10 elementos
print(list(range(10)))

print("\n")


# TUPLAS, las tuplas se hacen con parentesis y no son mutables
grupo1 = ("Daniel","Cristian","Felipe",200,100,"Daniel")

print("###### TUPLAS ######")
print(type(grupo1),"\n")

#Accediendo al primer elemento de la tupla
print(grupo1[0])

#Consultando el elemento "Daniel" cuantas veces se encuentra en la tupla
print("El elemento se repite:",grupo1.count("Daniel"),"veces","\n")

#Muestra el indice del primer elemento buscado
print("El indice del elemento es:",grupo1.index("Daniel"),"\n")

#Reasignar el primer elemento de la tupla
#grupo1[0]="Constanza"
#print(grupo1[0])
#NO ES MUTABLE

#Se pueden sumar las tuplas?
grupo2=("Constanza","Cristobal",150,250)
grupos=grupo1+grupo2
print(grupos,"\n")

#Entonces como no puedo modificar una tupla, ¿Que puedo hacer?
grupo1=list(grupo1)
print("La tupla ahora es de tipo:",type(grupo1),"\n")
print("\n")
print(grupo1[1:4])

# SETS o Conjuntos
#Formas de inicializar un Set
conjunto_vacio = set()
conjunto_vacio1 = {} #diccionario o set?
print(type(conjunto_vacio1))
conjunto_colores = set({"Azul","Rojo","Verde"}) #utilizando la funcion set
conjunto_animales = {"Gato","Perro","Loro"} #Utilizando corchetes
print(type(conjunto_colores))
print(type(conjunto_animales)) #Este dice que es un set porque añadimos elementos, aunque lo hayamos hecho con {} llaves
print(f"El primer set contiene los siguientes colores: {conjunto_colores}")
print(f"El segundo set contiene los siguientes animales: {conjunto_animales}")

#print(conjunto_animales[0]) #accediendo al primer elemento del set, da error.
conjunto_colores.add("Celeste")
print(f"El set de colores lo conforman: {conjunto_colores}")
conjunto_animales.add("Cocodrilo")
print(f"El set de animales lo conforman: {conjunto_animales}")
print("\n")

""" -------Diccionarios------ """
diccionari1=dict()
diccionario2={}

print(type(diccionario2))

datos_personales={
    "Nombre":"Nicolás",
    "Institución":"Ulagos",
    "Edad":29,
    "Asignaturas": {"Estructura de Datos", "Programación"}
    }

print("Diccionario inicial:",datos_personales)

#Clave es lo mismo que un campo
#Consulta la cantidad de elementos del Diccionario
print(len(datos_personales))

#Como acceder a un elemento especifico de una lista?
print(datos_personales["Institución"])

#Como actualizamos el valor de una clave dentro de un diccionario?
datos_personales["Institución"] = "USS"

#Agregando un nuevo campo al diccionario
datos_personales["Ciudad"] = "Osorno"
print(datos_personales)

#Eliminando un campo del diccionario
del datos_personales["Ciudad"]
print("Diccionario con el campo eliminado:",datos_personales)

hospital = dict(
    nombre = "Hospital San Nico",
    direccion = "Dr. Guillermo Buhler 1765",
    ciudad = "Osorno"
)