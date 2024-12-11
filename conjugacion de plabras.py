# Metodo swapcase
#En esta opcion lo que hace esta lineas de codigo es que coloca las primeras letras en mayusculas y demas en minusculas poniendo la variable
#y despues la funcion .swapcase
tex_lower_up = "lA gEKKIPEDIA"
print(tex_lower_up.swapcase())
"""En esta funcion lo que realizamos es que las letras minusculas las vuelve mayusculas y las mayusculas minusculas al igual que 
en la funcion naterior"""
tex_lower = "letras en mayusculas"
print(tex_lower.swapcase())
"""En esta parte se realiza lo mismo solo que se cambia las letras por mayuscualas para ver como funciona"""
tex_min = "LETRAS EN MINUSCULAS"
print(tex_min.swapcase())
#Solo funciona con lines de texto no aplica en enteros os signos 
Exepcion = "123 ! * -"
print(Exepcion.swapcase())

print()

print(tex_lower_up)
print(tex_lower)
print(tex_min)
print(Exepcion)
#En esta parte usamos Capitalize para realizar bien el texto y colocarlo como normalmente lo conocemos 
String = "eL ViaJe es La Rencompenza"
print(f"la cadena de texros sin capitalize (): {String}")
String = String.capitalize()
print(f"La cadena de texto de pues de capitalize(): {String}")