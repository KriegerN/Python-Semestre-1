# Datos de un tipo numerico
estatura = 1.71 #Real
edad= 29 #Entero
peso = 70.5 #Real
complejo = 1 + 4j #Complejo, se pone j para los complejos
print("Impresión del número complejo",complejo)
print(f"Mi estatura es de {estatura}")
# Operacion aritmetica basica para sacar el imc
imc = peso/estatura**2
print("Mi IMC es de:",imc)

#El codigo {:.2f} es para aproximar y va entre comillas y .format es para 
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
print(type(ampolleta))

ampolleta='soy una ampolleta'
print(type(ampolleta))

estudiantes = ['Matias', 'Marco', 'Cristobal', 'Sebastián']
num=[1,2,3,4,5,6]
lenguaje = ["Python"]
data= ["Osorno", {"UV": "nivel bajo", "Temp ºC": 15}, (-40.5725, -70.432)]
print(data)
print(len(data)) #Con len() podemos ver cuantos tipos de elementos, hay, deberian ser 3.
print("lista de cadena de caracteres:",estudiantes)
print("lista de números:",num)
print("lista de elementos:",lenguaje)
#Con .count() podemos buscar un elemento dentro de una lista y nos muestra donde está.
print(estudiantes.count("Matias"))
#Datos tipo array (objetos de tipo colección) o arreglos. Con array se gasta menos memoria que con list() pero list() es mas dinamico
#y array es mas limitado a un tipo de dato.
nueva_lista = list()
print("Esta es una lista vacia",nueva_lista)
# los corchetes [] se utilizan para crear una lista
# que es una colección ordenada, los elementos de la lista están separados por comas



