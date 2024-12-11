print("************************************************************************** \n")
print("              programa para elegir un numero mayor                         \n")
print("************************************************************************** \n")
"""Primero creamos unas variebles de tipo float para que ingresen un numero desde teclado bueno en este caso serian 3 numeros
y guardandolos en diferentes variables para poder utilizarlas en una comparacion """
numero_uno = float(input("Ingresa el primer numero: \n"))
numero_dos = float(input("Ingrese el segundo numero: \n"))
numero_tres = float(input("Ingrese el tercer numero: \n"))
"""En esta parte del codigo lo que realizamos es una condicion if utilizando un and para poder unir 
2 variables en la cual pide que si el numero dos y el numero uno son mayores a numero tres tienen que emprimir lo que se pide
 asi repetimos con las 3 posibles resultados colocando un elif el cual nos da la opcion de poner unas condicionantes para que tenga 
 mas opciones el ciclo y no se detenga el proceso en cambio realice una accion diferente """
if numero_uno > numero_dos and numero_uno > numero_tres:
    print("El numero ",int(numero_uno), " es mayor")
elif numero_dos > numero_uno and numero_dos > numero_tres:
    print("El numero ",int(numero_dos), " es mayor")
elif numero_tres > numero_uno and numero_tres > numero_dos:
    print("El numero ",int(numero_tres), " es mayor")
    