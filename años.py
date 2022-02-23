# Escriba un programa que pida el año actual y un año cualquiera y que escriba 
#    cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.

while True: 
    print("inserte el año actual")
    entrada=int(input())

    print("inserte un año cualquiera")
    año=int(input())


    resultado= entrada-año
    print(" han pasado " + str(resultado) + " años ")

    respuesta= input("desea continuar? (s/n)")
    if respuesta == "n":
        break
