import numpy as np
import pandas as pd

lista1=[]
lista2=[]

def pedir_listas(lista):
    while True:
        if 0.0 in lista:
            lista.remove(0.0)
            break
        else:
            lista.append(float(input('Ingrese un número: ')))
            
def comprobar_elementos_listas(lista1,lista2):
    i=0
    if len(lista1) > len(lista2):
        diferencia = len(lista1) - len(lista2)
        while i < diferencia:
            i+=1
            lista2.append(1)
    elif len(lista2) > len(lista1):
        diferencia = len(lista2) - len(lista1)
        while i < diferencia:
            i+=1
            lista1.append(1)
            
def multiplicar_elementos(lista1,lista2):
    return np.multiply(lista1,lista2)

def dividir_elementos(lista1,lista2):
    return np.divide(lista1,lista2)

def combinar_listas(lista1,lista2):
    return lista1 + lista2
    
def promedio(lista):
    return np.mean(lista)

def mediana(lista):
    return np.percentile(lista,50)

# INGRESAR ELEMENTOS FLOAT A LAS LISTAS
print('Ingrese la lista número 1 (0 Para salir).')
pedir_listas(lista1)
print('Ingrese la lista número 2 (0 Para salir).')
pedir_listas(lista2)

print(f'La lista 1 es: {lista1} ')
print(f'La lista 2 es: {lista2}')

# SE COMPRUEBAN QUE LOS ELEMENTOS EN AMBAS LISTAS SEAN LA MISMA CANTIDAD PARA EVITAR ERRORES
# EN CASO DE SER DISTINTA CANTIDAD, SE LE AÑADE UN 1 A LA RESPECTIVA LISTA CON MENOS ELEMENTOS.
comprobar_elementos_listas(lista1,lista2)

# MULTIPLICAR LOS ELEMENTOS DE AMBAS LISTAS
listas_multiplicadas = multiplicar_elementos(lista1,lista2)
print(f'Las listas multiplicadas son: {listas_multiplicadas}')

# DIVIDIR LOS ELEMENTOS DE AMBAS LISTAS

listas_divididas = dividir_elementos(lista1,lista2)
print(f'Las listas divididas son: {listas_divididas}')

# OBTENER EL PROMEDIO DE AMBAS LISTAS COMBINADAS

listas_combinadas = combinar_listas(lista1,lista2)
promedio_listas = promedio(listas_combinadas)
print(f'El promedio de las listas combinadas es: {promedio_listas}')

# OBTENER LA MEDIANA DE AMBAS LISTAS COMBINADAS 

mediana_listas = mediana(listas_combinadas)
print(f'La mediana de ambas listas combinadas es: {mediana_listas}')