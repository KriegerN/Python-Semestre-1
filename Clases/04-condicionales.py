"---- CONDICIONALES ----"

#CONDICIONAL IF
print('--- UTILIZANDO IF y ELSE ---')

licencia = True
edad = 19
automovil = False

#¿Estará correcto este código?                                                  - Código Incorrecto  
print('\n>>> Testeando los comparadores y el IF')
if licencia:
    print('Puedo conducir porque tengo licencia')
else:
    print('No tengo licencia para conducir')
#En caso de True imprimira que si puede conducir y en caso de false, será el else

#Sucede que la variable licencia se esta comparando con True,
#y se debe asignar directamente, es decir no se ocupa el ==, sino solamente el igual (=)

print('\n>>> Utilizando el primer condicional IF')
if licencia:
    print('Puedo conducir porque tengo licencia\n')
else:
    print('No tengo licencia para conducir\n')
print("Este print esta fuera del else")


print('>>> Utilizando el segundo condicional IF')
if edad:
    print('Puedo conducir porque soy mayor de edad\n')
else:
    print('No puedo conducir soy menor de edad\n')
    

print('>>> Utilizando el tercer condicional IF')
if edad >= 18:
    print('Puedo conducir porque soy mayor de edad\n')
else:
    print('No puedo conducir soy menor de edad\n')


print('################ 02 - UTILIZANDO IF, ELIF y ELSE ################')
if licencia and edad >= 18:
    print('Puedo conducir porque soy mayor de edad y tengo licencia')
elif automovil:
    print('Tengo automovil, pero no tengo licencia ni la edad necesaria')
else:
    print('No puedo conducir no tengo ni la edad, ni licencia ni automovil')

