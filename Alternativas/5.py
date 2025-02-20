# Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido "pepe" y "1234" se indica "Has entrado al sistema", sino se da un error.

nombre=input("Introduzca su nombre de usuario: ")
passw=int(input("Y una contraseña: "))

if nombre == "pepe" and passw == 1234:
    print("Bienvenido pepe")
else:
    print("Lo siento pero no tienes acceso")