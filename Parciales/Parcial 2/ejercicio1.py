def palindromo():
    print('--- Determinar si una palabra ingresada por teclado es una palíndromo ---')
    palabra=str(input('Ingrese una palabra: ').lower())
    lista=[]
    for i in palabra:
        lista.insert(0,i)
    palabraalreves=''.join(lista)
    print(palabraalreves)
    if palabra==palabraalreves:
        print(f'La palabra {palabra} es un palíndromo')
    else:
        print(f'La palabra {palabra} no es un palíndromo')
palindromo()