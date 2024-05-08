
op1=0
op2=0
op3=0
op4=0

totalpro= 0
producto=1
cantidad=1 


try:
    while producto==1:
        print("---Bienvenido---")
        print("Selecciona alguno de nuestros productos")
        print("1" , "Pikachu Roll", "4500" , sep= "-")
        print("2" , "Otaku Roll", "5000" , sep= "-")
        print("3" , "Pulpo Venenoso Roll", "5200" , sep= "-")
        print("4" , "Anguila Electrica Roll", "4800" , sep= "-")
        print("Para salir presione 0")

        
  
        if producto >= op1 :
            cantidad=int(input("Has seleccionado la opcion 1,cuantos deseas agregar ?: "))
            cantidad=cantidad*4500
        elif producto==op2:
            cantidad=int(input("Has seleccionado la opcion 2,cuantos deseas agregar ?: "))
            cantidad=cantidad*5000
        elif producto ==op3:
            cantidad=int(input("Has seleccionado la opcion 3,cuantos deseas agregar ?: "))
            cantidad=cantidad*5200
        elif producto==op4:
            cantidad=int(input("Has seleccionado la opcion 4,cuantos deseas agregar ?: "))
        cantidad=cantidad*4800
    else:
        print("desea agregar algo mas?")
except ValueError:
    print("opcion no valida,debe ser del 1-4")      



   

        
