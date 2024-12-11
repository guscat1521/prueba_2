string = "menu"
print("Metodos con espacios")
print(string.center(20 ))
print(string.ljust(20 ))
print(string.rjust(20 ))

print("Metodos con un caracter ")
print(string.center(20 , "="))
print(string.ljust(20 , "="))
print(string.rjust(20 , "="))

print("modificacion de la variable ")
string = string.center(20 , "=")
print(string)