# --- ESTACIONES ---
verano='enero','febrero','diciembre'
otonio='marzo','abril','mayo'
invierno='junio','julio','agosto'
primavera='septiembre','octubre','noviembre'
meses=verano+invierno+primavera+otonio
mes=str(input('Ingrese el mes: ')).lower()
while mes not in meses:
    mes=str(input('Ingrese el mes nuevamente: ')).lower()
if mes in verano:
    print('Es verano')
elif mes in otonio:
    print('Es otoño')
elif mes in invierno:
    print('Es invierno')
elif mes in primavera:
    print('Es primavera')