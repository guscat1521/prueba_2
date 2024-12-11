print("************************************************* \n" )
print("      programa de deteccion de pares a impares     \n  ")
print("************************************************** \n")

Numero_entero = int(input("Ingresa el numero que deseas comparar: \n"))
operacion = Numero_entero % 2
if operacion == 0:
    print("el numero ", Numero_entero ,  " es par")
elif operacion >= 1 :
    print("el numero " , Numero_entero, " es impar")
else:
    print("la opcion no exixste ")