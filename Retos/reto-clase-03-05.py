ciudades=["Santiago","Temuco","Osorno","Punta Arenas"]
indice_calidad_aire=[134,99,245,50]

indice_min = min(indice_calidad_aire)
ciudad_min=ciudades[indice_calidad_aire.index(indice_min)]

print(ciudad_min,"tiene el indice de calidad de aire más bajo:",indice_min)
if (indice_min>0 and indice_min<50):
    print("Calidad de aire de",ciudad_min,"es buena")
elif (indice_min>51 and indice_min<100):
    print("Calidad de aire de",ciudad_min,"es Moderada")
elif (indice_min>101 and (indice_min)<150):
    print("Calidad de aire de",ciudad_min,"es Dañina a la salud para grupos sensibles")
elif (indice_min>151 and (indice_min)<200):
    print("Calidad de aire de",ciudad_min,"es Dañina a la salud")
elif (indice_min>201) and (indice_min<300):
    print("Calidad de aire de",ciudad_min,"es Muy dañina a la salud")
else:
    print("La Calidad de aire de",ciudad_min,"es Peligrosa")

indice_max = max(indice_calidad_aire)
ciudad_max=ciudades[indice_calidad_aire.index(indice_max)]

print(ciudad_max,"tiene el indice de calidad de aire más alto:",indice_max)
if (indice_max>0 and indice_max<50):
    print("Calidad de aire de",ciudad_max,"es buena")
elif (indice_max>51 and indice_max<100):
    print("Calidad de aire de",ciudad_max,"es Moderada")
elif (indice_max>101 and (indice_max)<150):
    print("Calidad de aire de",ciudad_max,"es Dañina a la salud para grupos sensibles")
elif (indice_max>151 and (indice_max)<200):
    print("Calidad de aire de",ciudad_max,"es Dañina a la salud")
elif (indice_max>201) and (indice_max<300):
    print("Calidad de aire de",ciudad_max,"es Muy dañina a la salud")
else:
    print("Calidad de aire de",ciudad_max,"es Peligrosa")

'''Solución del profe:
ica=[134,99,245,50]
for i in range(len(ciudades)):
    if ica[i]>= 0 and ica[i] <= 50:
    print(ciudades[i],"tiene un indice de calidad de aire bueno")......
'''