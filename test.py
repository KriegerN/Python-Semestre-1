#Se pueden sumar las tuplas?
grupo1 = ("Daniel","Cristian","Felipe",200,100,"Daniel")
grupo2=("Constanza","Cristobal",150,250)
grupos=grupo1+grupo2
print(grupos,"\n")

#Entonces como no puedo modificar una tupla, ¿Que puedo hacer?
grupo1=list(grupo1)
print("La tupla ahora es de tipo:",type(grupo1),"\n")
grupo1=tuple(grupo1)
print("La tupla ahora es de tipo:",type(grupo1),"\n")