while True:
    input("ingrese un numero")
    num1=int(input())

    input("ingrese otro numero")
    num2= int(input())

    resultado= num1+num2
    print(resultado)

    respuesta= input("desea continuar? (s/n):")
    if respuesta == "n":
        break