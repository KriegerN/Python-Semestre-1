verano='enero','febrero','diciembre'
otonio='marzo','abril','mayo'
invierno='junio','julio','agosto'
primavera="septiembre",'octubre','noviembre'
mes=str(input('Ingrese el mes: ')).lower()
while mes not in verano and mes not in otonio and mes not in invierno and mes not in primavera:
    print('Mes inválido')
    mes=str(input('Ingrese el mes nuevamente: ')).lower()
if mes in verano:
    print('Es verano')
elif mes in otonio:
    print('Es otoño')
elif mes in invierno:
    print('Es invierno')
elif mes in primavera:
    print('Es primavera')