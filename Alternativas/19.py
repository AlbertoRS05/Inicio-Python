# Escribe un programa que pida un número entero entre uno y doce e imprima el 
# número de días que tiene el mes correspondiente.
#  Si introducimos otro número nos da un error.

mes=int(input("Elija un número del 1 al 12: "))

if mes < 1 or mes > 12:
    print("ERROR: No hay más de 12 meses")
else:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        dias=31
        print(f"El mes número {mes} tiene {dias}")

    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dias=30
        print(f"El mes número {mes} tiene {dias}")

    elif mes == 2:
        dias=28
        print(f"El mes número {mes} tiene {dias}")