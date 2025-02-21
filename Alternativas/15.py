# El director de una escuela está organizando un viaje de estudios, y requiere 
# determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de 
# viajes por el servicio. La forma de cobrar es la siguiente: 
# si son 100 alumnos o más, el costo por cada alumno es de 65 euros; 
# de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, 
# y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos. 
# Realice un algoritmo que permita determinar el pago a la compañía de autobuses 
# y lo que debe pagar cada alumno por el viaje.

num_alu=int(input("Cuántos alumnos van?: "))
if num_alu <= 0:
    print("Solo se pueden insertar número positivos")

else:
    if num_alu >= 100:
        costo=65
        costo_total=costo * num_alu
        print(f"El costo por {num_alu} alumnos es de {costo} individual y de {costo_total} en total");
    elif num_alu < 100 and num_alu >= 50:
        costo=70
        costo_total=costo * num_alu
        print(f"El costo por {num_alu} alumnos es de {costo} individual y de {costo_total} en total");
    elif num_alu < 50 and num_alu >= 30:
        costo=95
        costo_total=costo * num_alu
        print(f"El costo por {num_alu} alumnos es de {costo} individual y de {costo_total} en total");
    elif num_alu < 30:
        costo_total=4000/num_alu
        print(f"El costo por {num_alu} alumnos es de {costo_total} en cada uno");
