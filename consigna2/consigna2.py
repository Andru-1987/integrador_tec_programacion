import csv
from helper import *


def main():
	
	dateConcurso=input('Bienvenido\nIngrese el año del concurso\n')
	print('Gracias por usar el programa Concurso de Tiro del año: '+dateConcurso)
	
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

	createCSV(listaDeParticipantes,dateConcurso)
	print('\nGracias! => Realizado por Anderson')



main()
