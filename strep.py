#metodo strip
#Para el metodo strip lo que hacemos es que lo usamos para poder eliminar cierto numero de letras de una variable de tipo String
"""Por ejemplo en esta parte declaramos la variable y agregamos  el inicio de la variable y donde termina para que sepa 
la accion strip de donde emepezar a buscar y borrar las letras"""
Cadena = "\t Hola Ernesto \n "
print(Cadena)
Cadena = Cadena.strip("s tHo \t \n")
print(Cadena)

#metodo rstrip
"""El metodo rstrip puede regresar las palabras borradas del metodo strip """
cadena = "\t Hola Hernesto \n"
print(cadena)
cadena = cadena.rstrip("s tHo \t \n")

#metodo lstrip
"""En esta parte solo solo se borra una vex falta recarlcar que con el metodo Strip repite el proceso varias veces hasta que se queda 
sin las letras que pediste buscar pero en el caso lStrip no solo  lo realiza 1 sola por ejemplo si ya encontro la primera H solo borra es
he ignora la que siga """
print(cadena)
cadena = cadena.lstrip("s tHo \t \n")
print(cadena)