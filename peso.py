#    IMC = Peso(kg) / altura(m)2Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
#    calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase 
#    "Tu índice de masa corporal es <imc>" donde <imc> es el índice de masa corporal calculado 
#    redondeado con dos decimales.

#    IMC = Peso(kg) / altura(m)2

print("ingrese su peso")
peso= float(input())

print("ingrese su estatura en metros")
estatura=float(input())

imc= peso/estatura

print(" su imc es " + str(imc)  )