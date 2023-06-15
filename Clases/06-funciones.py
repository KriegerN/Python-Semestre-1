# Declarando una función simple
def mi_primera_funcion():
    print('Esta es mi primera función')
mi_primera_funcion()

def concatenar(lista1,lista2):
    return lista1 + lista2
a=[1,2,3]
b=[4,5,6]
# concatenar()
print(concatenar(a,b))

def multiplicacion(a,b):
    return a*b
print(multiplicacion(5,3))

'################ SUMA Y RESTA ################'

def suma(a,b):
    return a+b
print(suma(2,4))
def resta(a,b):
    return a-b


a=int(input('Ingrese a: '))
a=int(input('Ingrese b: '))