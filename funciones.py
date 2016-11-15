	# Integrantes:
# Rut Nombre
#
#

from recursos import *

def ordenarDatos():
	#dicAlumnos
	#Nombre_Alumno : [Sopa, Entrada, Fondo, Postre, Clases, Tiempo, HambreMaxima, HambreActual, [Amigos], Ingreso]
	#Ingreso	= 0 # Si el alumno no llega a la fila
	#			= 1 # Si el alumno ya llego a la fila
	#			= 2 # Si el alumno ya ingreso al comedor

	arch = open("Alumnos.txt")
	global dicAlumnos
	dicAlumnos = {}
	for alumno in arch:
		nombre, sop, entr, fondo, post, clases, tiempo, hambre = alumno.strip().split(";")
		hambMax, hambAct = hambre.split("/")
		dicAlumnos[nombre] = [sop, entr, fondo, post, clases, tiempo, hambMax, hambAct, [], 0]
	arch.close()

	arch = open("Amistades.txt")
	for linea in arch:
		estudiante1, estudiante2 = linea.strip().split("->")
		dicAlumnos[estudiante2][8].append(estudiante1)
	arch.close()

def FilaColandose(hora):

	return None

def FilaNormal(hora):
	arch = open("Entrada.txt") #Abrir archivo ENTRADA en modo LECTURA
	hora = tuple(map(int,hora.split(":"))) #Convertir la hora entregada en tupla
	fila = [] #Crear lista vacia para guardar datos
	for linea in arch: #Recorrer archivo por linea
		nombre, hora_llegada = linea.strip().split("#") #Desempaquetar linea
		hora_llegada = tuple(map(int,hora_llegada.split(":"))) #Convertir hora de llegada en tupla
		if hora_llegada <= hora: #Verifica si la persona ya llego a esa hora
			if dicAlumnos[nombre][9] != 2:
				fila.append([hora_llegada, nombre]) #Agrega a la persona a la lista de la fila
				dicAlumnos[nombre][9] = 1 #Cambia el estado del alumno a que esta en la fila
	arch.close() #Cierra archivo
	fila.sort() #Ordenar la fila por hora de llegada
	arch = open("Fila.txt", "w") #Abrir archivo FILA en modo ESCRITURA
	for alumno in fila: #Recorrer la fila ordenada
		arch.write(alumno[1]+"\n") #Escribir el nombre del alumno
	arch.close() #Cerrar el archivo
	return None

def ProcesarHora(hora, cantidad, comida):
	print "Hora:", hora
	print "Cantidad de estudiantes", cantidad
	print "Comida:", comida
	comida = list(comida) #La tupla comida se transforma a tupla para poder editarla
	arch = open("Fila.txt")
	i = 0 #Contador
	for linea in arch:
		if i < cantidad:
			nombre = linea.strip()
			dicAlumnos[nombre][9] =  2
			###Se Reunen los gustos y se dejan entre 0 y 1
			sopa = int(dicAlumnos[nombre][0]) -1
			entrada = int(dicAlumnos[nombre][1]) -1
			fondo = int(dicAlumnos[nombre][2]) -1
			postre = int(dicAlumnos[nombre][3]) -1

			orden = -2
			### Checkea si hay de lo que gusta comer disponible
			for alimento in (sopa, entrada, fondo, postre):
				orden += 2
				if comida[alimento + orden] == 0: #Si no quedan alimentos preferidos
					if comida[((alimento+1)%1)+orden] != 0: #Pero quedan de las otros
						comida[((alimento+1)%1)+orden] -= 1 #Se resta un alimento de los otros
					else: #Si no queda ningun alimento
						pass #No se hace nada
				else: #Si queda alimento preferido
					comida[alimento + orden] -= 1

		else: # Si se supero el numero de ingresos por hora se cierra el ciclo
			break

			i += 1 #Aumenta el contador
	arch.close()
	return 0, (0,0), tuple(comida)

def ProcesarHambre():

	return 0

def EliminarPorHambre():

	return 0

def Visualizar():

	return ''
