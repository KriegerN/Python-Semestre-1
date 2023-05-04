print("-------Ingresar datos del paciente 1-------")
#NOMBRE
paciente1nombre=str(input("Ingrese su nombre: "))
#EDAD
paciente1edad=int(input("Ingrese su edad: "))
while paciente1edad<0 or paciente1edad>200: 
    paciente1edad=int(input("Ingrese una edad válida: "))
#PESO
paciente1peso=float(input("Ingrese su peso: "))
while paciente1peso<0:
    paciente1peso=float(input("Ingrese un peso válido: "))
#ESTATURA
paciente1estatura=float(input("Ingrese su estatura: "))
while paciente1estatura<0:
    paciente1estatura=float(input("Ingrese una estatura válida: "))
#Conversión a tupla
paciente1datos=[paciente1nombre,paciente1edad,paciente1peso,paciente1estatura]
paciente1datos=tuple(paciente1datos)

print("")
print("-------Ingresar datos del paciente 2-------")
#NOMBRE
paciente2nombre=str(input("Ingrese su nombre: "))
#EDAD
paciente2edad=int(input("Ingrese su edad: "))
while paciente2edad<0 or paciente2edad>200: 
    paciente2edad=int(input("Ingrese una edad válida: "))
#PESO
paciente2peso=float(input("Ingrese su peso: "))
while paciente2peso<0:
    paciente2peso=float(input("Ingrese un peso válido: "))
#ESTATURA
paciente2estatura=float(input("Ingrese su estatura: "))
while paciente2estatura<0:
    paciente2estatura=float(input("Ingrese una estatura válida: "))
#Conversión a tupla
paciente2datos=[paciente2nombre,paciente2edad,paciente2peso,paciente2estatura]
paciente2datos=tuple(paciente2datos)

("")
print("-------Ingresar datos del paciente 3-------")
#NOMBRE
paciente3nombre=str(input("Ingrese su nombre: "))
#EDAD
paciente3edad=int(input("Ingrese su edad: "))
while paciente3edad<0 or paciente3edad>200: 
    paciente3edad=int(input("Ingrese una edad válida: "))
#PESO
paciente3peso=float(input("Ingrese su peso: "))
while paciente3peso<0:
    paciente3peso=float(input("Ingrese un peso válido: "))
#ESTATURA
paciente3estatura=float(input("Ingrese su estatura: "))
while paciente3estatura<0:
    paciente3estatura=float(input("Ingrese una estatura válida: "))
#Conversión a tupla
paciente3datos=[paciente3nombre,paciente3edad,paciente3peso,paciente3estatura]
paciente3datos=tuple(paciente3datos)
#Se imprimen todos juntos
print("")
print("Los datos del primer paciente son:",paciente1datos)
print("Los datos del segundo paciente son:",paciente2datos)
print("Los datos del tercer paciente son:",paciente3datos)

