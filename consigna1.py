from helpers import*


# Una empresa está solicitando un programa que pida el ingreso de
# 4 datos por teclado: 
# el sueldo básico de cada empleado, su edad, sexo y la antigüedad de cada uno 
# (expresado en años). El fin de ingreso se indica con sueldo básico = 0

# La empresa tiene la siguiente consideración por antigüedad:
# #  Antigüedad entre 1 y 5 años,
#  al sueldo básico se le suma un bono del 10% de su básico.
#  Antigüedad entre 5 y 10 años,
#  al sueldo básico se le suma un bono del 20% de su básico.
#  Antigüedades mayores a 11 años, se le suma un adicional de 30%.
# Se pide calcular e informar lo siguiente:

#  Informe la cantidad de empleados
#  Informe el sueldo básico promedio
#  Informe la antigüedad promedio de todos los empleados

#  Informe el porcentaje de mujeres trabajando
#  Informe el sueldo total promedio (básico + bono)
#  Informar el sueldo total más alto (básico + bono)
#  Informar el empleado más joven y el más viejo.
# Para el cálculo del sueldo + bono, 
# utilizar una función que reciba el sueldo básico y la antigüedad,
# y la misma retorne el sueldo total a percibir.



listaTest=[{'sueldoBasico': 1000.0, 'edadEmpleado': 22, 'sexoEmpleado': 'f', 'antiguedadEmpleado': 20, 'antiguedadBono': 300.0}, {'sueldoBasico': 10000.0, 'edadEmpleado': 23, 'sexoEmpleado': 'm', 'antiguedadEmpleado': 3, 'antiguedadBono': 1000.0}, {'sueldoBasico': 40000.0, 'edadEmpleado': 34, 'sexoEmpleado': 'm', 'antiguedadEmpleado': 1, 'antiguedadBono': 4000.0}, {'sueldoBasico': 30000.0, 'edadEmpleado': 44, 'sexoEmpleado': 'm', 'antiguedadEmpleado': 34, 'antiguedadBono': 9000.0}]


antiguedadPromedio(listaTest)
# def main():

# 	while true:
# 		if 