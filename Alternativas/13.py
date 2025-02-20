# Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.
dia=int(input("Dime un día: "))
mes=int(input("Dime un mes: "))
year=int(input("Dime un año: "))

if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
    num_dias=31;
elif mes==4 or mes==6 or mes==9 or mes==11:
    num_dias=30;
elif mes==2:
    num_dias=28;
else:
    print("No hay ni más ni menos que 12 meses")

if dia<=0 or dia>num_dias:
    print("Número introducio no válido");
else:
    print(f"Seleccionaste el día {dia} del mes {mes} del año {year}")