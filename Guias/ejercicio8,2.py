estacion_mes = {
    'enero': 'verano',
    'febrero': 'verano',
    'marzo': 'otoño',
    'abril': 'otoño',
    'mayo': 'otoño',
    'junio': 'invierno',
    'julio': 'invierno',
    'agosto': 'invierno',
    'septiembre': 'primavera',
    'octubre': 'primavera',
    'noviembre': 'primavera',
    'diciembre': 'verano'
}
mes = input("Ingrese un mes: ").lower()
while mes not in estacion_mes:
    print('Ingrese un mes válido')
    mes = input("Ingrese un mes: ").lower()
if mes in estacion_mes:
    estacion = estacion_mes[mes]
    print(f"La estación correspondiente al mes {mes} es {estacion}")