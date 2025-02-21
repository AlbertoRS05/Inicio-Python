# La política de cobro de una compañía telefónica es: cuando se realiza una 
# llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros 
# cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos,
# los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
# Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno
# de mañana, 15 %, y en turno de tarde, 10 %. 
# Realice un algoritmo para determinar cuánto debe pagar por cada concepto 
# una persona que realiza una llamada.

tiem=int(input("Cuánto dura la llamada?: "))
dom=input("Hoy es domingo? (S/N): ")

if dom.upper()=="N":
    turno = input("Lo llamas de mañana o de tarde?(M/T): ")

if tiem <= 5:
    precio=tiem*1
else:
    if tiem < 8:
        precio=(tiem - 5) * 0.8+500
    else:
        if tiem < 10:
            precio= (tiem - 8) * 0.7+2.4+5
        else:
            precio= (tiem - 10) * 0.5+1.4+2.4+5

if dom.upper()=="S":
    precio=precio+precio*0.03
else:
    if turno == "M":
        precio=precio+precio*0.15
    elif turno == "T":
        precio=precio+precio*0.1
    else:
        print("Valor no válido")

print(f"El costo total es de {precio}")