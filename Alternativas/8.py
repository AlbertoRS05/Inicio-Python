# Algoritmo que pida dos números 'nota' y 'edad' y un carácter 'sexo' 
# y muestre el mensaje 'ACEPTADA' si la nota es mayor o igual a cinco, 
# la edad es mayor o igual a dieciocho y el sexo es 'F'. 
# En caso de que se cumpla lo mismo, pero el sexo sea 'M', debe imprimir 'POSIBLE'. 
# Si no se cumplen dichas condiciones se debe mostrar 'NO ACEPTADA'.

nota = int(input("Dime la nota: "))
edad = int(input("Dime la edad: "))
sexo = input("Dime tu sexo (M/F): ")

if nota >= 5 and edad >= 18 and sexo == "F":
    print("ACEPTADA")
elif nota >= 5 and edad >= 18 and sexo == "M":
    print("POSIBLE")
else:
    print("NO ACEPTADA")