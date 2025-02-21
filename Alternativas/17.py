# Realiza un programa que pida por teclado el resultado (dato entero) obtenido 
# al lanzar un dado de seis caras y muestre por pantalla el número en letras 
# (dato cadena) de la cara opuesta al resultado obtenido.
# * Nota 1: En las caras opuestas de un dado de seis caras están los números: 
# 1-6, 2-5 y 3-4.
# * Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, 
# se mostrará el mensaje: "ERROR: número incorrecto.".

result=float(input("Cuál es el resultado del dado?: "))

if result < 1 or result > 6:
    print("ERROR: número incorrecto")
else:
    if result == 1:
        print("6")
    elif result == 2:
        print("5")
    elif result == 3:
        print("4")
    elif result == 4:
        print("3")
    elif result == 5:
        print("2")
    elif result == 6:
        print("1")