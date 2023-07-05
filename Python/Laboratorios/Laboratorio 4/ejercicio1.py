trabajadores = [["Juan", [700000, 650000, 690000]], ["María", [681000, 710000, 590000]],
["Pedro", [590000, 635000, 705000]]]

# a)
def promedio(sueldo):
    suma=sum(sueldo)
    promedio=suma/len(sueldo)
    return promedio

# b)
def sueldomaximo(sueldo):
    sueldomax=max(sueldo)
    return sueldomax

# c)
def retencion_impuesto(sueldomax):
    retencion=sueldomax*0.1125
    return retencion

# d)
for i in trabajadores:
    trabajador=i[0]
    sueldos=i[1]
    promedio_t=promedio(sueldos)
    print(f'El promedio de {trabajador} es: {promedio_t}')
    print(f'El sueldo maximo de {trabajador} es: {sueldomaximo(sueldos)}')
    print(f'La retencion de impuestos de {trabajador} es de: {retencion_impuesto(sueldomaximo(sueldos))}')
