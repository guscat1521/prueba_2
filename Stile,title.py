firs_name = input("Nombre: ")
Last_name = input("Apaellido: ")
full_name = f"{firs_name} {Last_name}"

print("")
print(f"¿El formato title se ha aplicado? {full_name.istitle()}")
print("")
print(f"Aqui mostramos ya aplicado el metodo title: {full_name.title()}")
print(f"Volvemos a imprimir el nombre: {full_name}" )
print("")

full_name = full_name.title()
print(f"¿El formato title se ha aplicado? {full_name.istitle()}")
print(f"Se a aplicado correctamento el metodo title {full_name}")

# islower y lower

full_name = full_name.islower()
print(full_name)

Taco = "la Gikippedia"
Taco = Taco.lower()
print(Taco)

#isupper y upper 
Taco = Taco.upper()
print (Taco)
Taco = Taco.isupper()
print (Taco)
# para cambiar el contenido de la variable se coloca el nombre de la varibale y la variables ejemplo para mejor comprencion
# Taco = taco.metodod() se modifica
# print (taco.metodod()) no se modifica