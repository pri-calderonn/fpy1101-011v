
mientras1=1

mientras2=2

total=0

while mientras1!=5:
    print("---Bienvenido---")
    print("Selecciona alguno de nuestros productos")
    print("1" , "Pikachu Roll", "4500" , sep= "-")
    print("2" , "Otaku Roll", "5000" , sep= "-")
    print("3" , "Pulpo Venenoso Roll", "5200" , sep= "-")
    print("4" , "Anguila Electrica Roll", "4800" , sep= "-")
    print("Para salir presione 0")
    
    
    pedido=int(input("Que desea ordenar?"))
    
    if (pedido==1):
        valor=4500
        cant_pe=int(input("$4500 Cuantos desea ordenar?"))
        total=total+(valor*cant_pe)
        print(f"el total de su pedido es: {total}")
    elif (pedido==2):
        valor=5000
        cant_pe=int(input("$5000 Cuandos desea ordenar?"))
        total=total+(valor*cant_pe)
        print(f"el total de su pedido es: {total}")
    elif (pedido==3):
        valor=5200
        cant_pe=int(input("$5200 Cuandos desea ordenar?"))
        total=total+(valor*cant_pe)
        print(f"el total de su pedido es: {total}")
    elif (pedido==4):
        valor=4800
        cant_pe=int(input("$4800 Cuandos desea ordenar?"))
        total=total+(valor*cant_pe)
        print(f"el total de su pedido es: {total}")
        
    
    
        
    adicion=int(input("Desea ordenar algo mas? \n 1-Si \n 2-No"))
        
        
    if adicion==1:
            total=+1
            print(f"su total es {total}")
            
    


    

    cupon=int(input("Tiene cupon de descuento? \n 1-Si \n 2-No "))

    if cupon==1:
            codigo=input("Ingrese codigo de cupon")
            if codigo==("soyotaku"):
                total1=("total*100")
                total2=("total1/10")
                print(f"Tiene descuento del 10% total es: {total2}")
    elif cupon==2:
            print("Error de codigo")
            print("vuelve a inicio")
    
    adicion1=int(input("Desea ordenar algo mas? \n 1-Si \n 2-No"))
    if adicion1==1:
        continue
    break    
    
        

    

    



print("**********************************")
print(f"TOTAL DE PRODUCTOS: {pedido}")
print("**********************************")

print(f"pikachu Roll {1}")
print(f"Otaku Roll {2}")

print(f"Pulpo Venenoso Roll{3}")
print(f"Anguila Electrica Roll{4}")
print("***********************************")
    
print(f"total= {total2}")
    
    