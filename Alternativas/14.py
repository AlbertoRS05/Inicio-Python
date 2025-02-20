# La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, 
# la cual se clasifica en tipos A y B,  y además en tamaños 1 y 2. 
# Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño, 
# se requiere determinar cuánto recibirá un productor por la uva que entrega en un 
#embarque, considerando lo siguiente: 
# si es de tipo A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2. 
# Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2. 
# Realice un algoritmo para determinar la ganancia obtenida.

precio_ini=int(input("Cuánto cuestan las uvas de base?(centimos): "))
tipo=input("De qué tipo es la uva?: ")
tam=int(input("Y el tamaño?: "))
kilos = int(input("Cuántos kilos entregará el productor?: "))

if tipo=="A":
    if tam==1:
        precio_ini = precio_ini + 20
        print(f"La ganancia es de {precio_ini} cent");
    elif tam==2:
        precio_ini = precio_ini + 30
        print(f"La ganancia es de {precio_ini} cent");
    else:
        print("Solo hay dos tamaños de uva");
elif tipo=="B":
    if tam==1:
        precio_ini = precio_ini - 30
        print(f"La ganancia es de {precio_ini} cent");
    elif tam==2:
        precio_ini = precio_ini - 50
        print(f"La ganancia es de {precio_ini} cent");
    else:
        print("Solo hay dos tamaños de uva");
else:
    print("Solo hay tipo A y tipo B")

gana=precio_ini*kilos
print(f"Y las ganancias obtenidas son de {gana} €")