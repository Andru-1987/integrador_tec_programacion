
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
		empleado['antiguedadBono']=valorBono(empleado.get('antiguedadEmpleado'))*empleado.get('sueldoBasico')

		listaEmpleados.append(empleado)

	return listaEmpleados


def cantidadEmpelados(listaEmpleados):
	print("Cantidad de empleados cargados: "+ len(listaEmpleados))

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



	
