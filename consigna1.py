from helpers import*



def main():
	import os
	print('Consigna #1 Ingreso de empleados, con el valor de sueldo básico = 0 se finaliza la carga de empleados')

	
	listaEmpleados=ingresoEmpleado()
	# Esta es una lista de prueba
	# listaEmpleados=[{'sueldoBasico': 1000.0, 'edadEmpleado': 22, 'sexoEmpleado': 'f', 'antiguedadEmpleado': 20, 'antiguedadBono': 300.0},
	#  {'sueldoBasico': 10000.0, 'edadEmpleado': 23, 'sexoEmpleado': 'm', 'antiguedadEmpleado': 3, 'antiguedadBono': 1000.0}, 
	#  {'sueldoBasico': 40000.0, 'edadEmpleado': 34, 'sexoEmpleado': 'm', 'antiguedadEmpleado': 1, 'antiguedadBono': 4000.0},
	#  {'sueldoBasico': 30000.0, 'edadEmpleado': 44, 'sexoEmpleado': 'f', 'antiguedadEmpleado': 34, 'antiguedadBono': 9000.0}]


	mensaje='Opcion 1: Informe de cantidad de empleados'+'\nOpcion 2: Informe de sueldo básico promedio'+'\nOpcion 3: Informe promedio de antigüedad de los empleados'+'\nOpcion 4: Informe del porcentaje de mujeres trabajando'+'\nOpcion 5: Informe del sueldo total promedio'+'\nOpcion 6: Informe del sueldo más alto'+'\nOpcion 7: Informe del empleado más viejo y más joven'+'\nOpcion 8: Salir del programa'
	print(mensaje)
	opcion=input('Ingrese su opcion: ')

	while True:
		if opcion=='8':
			print('Gracias por usar el programa!=>Hecho por Anderson')
			break
		elif opcion=='1':
			cantidadEmpleados(listaEmpleados)
		elif opcion=='2':
			sueldoBasicoPromedio(listaEmpleados)
		elif opcion=='3':
			antiguedadPromedio(listaEmpleados)
		elif opcion=='4':
			mujeresEmpleados(listaEmpleados)
		elif opcion=='5':
			sueldoTotalPromedio(listaEmpleados)
		elif opcion=='6':
			sueldoAlto(listaEmpleados)
		elif opcion=='7':
			empleadoEdades(listaEmpleados)
		else:
			print('No entiendo lo ingresado')

		opcion=input('Ingrese su opcion: ')
		os.system('clear')
		print(mensaje)

main()