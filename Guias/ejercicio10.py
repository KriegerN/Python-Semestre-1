agenda={
    'Nombre':'Nico',
    'Dirección':'Calle 1239',
    'Ciudad':'Osorno',
    'Número telefónico':'923874629'
    }
agenda['Redes sociales']={'nico_facebook','nico_instagram','nico_twitter'}
print(f'La agenda modificada es: {agenda} \n')

print('Cambiando la forma en que se muestra la agenda en un formato más entendible \n')
for clave,valor in agenda.items():
    if isinstance(valor, set): 
        valor = ', '.join(valor)  
    print(f'{clave}: {valor}')