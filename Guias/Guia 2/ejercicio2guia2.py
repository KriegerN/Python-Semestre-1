def ingresar_nombres():
    nombres=[]
    while True:
        nombres.append(str(input('Ingrese un nombre(0 para parar): ')))
        nombres_bien = [elemento.replace(" ", "") for elemento in nombres]
        if nombres_bien.count('0')==1:
            nombres_bien.remove('0')
            break
    return nombres_bien
def contar_letras(nombres):
    suma=0
    for i in nombres:
        suma+=len(i)
    return suma
def resultados(nombres,letras):
    return f'Los nombres son ({nombres}). Las letras contadas son {letras}'
    
nombres=ingresar_nombres()
letras=contar_letras(nombres)
print(resultados(', '.join(nombres[0:-1]) + f' y {nombres[-1]}', letras))
