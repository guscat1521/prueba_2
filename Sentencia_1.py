print("sistemas para calcular el promedio de un alumno")
nombre = input("ingresa tu nombre: ")
print("Hola " + nombre + " esta aplicacion calcula tu calificacion")
Cal_1 = int (input("ingresa tu primera calificacion: "))
Cal_2 = int(input("ingersa tu segunda calificacion: "))
Cal_3 = int(input("ingresa tu tercer calificacion: "))
Promedio = (Cal_1 + Cal_2 + Cal_3) / 3
Promedio =  int(Promedio)
if Promedio >= 6 :
    print('pasate de pura suerte ' + nombre + ' "aprobaste :) ', Promedio)

else :
    print("lo siento " + nombre + " reprovaste con ", Promedio)
print("adios")

