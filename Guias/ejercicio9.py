import math
numeros=[4,3,8,12,6,10,14,3,6]
print(f'La lista es: {numeros} \n')

del numeros[-1]
print(f'La lista con el ultimo numero eliminado es: {numeros} \n')

numeros=[4,3,8,12,6,10,14,3,6]
numeros.insert(0,2)
print(f'Añadiendo el 2 en la primera posición de la lista: {numeros} \n')

numeros=[4,3,8,12,6,10,14,3,6]
numeros=list(set(numeros))
print(f'Eliminando los duplicados {numeros} \n')

numeros=[4,3,8,12,6,10,14,3,6]
cantidad=len(numeros)
suma=sum(numeros)
media=round((suma/cantidad),1)
numeros_ordenados=sorted(numeros)
mediana_index=math.ceil(cantidad/2)
mediana=numeros_ordenados[mediana_index-1]
print(f'La lista ordenada es {numeros_ordenados}, su media es de {media} y su mediana es {mediana} \n')
