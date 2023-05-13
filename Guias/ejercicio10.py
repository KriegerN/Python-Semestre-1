agenda={
    'Nombre':'Nico',
    'Dirección':'Calle 1239',
    'Ciudad':'Osorno',
    'Número telefónico':'923874629'
    }
agendasincambios=agenda
agenda['Redes sociales']={'Facebook':'nico_facebook','Instagram':'nico_instagram','Twitter':'nico_twitter'}
print(f'El facebook del contacto es {agenda["Redes sociales"]["Facebook"]}')
print(f'La agenda completa actualizada es: {agenda} \n')

print('Cambiando la forma en que se muestra la agenda en un formato más entendible \n')
for clave, valor in agenda.items():
    if isinstance(valor, dict):
        print(f'{clave}:')
        for subclave, subvalor in valor.items():
            print(f'    {subclave}: {subvalor}')
    else:
        print(f'{clave}: {valor}')