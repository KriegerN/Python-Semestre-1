numeros=[4,3,8,12,6,10,14,3,6]
print(f'La lista es: {numeros} \n')

numeros.pop(-1)
print(f'La lista con el ultimo numero eliminado es: {numeros} \n')

numeros.insert(0,2)
print(f'Añadiendo el 2 en la primera posición de la lista: {numeros} \n')

numeros=list(set(numeros))
print(f'Eliminando los duplicados {numeros} \n')

numeros=[4,3,8,12,5,10,14,3,6,9]
# ----  Media  ----
cantidad=len(numeros)
suma=sum(numeros)
media=round((suma/cantidad),1)
# ---- Mediana ----
numeros.sort()
mediana_index=(cantidad//2)
if (cantidad/2)%1==0.5:
    mediana=numeros[mediana_index]
else:
    mediana=(numeros[mediana_index-1]+numeros[mediana_index])/2
print(f'La lista ordenada es {numeros} y su media es de {media} y su mediana es {mediana}')