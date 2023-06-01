print('''Se cuenta con dos sets: el primero contiene las temperaturas mínimas tomadas el mes de
Mayo en Osorno. El segundo set contiene las temperaturas máximas:''')
mintemp = {9, 5, 2, 7, 6, 1}
maxtemp = {12, 14, 11, 10, 15, 9}
print(f'Temperaturas mínimas: {mintemp}')
print(f'Temperaturas máximas: {maxtemp}')
# a)Verificar si la temperatura 9°C está en ambos sets
if 9 in mintemp.intersection(maxtemp):
    print(f'9°C está en ambos sets')
else: 
    print('9°C No está en ninguno de los 2 sets')
# b)Comprobar si al menos la temperatura 6°C y 17°C está en alguno de los sets
if  6 or 17 in mintemp.union(maxtemp):
    print('La temp 6°C o 17°C se encuentra dentro de alguno de los sets.')
else:
    print('No se encuentra la temp 6°C o 17°C dentro de ninguno de los sets.')
    
# c)Elevar a 4 todas las temperaturas dentro de los sets
mintemp_actualizada=set()
maxtemp_actualizada=set()
for i in mintemp:
    mintemp_actualizada.add(i+4)
for j in maxtemp:
    maxtemp_actualizada.add(j+4)
print(f'Las temperaturas minimas actualizadas aumentando en 4 cada temperatura es: {mintemp_actualizada}')
print(f'Las temperaturas maximo actualizadas aumentando en 4 cada temperatura es: {maxtemp_actualizada}')
# d)Unir ambos sets en uno solo
union=mintemp_actualizada.union(maxtemp_actualizada)
print(union)