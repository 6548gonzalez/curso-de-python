# Escriba un programa que pida tres números y que escriba si son los tres iguales, 
#    si hay dos iguales o si son los tres distintos.

print("ingrese un numero")
num1=int(input())

print("ingrese un numero")
num2=int(input())

print("ingese un numero")
num3=int(input())

if num1 == num2 :
  
    if num2 == num3:
        print("los numeros son iguales")
    
    else:
        print("hay dos numeros iguales")
else: 
    if num2 == num3:
        print("2 numeros son iguales")
    else:
        print("ningun numero es igual")
