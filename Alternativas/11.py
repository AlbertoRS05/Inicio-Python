# Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. 
# El programa debe determinar que tipo de triángulo es, teniendo en cuenta:
# Si se cumple Pitágoras entonces es triángulo rectángulo
# Si sólo dos lados del triángulo son iguales entonces es isósceles.
# Si los 3 lados son iguales entonces es equilátero.
# Si no se cumple ninguna de las condiciones anteriores, es escaleno.

ladA=int(input("Cual es A?: "))
ladB=int(input("Cual es B?: "))
ladC=int(input("Cual es C?: "))

if ladA**2 + ladB**2 == ladC**2:
    print("Este triángulo es rectángulo")
elif ladA == ladB and ladA != ladC or ladB == ladC and ladB != ladA or ladA == ladC and ladA != ladB:
    print("Es un triángulo isóceles")
elif ladA == ladB == ladC:
    print("Triángulo equilátero")
else:
    print("Triángulo escaleno")