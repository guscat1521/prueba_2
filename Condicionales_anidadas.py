print("=============================")
print("Conversor ")
print("============================= \n")
"""Para esta parte creamos un menu donde donde tenemos que elegir una opcion para poder convertir numeros a palabras y a la inversa"""
print("menu de opciones \n")
print("presiona 1 para convertir de numero a palabra")
print("presiona 2 para convertir de palabra a numero \n")
"""En esta parte lo que hicimos fue crear la varible opcion la cual va recibir el numero de tipo entero para poder
Elejir la opcion que quieras realizar con el prpgrama """
opcion = int(input("Cual es tu opcion deseada?: \n"))
#En esta parte utilizmos un ciclo if el cual va analizar el valor del la varible y con base a ello empezar a hacer las tareas 
if opcion == 1:
    print("\n Conversor de palabra a numero \n")
    """En esta parte dependiendo del numero que ingrese dara un resultado de las opciones elif
     teniendo de opcion del 1 al 5 repitiendo lo mismo en el siguinete bucle o opcion del menu """
    numero_1 = int(input("Ingresa el numero a convertir a palabra: "))
    if numero_1 == 1:
        print("El numero que deseas convertir a palabra es 'uno' ")
    elif numero_1 == 2:
        print("El numero que deseas convertir a palabra es 'Dos' ")
    elif numero_1 == 3:
        print("El numero que deseas convertir a palabra es 'Tres' ")
    elif numero_1 == 4:
        print("El numero que deseas convertir a palabra es 'Cuatro' ")
    elif numero_1 == 5:
        print("El numero que deseas convertir a palabra es 'Cinco' ")
    else:
        print("no se esncunetra la opcion disponibles")
    
elif opcion ==2:
    print("\n conversor de numeros a palabras \n")
    opc_1 = input("Ingresa la palabra a convertir a numero: ")
    opc_1 = opc_1.lower() 
    if opc_1 == "uno":
        print("El numero que deseas convertir a numero es ' 1 ' ")
    elif opc_1 == "dos":
        print("El numero que deseas convertir a numero es ' 2 ' ")
    elif opc_1 == "tres":
        print("El numero que deseas convertir a numero es ' 3 ' ")
    elif opc_1 == "cuatro":
        print("El numero que deseas convertir a numero es ' 4 ' ")
    elif opc_1 == "Cinco":
        print("El numero que deseas convertir a numero es ' 5 ' ")
    else:
        print(" La opcion no se encuetra disponibles ")
else :
    print("\n La opcion no esta disponible aun \n")
print("Fin")

    
