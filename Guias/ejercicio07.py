nombres=['Juan','Jose','Nico','Martin','Daniel']
edades=[21,24,19,18,17]
# trabajadores={
#     'Nombre':nombres,
#     'Edad':edades
#   }
# print(trabajadores['Nombre'],"\n",trabajadores['Edad'])
trabajadores=dict(zip(nombres,edades))
print(trabajadores)