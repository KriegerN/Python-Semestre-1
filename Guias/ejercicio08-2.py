estacion_mes = {
    'diciembre': 'verano',
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
}
mes = input("Ingrese un mes: ").lower()
while mes not in estacion_mes:
    print('Ingrese un mes válido')
    mes = input("Ingrese un mes: ").lower()
    
if mes in estacion_mes:
    print(f"La estación correspondiente al mes {mes} es {estacion_mes[mes]}")