def frase(a):
    lista=a.split()
    longitud=len(a)
    diccionario={
        'Palabras':lista,
        'Longitud':longitud
    }
    print(diccionario)
frase(input('Escriba una frase para crear un diccionario con sus palabras y longitud: '))