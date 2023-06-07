def ingresarCantidad():
    n=int(input('Ingrese la cantidad de números que va a ingresar: '))
    return n

def suma_total(lista):
    sumanum = sum(lista)
    return sumanum

def suma_pares(lista):
    suma=0
    for i in lista:
        if i % 2 == 0:
            suma+=i
    return suma
  
def suma_impares(lista):
    suma=0
    for i in lista:
        if i % 2 == 1:
            suma+=i
    return suma

lista = []
n = ingresarCantidad()
for i in range(1,n + 1):
    num=int(input(f'Ingrese un número {i}: '))
    lista.append(num)
par_suma=suma_pares(lista)
impar_suma=suma_impares(lista)
total_suma=suma_total(lista)

print(f'La suma de todos los números es: {total_suma}')
print(f'La suma de los pares es: {par_suma}')
print(f'La suma de los impares es: {impar_suma}')