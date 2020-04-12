estatura = float(input("Digite la estatura\n"))
acomu_estatura = 0
cont_personas = 0
prom = 0

while estatura >= 1.0 and estatura <= 3.0 :
	estatura = float(input("Digite la estatura\n"))
	cont_personas = cont_personas + 1
	acomu_estatura = acomu_estatura + estatura
	prom = acomu_estatura / cont_personas

else:
	print("El promedio de las estaturas es:",prom)