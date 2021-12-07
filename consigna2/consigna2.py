from helper import *


def main():
	
	print('Gracias por usar el programa Concurso de Tiro')

	print('Ingreso de participantes al concurso')
	# listaDeParticipantes=participantesLista()

	# Lista de pruebas

	listaDeParticipantes=[{'id': 1, 'nombre': 'Anderson', 'apellido': 'Ocaña', 'edad': 33, 'sexo': 'h', 'disparo': [49.65, 49.88],'mejorDisparo':10.2},{'id': 2, 'nombre': 'Julieta', 'apellido': 'Venegas', 'edad': 22, 'sexo': 'm', 'disparo': [31.14, 24.6],'mejorDisparo':24.6},{'id': 3, 'nombre': 'Miguel', 'apellido': 'Mateos', 'edad': 44, 'sexo': 'm', 'disparo': [33.0, 30.0],'mejorDisparo':33.0},{'id': 4, 'nombre': 'Lourdes', 'apellido': 'Achavallastra', 'edad': 40, 'sexo': 'm', 'disparo': [22.2, 30.0],'mejorDisparo':0.0}]

	print('Informe del concurso Tiro al Blanco\n')

	mostrarGanador(listaDeParticipantes)
	mostrarPerdedor(listaDeParticipantes)
	participantes(listaDeParticipantes)
	cantidadMujeres(listaDeParticipantes)
	edadPromedioHombres(listaDeParticipantes)
	promedioDisparos(listaDeParticipantes)
	promedioMejoresDisparos(listaDeParticipantes)

	print('\nGracias! => Realizado por Anderson')


main()