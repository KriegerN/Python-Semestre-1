palabra1=str(input('Ingrese la primera palabra: '))
palabra2=str(input('Ingrese la segunda palabra: '))
if len(palabra1)>len(palabra2):
    print(f'''La palabra 1: "{palabra1}" tiene más caracteres ({len(palabra1)})'
La palabra 2: "{palabra2}" tiene menos caracteres ({len(palabra2)})''')
else:
    print(f'''La palabra 2: "{palabra2}" tiene más caracteres ({len(palabra2)})
La palabra 1: "{palabra1}" tiene menos caracteres ({len(palabra1)})''')