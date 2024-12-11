print("Esta es una aplicacion para calcular una calificacion")
nombre=input("Ingresa tu nombre: ")
Matematicas = float(input("Ingresa tu calificacion de matematicas por favor:"))
Filosofia = float(input("Ingresa tu calificacion de filosofia por favor:"))
Aritmetica = float(input("Ingresa tu calificacion de aritmetica por favor:"))
Promedio =(Matematicas + Filosofia + Aritmetica) / 3

if Promedio >= 6 :
    print("'Felicidades " + nombre + " pasate con un promedio de' ", Promedio)
    print("'Felicidades " + nombre + " pasate con un promedio de' ",  round(Promedio, 2))
else :
    print (" lo siento " + nombre + " reprobaste con un promedio de ", Promedio)
    print(" lo siento "  + nombre + " reprobaste con un promedio de ",  round(Promedio, 1))
print('"adios"')
