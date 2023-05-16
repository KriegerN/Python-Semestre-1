while True:
    mes = str(input('Ingrese un mes: ')).lower()
    if mes == 'enero' or mes == 'febrero' or mes == 'diciembre':
        print('La estación correspondiente al mes', mes, 'es verano')
        break
    elif mes == 'marzo' or mes == 'abril' or mes == 'mayo':
        print('La estación correspondiente al mes', mes, 'es otoño')
        break
    elif mes == 'junio' or mes == 'julio' or mes == 'agosto':
        print('La estación correspondiente al mes', mes, 'es invierno')
        break
    elif mes == 'septiembre' or mes == 'octubre' or mes == 'noviembre':
        print('La estación correspondiente al mes', mes, 'es primavera')
        break
    else:
        print('---Mes inválido---')