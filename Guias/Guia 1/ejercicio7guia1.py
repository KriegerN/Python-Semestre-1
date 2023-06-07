def nfactorial(n):
    suma=1
    for i in range(n):
        a=n-i
        suma*=a
    return suma
    

print('---- Determinar el factorial de un número n ----')
while True:
    n=int(input('Ingrese n: '))
    if n>0:
        factorial=nfactorial(n)
        print(f'El factorial de {n}! es {factorial}')
    else:
        break
