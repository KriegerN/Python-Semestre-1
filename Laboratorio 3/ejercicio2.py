a = [21,8,15,3,12]
b = [10,9,12,15,18]
c = [2,3,8,9,12]
#a)Concatenar todas las listas e imprimir la lista obtenida.
listas_concatenadas=a+b+c
print(f'La lista es: {listas_concatenadas} \n')
#b)Agregar el número 20 en la penúltima posición de la lista.
listas_concatenadas.insert(-1,20)
print(f'La lista es: {listas_concatenadas} \n')
#c)Ordenar la lista de forma descendente.
listas_concatenadas.sort()
listas_concatenadas.reverse()
print(f'La lista es: {listas_concatenadas} \n')
#d)Insertar la lista [4,5,6] en la última posición de la lista ordenada.
nuevalista=[4,5,6]
listas_combinadas=listas_concatenadas.copy()
listas_combinadas.append(nuevalista)
listas_concatenadas.extend(nuevalista)
print(f'La lista es: {listas_combinadas} \n')
#e)Sumar todos los números dentro de la lista.
lista_sumada=sum(listas_concatenadas)
print(f'La lista sumada es: {lista_sumada} \n')
#f)Obtener el promedio simple de la lista.
promedio=lista_sumada/len(listas_concatenadas)
print(f'El promedio es: {promedio}')