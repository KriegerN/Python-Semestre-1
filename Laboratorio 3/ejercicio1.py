#a)Guardar la información de la tabla en un diccionario, luego imprimir el diccionario por consola.
censo2017={
    'ID 14':{
    'ID':14,
    'Nombre': 'Los Rios',
    'Superficie':18429,
    'Habitantes':404432}
    ,
    'ID 12':{
    'ID':12,
    'Nombre': 'Magallanes',
    'Superficie':1382291,
    'Habitantes':166533}
    }
print(f'El diccionario es: \n {censo2017} \n')
#b)Crear una nueva clave al diccionario llamada “Densidad”. La densidad poblacional se
# calcula de la siguiente forma: (Densidad = Habitantes/Superficie). Solamente debe
# tener 1 decimal la salida del resultado.
censo2017['ID 14']['Densidad']=round((censo2017['ID 14']['Habitantes']/censo2017['ID 14']['Superficie']),1)
censo2017['ID 12']['Densidad']=round((censo2017['ID 12']['Habitantes']/censo2017['ID 12']['Superficie']),1)
#c)Agregar otra clave llamada “Capital”, correspondiente a la capital de cada región
censo2017['ID 14']['Capital']='Valdivia'
censo2017['ID 12']['Capital']='Punta Arenas'
#d)Agregar otra clave con el nombre “Comunas” la cual será una lista de 3 comunas de cada región como mínimo.
comunas_id_14=['Rio Bueno','La Union','Paillaco']
comunas_id_12=['Cabo de Hornos','Puerto Williams','Porvenir']
censo2017['ID 14']['Comunas']=comunas_id_14
censo2017['ID 12']['Comunas']=comunas_id_12
#e)Crear una última clave llamada “Provincia” la cual almacenará el nombres de las provincias correspondiente a cada región. 
# Las provincias se guardarán en tuplas.
provincia_id_14=('Ranco','Valdivia')
provincia_id_12=('Antártica Chilena','Magallanes, Tierra del Fuego','Última Esperanza')
censo2017['ID 14']['Provincia']=provincia_id_14
censo2017['ID 12']['Provincia']=provincia_id_12
#f)Imprimir el diccionario nuevamente con las nuevas claves creadas.
print(f'El diccionario actualizado es: \n {censo2017["ID 14"]} \n {censo2017["ID 12"]}')