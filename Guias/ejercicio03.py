a=float(input('Ingrese el primer lado: '))
b=float(input('Ingrese el segundo lado: '))
c=float(input('Ingrese el tercer lado: '))
p=(a+b+c)/2
area=round(((p*(p-a)*(p-b)*(p-c))**0.5),2)
if a==b and b==c:
    triangulo='triangulo equilátero'
    print(f'Es un {triangulo}')
    print(f'Su área es de {area} cm^2')
elif a==b or b==c or a==c:
    triangulo='triangulo isosceles'
    print(f'Es un {triangulo}')
    print(f'Su área es de {area} cm^2')
else:
    triangulo='triangulo escaleno'
    print(f'Es un {triangulo}')
    print(f'Su área es de {area} cm^2')