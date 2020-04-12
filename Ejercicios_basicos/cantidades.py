numero = 1
cantnume = 0
cantnumeronega = 0
while numero != 0:
    numero = float(input("digite numero\n"))
    if numero > 0:
        cantnume = cantnume + 1
    elif numero < 0:
        cantnumeronega = cantnumeronega + 1
else:      
      print("Cantidad de numeros positivos",cantnume)
      print("Cantidad de numeros negativos",cantnumeronega)
