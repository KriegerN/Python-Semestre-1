nombre1 = str(input("Ingrese el primer nombre: "))
nombre2 = str(input("Ingrese el segundo nombre: "))
if nombre1[0] == nombre2[0] and nombre1[-1] == nombre2[-1]:
    print('Ambos nombres empiezan por la misma letra y terminan con la misma letra')
elif nombre1[0] == nombre2[0]:
    print("Ambos nombres comienzan con la misma letra.")
elif nombre1[-1] == nombre2[-1]:
    print("Ambos nombres terminan con la misma letra.")
else:
    print("Los nombres tienen la letra inicial y la letra final distintas.")