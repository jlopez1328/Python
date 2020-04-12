print("PARES E IMPARES")
numero_1 = 0
numero_2 = 100
multiplicador = 0
resultado = 0

for i in range(numero_1,numero_2 + 1):
    if i % 2 == 0:
        print(f"El numero {i} es par.")
        multiplicador = multiplicador + i
    else:
        print(f"El numero {i} es impar.")
        multiplicador = multiplicador + i
else:
	resultado = multiplicador * multiplicador
	print(f"el resultado es {multiplicador}\n")
	print(f"el resultado es {resultado}")
