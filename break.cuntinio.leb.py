#Ejemplo para break
"""imprimimos en consola para que funciona el programa en este caso vamos hacer una sentencia con While
la cual va tiene un valor inicial de 0 y debe de ir aumentando hasta que sea menor o igual a 10 Haciendo una suma de 1 en 1 aplicando 
un asignacion de suma pero agregando un condicion If la cual pide que cuando sea igual a 5 se detenga toda la sentancia 
asi explicamos que si la suma llega a resultado 5 termina el ciclo y ya no llega a 10 y despues imprimiemos el resultado """
print("Programa para ver la funcion de una instruccion break ")
contador = 0
while contador <= 10:
    contador += 1
    if contador == 5:
        break
    print("el valor actual de la variable es: ", contador)
print("Fin la sentencia break se ha cumplido ")



#Ejemplo de continue
"""En esta parte solo cambiamos la parte del break por continue lo cual hace que a diferencia del anterior en vez de parar el ciclo 
simplemente se salta ese resultado y continua hasta cumplir las condicones del ciclo """
print("\n Programa para ver la funcion de una instruccion continue \n ")
contador = 0
while contador < 10:
    contador += 1
    if contador == 5:
        continue
    print("el valor actual de la variable es: ", contador)
print("Fin la sentencia continue se ha cumplido ")



#Funcion len
#opcion 1
"""la Funcion len lo que hace es que cuenta la canridad de string que tiene la palabra que le ingresas o pider falta aberiguar si funciona 
tanbien con variables creo que si """
print(" \n hola, tiene: ", len("hola"), "caracteres")

longitud = len("longitud")
print("\n longitud, tiene", longitud, " caracteres" )