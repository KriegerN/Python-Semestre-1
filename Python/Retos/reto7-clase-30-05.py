def frase(a):
    lista=a.split()
    quitarespacios=''.join(lista)
    longitud=len(quitarespacios)
    diccionario={
        'Palabras':lista,
        'Longitud':longitud
    }
    print(diccionario)
frase(input('Escriba una frase para crear un diccionario con sus palabras y longitud: '))