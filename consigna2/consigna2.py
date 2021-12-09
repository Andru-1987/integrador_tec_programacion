import csv
from helper import *


def main():
	
	dateConcurso=input('Bienvenido\nIngrese el año del concurso\n') or 'No Ingresado'
	print('Concurso de Tiro del año: '+dateConcurso)
	
	print('Ingreso de participantes al concurso')
	print('-------------- Termina la carga con 999 --------------')
	listaDeParticipantes=participantesLista()

	print('-------------- Informe del concurso --------------')
	
	mostrarGanador(listaDeParticipantes)
	mostrarPerdedor(listaDeParticipantes)
	participantes(listaDeParticipantes)
	cantidadMujeres(listaDeParticipantes)
	edadPromedioHombres(listaDeParticipantes)
	promedioDisparos(listaDeParticipantes)
	promedioMejoresDisparos(listaDeParticipantes)

	createCSV(listaDeParticipantes,dateConcurso)
	print('-------------- Fin --------------')
	print('\nGracias! => Realizado por Anderson')



main()
