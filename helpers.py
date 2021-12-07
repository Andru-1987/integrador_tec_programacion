
def notEmpty(numero):
# Ingresa valores en string y retorna un int
    import re

    # Permite valores positivos
    user_format=re.compile(r'^[0-9]*$')
    valido=re.match(user_format,numero)

    while valido==None:
        numero=input('Ingrese un valor correcto\n')
        valido=re.match(user_format,numero)

    return int(numero)


def sexoEmpleado(sexo):

	sexo=sexo.lower()

	while sexo=='' or sexo!='m' and not sexo=='f': 
		sexo=input('Ingrese un valor correcto\n').lower()

	return sexo


def edadEmpleado(edad):

	while edad<1 or edad>100:
		edad=int(input("Ingrese una edad válida: "))

	return edad

def antiguedadEmpleado(antiguedad):

	while antiguedad<1 or antiguedad>100:
		antiguedad=int(input("Ingrese una antiguedad válida: "))

	return antiguedad

def sueldoBasico(sueldo):

	while sueldo<0:
		sueldo=float(input("Ingrese valor válido: "))

	return sueldo


def valorBono(antiguedad):

	# funcion selectora de bono por antiguedad

	if antiguedad>=1 and antiguedad<=5:
		valorBono=0.10
	elif antiguedad>5 and antiguedad<=10:
		valorBono=0.20
	else:
		valorBono=0.30
	return valorBono



def ingresoEmpleado():
	
	listaEmpleados=[]

	while True:

		idEmpleado=str(len(listaEmpleados)+1)
		empleado={}

		empleado['sueldoBasico']=sueldoBasico(float(input("Ingrese el sueldo básico del empleado #"+ idEmpleado+": $" )))
	
		if empleado.get('sueldoBasico')==0:
			print("Se completó la carga de empleados")
			break
		empleado['edadEmpleado']=edadEmpleado(int(input("Ingrese la edad(años): ")))
		empleado['sexoEmpleado']=sexoEmpleado(input("Ingrese el sexo del empleado(M o F): "))
		empleado['antiguedadEmpleado']=antiguedadEmpleado(int(input("Ingrese su antiguedad: ")))
		
		# se guarda directamente como item dentro del diccionario del empleado

		empleado['antiguedadBono']=valorBono(empleado.get('antiguedadEmpleado'))*empleado.get('sueldoBasico')

		listaEmpleados.append(empleado)

	return listaEmpleados


def cantidadEmpleados(listaEmpleados):
	print("Cantidad de empleados cargados: "+ str(len(listaEmpleados)))

def sueldoBasicoPromedio(listaEmpleados):

	cantEmpleados=len(listaEmpleados)
	sumaTotal=0
	for empleado in listaEmpleados:
		sumaTotal+=empleado.get('sueldoBasico')


	if len(listaEmpleados)==0:
		print('No hay empleados cargados')
	else:
		promedio=sumaTotal/cantEmpleados
		print('El sueldo promedio es: '+ str(promedio))


def antiguedadPromedio(listaEmpleados):

	cantEmpleados=len(listaEmpleados)
	sumaTotal=0
	for empleado in listaEmpleados:
		sumaTotal+=empleado.get('antiguedadEmpleado')


	if len(listaEmpleados)==0:
		print('No hay empleados cargados')
	else:
		promedio=sumaTotal/cantEmpleados
		print('La antiguedad promedio es: '+ str(promedio) +' años.')


def mujeresEmpleados(listaEmpleados):

	resultado=len(list(filter(lambda x: x['sexoEmpleado']=='f',listaEmpleados)))
	if resultado==0:
		print('No hay mujeres cargadas en nuestro sistema')
	else:

		print('Promedio de mujeres trabajando : ' +str(resultado*100/len(listaEmpleados))+' %')

def sueldoTotalPromedio(listaEmpleados):
	sueldoTotal=0
	if len(listaEmpleados)!=0:
		for empleado in listaEmpleados:
			sueldoTotal+=empleado['sueldoBasico']+empleado['antiguedadBono']

		print('Promedio de sueldo total: '+str(sueldoTotal/len(listaEmpleados)))

	else:
		print('No existen registros insertados')

def sueldoAlto(listaEmpleados):
	
	if len(listaEmpleados)!=0:
		sueldoTotalMax=listaEmpleados[0]['sueldoBasico']+listaEmpleados[0]['antiguedadBono']	 

		for empleado in listaEmpleados:
			sueldoTotal=empleado['sueldoBasico']+empleado['antiguedadBono']	 
			if sueldoTotal>sueldoTotalMax:
				sueldoTotalMax=sueldoTotal
		print('Sueldo total máximo es: '+str(sueldoTotalMax))
	else:
		print('No existen registros insertados')


def empleadoEdades(listaEmpleados):
	
	if len(listaEmpleados)!=0:
		edadMax=listaEmpleados[0]['edadEmpleado']
		edadMin=listaEmpleados[0]['edadEmpleado']

		for empleado in listaEmpleados:
			if (valor:=empleado.get('edadEmpleado'))>edadMax:
				edadMax=valor
			if (valor:=empleado.get('edadEmpleado'))<edadMin:
				edadMin=valor

		print('Edad del empleado más viejo: '+str(edadMax)+' años'+'\nEdad del empleado más joven: '+str(edadMin)+' años')
	else:
		print('No existen registros insertados')




	
