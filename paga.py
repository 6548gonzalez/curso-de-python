# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
#    Después debe mostrar por pantalla la paga que le corresponde.

print("ingrese su numero de horas trabajadas")
entrada= int(input ())

print("ingrese el coste")
paga= float(input())
resultado= (entrada*int(paga))

print(" su paga es " + str(resultado) )
