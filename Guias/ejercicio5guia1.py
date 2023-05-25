import random
lista=[]
for i in range(0,20):
    lista.append(random.randint(40,350))
    print(f'El número elegido al azar es: {lista[i]}')
buscar=int(input('Ingrese un número para conocer su número de ocurrencias: '))
print(lista.count(buscar))