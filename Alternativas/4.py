# Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.

num1=int(input("Elija un número: "))
num2=int(input("Elija otro número: "))

if num2 == 0:
    print("Error, se puede dividir entre 0")
else:
    print(f"El resultado de su división es {num1/num2}")