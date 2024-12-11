print("*************************")
print(" \n calculadora \n")
print("*************************")
print("________________________________")
print("menu de opciones")
print("________________________________\n")
print ( " 1.suma \n", "2.divicion \n", "3.divicion entera \n","4.resta \n", "5.exponente \n", "6. modulo o resto \n", "7. multiplicacion"  )
numero = int(input("seleccione un opcion: "))

if numero == 1:
    numero = int(input("ingrese el primer numero: "))
    numero += int(input("ingrese el segundo numero: "))
    print("La respuesta", numero)
elif numero == 2:
    numero = int(input("ingrese el primer numero: "))
    numero /= int(input("ingrese el segundo numero: "))
    print("La respuesta", numero)
elif numero == 3:
    numero = int(input("ingrese el primer numero: "))
    numero //= int(input("ingrese el segundo numero: "))
    print("La respuesta", numero)
elif numero == 4:
    numero = int(input("ingrese el primer numero: "))
    numero -= int(input("ingrese el segundo numero: "))
    print("La respuesta", numero)
elif numero == 5:
    numero = int(input("ingrese el primer numero: "))
    numero **= int(input("ingrese el exponente numero: "))
    print("La respuesta es: ", numero)
elif numero == 6:
    numero = int(input("ingrese el primer numero: "))
    numero %= int(input("ingrese el segundo numero: "))
    print("El residuo: ", numero)
elif numero == 7:
    numero = int(input("ingrese el primer numero: "))
    numero *= int(input("ingrese el segundo numero: "))
    print("La respuesta", numero)
else:
    print("No existe la opcion.")