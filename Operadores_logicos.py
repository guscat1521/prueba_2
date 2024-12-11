#Conjuncion
print("Conguncion (and)")
num_uno = int(input("escribe un numero mayor a 2 y menor a 5: "))
if num_uno > 2 and num_uno < 5:
    print("El numero ", num_uno, " cumple con la condicion. \n")
else:
    print("El numero ", num_uno, " no cumple la condicion. \n")


#Disyuncion (OR)
print("Disyuncion(or)")
palabra = input("para cumplir la condicion escribe 'si' o 'yes' : ")
if palabra == "si" or palabra == "yes":
    print(" la condicion se ha cumplido.\n")
else:
    print(" la condicion no se ha cumplido \n")



#Negacion
print("negacion (not)")

num_uno= int(input(" introducce un numero igual a 5: "))
if not num_uno == 5:
    print("\n El numero es diferente de cinco y si se cumple la condicion \n")
else:
    print(" \n El numero es igual a cinco y no cumple la condicion ")




