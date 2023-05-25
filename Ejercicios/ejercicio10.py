agenda={
    'Nombre':'Nico',
    'Dirección':'Calle 1239',
    'Ciudad':'Osorno',
    'Número telefónico':'923874629'
    }

agenda['Redes sociales']={
    'Facebook':'nico_facebook',
    'Instagram':'nico_instagram',
    'Twitter':'nico_twitter'
    }
print(f'El facebook de {agenda["Nombre"]} es {agenda["Redes sociales"]["Facebook"]}')
print(f'''La agenda completa actualizada es: 
Nombre: {agenda["Nombre"]}
Dirección: {agenda["Dirección"]}
Ciudad: {agenda["Ciudad"]}
Número telefónico: {agenda["Número telefónico"]}
Redes sociales: 
    Facebook: {agenda["Redes sociales"]['Facebook']}
    Instagram: {agenda["Redes sociales"]['Instagram']}
    Twitter: {agenda["Redes sociales"]['Twitter']}
''')