import csv
from helper import *


def main():
	
	print('Gracias por usar el programa Concurso de Tiro')

	print('Ingreso de participantes al concurso')
	listaDeParticipantes=participantesLista()

	print('Informe del concurso Tiro al Blanco\n')
	
	mostrarGanador(listaDeParticipantes)
	mostrarPerdedor(listaDeParticipantes)
	participantes(listaDeParticipantes)
	cantidadMujeres(listaDeParticipantes)
	edadPromedioHombres(listaDeParticipantes)
	promedioDisparos(listaDeParticipantes)
	promedioMejoresDisparos(listaDeParticipantes)

	createCSV(listaDeParticipantes)
	print('\nGracias! => Realizado por Anderson')



main()
