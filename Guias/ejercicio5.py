lab1=float(input('Ingrese la nota del laboratorio 1 (Entre 1 y 7): '))
while lab1<1 or lab1>7:
    print('Valor invalido')
    lab1=float(input('Ingrese la nota del laboratorio 1 (Entre 1 y 7): '))
lab2=float(input('Ingrese la nota del laboratorio 2 (Entre 1 y 7): '))
while lab2<1 or lab2>7:
    print('Valor invalido')
    lab2=float(input('Ingrese la nota del laboratorio 2 (Entre 1 y 7): '))
lab3=float(input('Ingrese la nota del laboratorio 3 (Entre 1 y 7): '))
while lab3<1 or lab3>7:
    print('Valor invalido')
    lab3=float(input('Ingrese la nota del laboratorio 3 (Entre 1 y 7): '))
promedio=round(lab1*0.3+lab2*0.4+lab3*0.3,1)
if promedio<4:
    print('Su promedio es: ',promedio,'y el estudiante ha reprobado')
elif promedio<=4 and promedio<6:
    print('Su promedio es: ',promedio,'y el estudiante ha aprobado')
else:
    print('Su promedio es: ',promedio,'y el estudiante ha aprobado con distinción')