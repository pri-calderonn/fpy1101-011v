#Evaluacion2

#cada camion lleva 450k de gas y por camion es 765.000
import time
import os
clean="cls"
os.system(clean)

producto=0
camion=0

cilindro1=0 #es 12 cilindros de 5k
cilindro2=0 # 20 cilindros de 15 k 
cilindro3=0 #2cilindros de 45k

kg5=0
kg15=0
kg45=0

kg= kg5+kg15+kg45 

total1=1
total2=765000
adicional=1


while True:
    volver=""
    try: 
        print("Bienvenido")
        nombre=input("Ingrese su nombre: ")
        contacto=int(input("Ingrese su número de contacto"))
        
    except ValueError:
        print("Valor invalido")
        os.system(clean)
        time.sleep(1)
        continue
    
    
    print("Selecciona una opcion: ")
    print("1-Camion estandar ")
    print("2-Carga especifica")
    print("3.Imprimir boleta y cerrar pedido")
    
    total=cilindro1*kg5+cilindro2 * kg15 +cilindro3 * kg45 
    opcion=int(input("Selecciona una opcion"))
    try:
        if opcion==1:
            print("Has escogido el camion estandar")
            camion=int(input("cuantos camiones quieres agregar?"))
            total2 = total2 * camion
        
            
            print(f"en total seria: {total2}")
    except ValueError:
        print("Valor invalido")
        os.system(clean)
        time.sleep(1)
        continue

    while True:
    
        if opcion==2:
            print("1.cilindro 5kg \n2.cilindro 15kg \n3.cilindro 45kg \4 pagar")
            total=(cilindro1*kg5)+(cilindro2 * kg15)+(cilindro3 * kg45) 
            menu2=f"llevas la cantidad de {producto} cilindros con un total de {total} kg"
            print(menu2)
            try:
                opcion1=int(input("Selecciona una opcion 1-4"))
            
                if opcion1==1:
                    producto+=1
                    cilindro1+=1
                    kg5+=5
                    continue
                elif opcion1==2:
                    producto+=1
                    cilindro2+=1
                    kg15+=15
                    continue
                elif opcion1==3:
                    producto+=1
                    cilindro3+=1
                    kg45+=45
                    continue
                elif opcion==4:
                    print()
                else:
                    print("Debe ser un valor valido")
            except ValueError:
                    print("Valor invalido")
                    continue
        elif opcion==3:
            print()
            time.sleep(1)
                
            
        
            os.system(clean)
        time.sleep(1)
        
    
    
    
        
        
    
            
    
        print(f"Cliente : {nombre}")
        print(f"Telefono: {contacto}")
        print(f"Cantidad de kilos: {kg}")
        print(f"Camiones: {camion}")
        print(f"Valor Total : ${total}")
    
    
    
    
    
    
            
        
        
