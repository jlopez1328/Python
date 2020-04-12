numero = int(input("Cuantos valores va a introducir? "))

if numero <= 0:
        print("¡Imposible!")
else:
        suma = 0
        for i in range(1, numero + 1):
            valor = float(input("Escriba el numero : "))
            suma = suma + valor
        print("La suma de los numeros que ha escrito es ",suma)





