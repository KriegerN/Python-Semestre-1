a = [10,80,15,30,20]
b = [20,45,80,20,10]
c = [20,35,60,90,20]
def valores_comun(a,b,c):
    comunes=[]
    for i in a:
        if i in b and c:
            comunes.append(i)
    return comunes

def eliminar_duplicados(lista):
    lista=list(set(lista))
    return lista

def concatenar(a,b,c):
    lista=a+b+c
    return lista

def ordenar_descendente(lista):
    lista_ordenada=lista.sort(reverse=True)
    return lista_ordenada

def reemplazar_posicion7(lista):
    num=lista[6]
    lista.insert(num,100)
    return lista


print(f'Los valores comunes entre a, b y c son: {valores_comun(a,b,c)}')
listas=concatenar(a,b,c)
print(f'Listas concatenadas {listas}')
ordenar_descendente(listas)
print(f'Lista ordenada en descendente: {listas}')
reemplazar_posicion7(listas)
print(f'La lista con el valor de la posicion 7 reemplazado: {listas}')