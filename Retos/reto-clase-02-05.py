datos_estudiante={
    "Nombre del estudiante": str(input("Ingrese su nombre: ")),
    "Asignatura":str(input("Ingrese el nombre de la asignatura: ")),
    "Nota Laboratorio 1":float(input("Ingrese su nota del laboratorio 1: ")),
    "Nota Laboratorio 2":float(input("Ingrese su nota del laboratorio 2: "))
    }
promedionota=datos_estudiante["Nota Laboratorio 1"]*0.3+datos_estudiante["Nota Laboratorio 2"]*0.7
print("Información del estudiante: ",datos_estudiante)
print("Su nota es:",round(promedionota,1))