#asignamos una variable
mensaje = "hola "
# tambien se asigna una variable pero la diferencia es que esta se puede agregar desde teclado y se agrega a la variable sin nececidad de crear una nueva variable
mensaje += input(" ingresa tu nombre: \n")
### imprimimos la variable con el print
print(mensaje, ", esto es el incremento o decremento de una variable \n ")

# se inicia un nuevo proyecto o programa 
print("Incremento o aumento")
# se crea la variable numero la cual va aguardar el numero 1
numero = 1
# imprimimos el valor de numero sin ningun cambio 
print("El valor inicial de x es: ",numero,)
# agregamos 4 nuevos valores a la variable la cual va funcionar como una suma de numeros pero en caso de palabras se agregan las palabras oletras al parrafo 
numero += 1
numero += 1
numero += 1
numero += 1
# imprimimos el valor de numero ya con el cambio realizado lo cual deveria mostrar un valor de 5
print("El valor con incremento de x es: ",numero,)

# en esta parte se realiza la misma actividad solo cambiando el echo de que en la anterior fue un incremento y en esta vamos hacer un decremento o resta
# para regresar a su valor inicial y re repite el procesos 
print(" \n dicremento o disminucion")
print("El valor inicial de x es: ",numero,)
numero -= 1
numero -= 1
numero -= 1
numero -= 1
print("El valor con dicremento de x es: ",numero,)
"""NOTA=== El codigo se va ejecutando como lo vayas creando de arriba para abajo si quieres imprimir los
procesos o operaciones se tiene que hacer despues del bucle o operacion"""
