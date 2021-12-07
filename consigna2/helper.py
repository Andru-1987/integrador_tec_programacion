# funciones
def tiroAlTablero(x,y):
    import math
    distancia=round(math.sqrt(x**2+y**2),2)
    return distancia

def validarNumero(numero):
    import re
    # Permite valores positivos
    user_format=re.compile(r'^[0-9]*$')
    valido=re.match(user_format,numero)

    while valido==None or numero=='':
      numero=input('Ingrese data valida ')
      valido=re.match(user_format,numero)

    return int(numero)

def validarNumeroString(numero):
    import re
    # Permite valores positivos
    user_format=re.compile(r'^[0-9]*$')
    valido=re.match(user_format,numero)

    while valido==None or numero=='':
      numero=input('Ingrese data valida ')
      valido=re.match(user_format,numero)

    return int(numero)

def cadena(string):
    import re
    # Ingreso de letras

    user_format=re.compile(r'^[A-z_Ññ]*$')
    valido=re.match(user_format,string)

    while valido==None or string=='':
      string=input('Ingrese data válida ')
      valido=re.match(user_format,string)

    return string


def validarID(ID,listaDeParticipantes):

	listaID=[]
	for participante in listaDeParticipantes:
		listaID.append(participante['id'])

	while True:
		if ID not in listaID:
			break
		else:
			ID=validarNumeroString(input('Ingrese otro ID: '))

	return ID



def participantesLista():

	listaDeParticipantes=[]

	while True:

		participante={}
		disparo=[]

		idParticipante=validarNumeroString(input('Ingrese #ID participante: '))
		participante['id']=validarID(idParticipante,listaDeParticipantes)

		if participante.get('id')==999:
			print('Carga de datos terminada')
			break

		participante['nombre']=cadena(input('Ingrese nombre: ')).lower().capitalize()
		participante['apellido']=cadena(input('Ingrese apellido: ')).lower().capitalize()
		participante['edad']=validarNumero(input('Ingrese edad: '))
		participante['sexo']=input('Ingrese sexo "h/m":' ).lower()

		for i in range(2):
			print('Ingrese coordenadas de disparo '+ str(i+1))
			disparoX=validarNumero(input('Coordenada X: '))
			disparoY=validarNumero(input('Coordenada Y: '))

			shot=tiroAlTablero(disparoX,disparoY)
			disparo.append(shot)

		participante['disparo']=disparo

		# cual es el mejor disparo
		mejorShot=lambda x: x[0] if x[0]<x[1] else x[1]

		participante['mejorDisparo']=mejorShot(disparo)
		listaDeParticipantes.append(participante)

	return listaDeParticipantes



def mostrarGanador(listaDeParticipantes):
    # Punto1
    maxValue=listaDeParticipantes[0].get('mejorDisparo')
    nombre=listaDeParticipantes[0].get('nombre')
    apellido=listaDeParticipantes[0].get('apellido')

    for n in listaDeParticipantes:
        if n['mejorDisparo']<maxValue:
            nombre=n['nombre']
            apellido=n['apellido']
            mejorDisparo=n['mejorDisparo']


    print(f'El ganador fue {apellido}, {nombre} y la distancia a su disparo fue de: {mejorDisparo}')


def mostrarPerdedor(listaDeParticipantes):
    
    peorDisparo=listaDeParticipantes[0].get('mejorDisparo')
    nombre=listaDeParticipantes[0].get('nombre')
    apellido=listaDeParticipantes[0].get('apellido')

    for n in listaDeParticipantes:
        if n['mejorDisparo']>peorDisparo:
            nombre=n['nombre']
            apellido=n['apellido']
            peorDisparo==n['mejorDisparo']

    print(f'El perdedor fue {apellido}, {nombre} y la distancia a su disparo fue de: {peorDisparo}')

def participantes(listaDeParticipantes):
    # Punto3
    cantidadParticipantes=len(listaDeParticipantes)
    print(f'Cantidad de participantes en el concurso : {cantidadParticipantes}')


def cantidadMujeres(listaDeParticipantes):

    accumulador=0
    for n in listaDeParticipantes:
        if n.get('sexo')=='m':
            accumulador+=1
    if accumulador==0:
        print('No hubo hombres en el concurso')
    else:
        print(f'Cantidad de participantes de sexo femenino: {accumulador}')

def edadPromedioHombres(listaDeParticipantes):
    
    contHombres=0
    accEdad=0

    for n in listaDeParticipantes:
        if n.get('sexo')=='m':
          contHombres+=1
          accEdad+=n.get('edad')

    if contHombres==0:
        print('No hubo hombres en el concurso')
    else:
        promedioEdad=round(float(accEdad/contHombres),2)
        print(f'El promedio de edad en hombres es de : {promedioEdad}')

def promedioDisparos(listaDeParticipantes):
   
    
    accValorDisparos=0

    for n in listaDeParticipantes:
      accValorDisparos+=(n['disparo'][0]+n['disparo'][1])
  
    promedio=round(float(accValorDisparos/(len(listaDeParticipantes)*2)),2)
    print(f'El promedio de valor en los disparos fue de: {promedio}')


def promedioMejoresDisparos(listaDeParticipantes):
    
    
    accValorDisparos=0

    for n in listaDeParticipantes:
      accValorDisparos+=n.get('mejorDisparo')
  
    promedio=round(float(accValorDisparos/len(listaDeParticipantes)),2)
    print(f'El promedio de valor en los disparos fue de: {promedio}')



