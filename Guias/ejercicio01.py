n1=int(input("Ingrese el primer número: "))
n2=int(input("Ingrese el segundo número: "))
n3=int(input("Ingrese el tercer número: "))
numeros=[n1,n2,n3]
if n1==n2 and n2==n3:
    print('Los tres números son iguales')
else:
    print(f"El número más grande es {max(numeros)}")
    print(f"El número más pequeño es {min(numeros)}")