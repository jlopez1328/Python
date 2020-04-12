calificaciones = {'calculo': 10, 'dibujo': 2.5}
sumcalificaciones = calificaciones.get('calculo') + calificaciones.get('dibujo')
totalnota = sumcalificaciones / 3
print('\n', 'La nota de calculo es:', calificaciones.get('calculo'), '\n', 
	'La nota de dibujo es:', calificaciones.get('dibujo'), '\n',
	'El promedio total es:', totalnota, '\n')


print('La materia con mejor promedio  es:', calificaciones.get('calculo'))


