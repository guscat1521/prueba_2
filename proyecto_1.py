print("programa de asignacion de vacaciones, dependiendo el tiempo de antiguedad del empleado \n")
nombre = input("Ingresa el nombre del empleado: \n")
clave = int(input ("Ingresar la clave del empleado: \n"))
años = float( input("Ingresa los años que lleva trabajando el empleado: \n"))
if clave == 1:
    if años >= 1 and años < 2:
        print( " El empleado " , nombre , " le corresponden 6 dias de vaciones \n")
    elif años >=2 and años <=6 : 
        print( " El empleado " , nombre , " le corresponden 14 dias de vaciones \n")
    elif años >= 7 :
        print ( " El empleado " , nombre , " le corresponden 20 dias de vaciones \n")
    else:
        print( " El empleado " , nombre , " no tiene derecho a vacaciones \n")

elif clave == 2:
     if años >= 1 and años < 2:
        print( " El empleado " , nombre , " le corresponden 7 dias de vaciones \n")
    elif años >=2 and años <=6 :
        print ( " El empleado " , nombre , " le corresponden 15 dias de vaciones \n")
    elif años >= 7 :
        print ( " El empleado " , nombre , " le corresponden 22 dias de vaciones \n")
    else:
        print( " El empleado " , nombre , " no tiene derecho a vacaciones \n")


elif clave == 3:
     if años >= 1 and años < 2:
        print( " El empleado " , nombre , " le corresponden 10 dias de vaciones \n")
    elif años >=2 and años <=6 : 
        print( " El empleado " , nombre , " le corresponden 20 dias de vaciones \n")
    elif años >= 7 :
        print ( " El empleado " , nombre , " le corresponden 30 dias de vaciones \n")
    else:
        print( " El empleado " , nombre , " no tiene derecho a vacaciones \n")

    
else:
    print("\n la clave de este departamento no sirve")


    
