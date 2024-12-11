"""esta parte del codigo es una concatenacion sin cambiar el nombre de la variable como se muestra
en la parte del codigo a contunuacion"""
mensaje = 'hola'
mensaje += ' '
mensaje += 'Ernesto'
print(mensaje)
"""aqui podemos ver como en el ejemplo anterior una concatenacion pero la diferencia es que aqui podemos ver
que la concatenacion la realizamos cambinado el nombre de las variables y al momento de imprimir en pantalla
concatenamos simando las variables """
print("concatenacioin:" )
mensaje = "hola"
espacio = "  "
nombre = "ernesto"
print(mensaje + espacio + nombre)
""" podemos hacer lo mismo con numeros pero a diferencia de los anteriores la suma de 2 numeros temos que convertilos
en datos de tipo string como en el ejemplo anterior vemos la concatenacion de dos variables de tipo int pero al momento de
realizar la concatenacion en la variable resultado pero marca error si no lo convertimos en un dato de tipo STR
por lo cual con el mismo nombre de la variable solo ponemos que es igual a un dato STR"""
num_1=2
num_2=2
resulado = num_1 + num_2
resulado = str(resulado)
print("resultado de la suma es: " + resulado)
"""en esta parte atra vez de un metodo llamado .find podemos buscar una parte de la cadena de texto colocando entre parentesis
la poarte de la cadena que buscamos como en el ejemplo"""
print("busqueda: ")
mensaje = "hoola Hernesto"
buscar_subcadena = mensaje.find("Hernesto")
print("buscar subcadena: ", buscar_subcadena)
"""la comparacion la utiliazamos colocando 2 signos iguales en vez de 1 solo y al momento de imprimir pantalla nos dira si es un valor verdadero o falso """
print("comparacion:")
mensaje_1 = "hola"
mensaje_2 = "holii"
print(mensaje_1 == mensaje_2)
""" en la abstraccion podemos solo mandar a imrpimir ciertas letras de la cadena colocnado entre corchetes de que pocicion a que pocicion queremos imprimir
 en pantalla sierta seccion de la cadena """
print("abstraccion")
mensaje_3 = "hola"
extraccion= mensaje_3[1:3]
print(extraccion)
