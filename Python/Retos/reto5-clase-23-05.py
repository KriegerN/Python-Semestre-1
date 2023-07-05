while True:
    num=int(input('Ingrese un número: '))
    if num==0:
        break
    i,suma=1,0
    while i<num:
        if num%i==0: 
            suma+=1
        i+=1
    print(num,'Es par',end='') if num%2==0 else print(num,'Es impar',end='')
    print(', es un número primo',end=' ') if suma==1 else print(', no es un número primo',end=' ')
    print('y mayor que 50') if num>50 else print('y es menor o igual que 50')