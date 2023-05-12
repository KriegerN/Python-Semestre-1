palabra1=str(input('Ingrese la primera palabra: '))
palabra2=str(input('Ingrese la segunda palabra: '))
if len(palabra1)>len(palabra2):
    print(palabra1,'tiene más caracteres.')
    print(palabra2,'tiene menos caracteres.')
else:
    print(palabra2,'tiene más caracteres.')
    print(palabra1,'tiene menos caracteres.')