#-*- coding: utf-8 -*- 
from random import randint,triangular,choice

statusdict={
	100:"😄 ",80:"😊 ",70:"😐 ",60:"😕 ",50:"😡 ",
	40:"😣 ",30:"😦 ",20:"😨 ",10:"😱 ",	0:"😵 "
}
statusdict2={
	10:"▁", #<10
	20:"▂",	#10 >= X <20
	30:"▃",	#20 >= X <30
	40:"▄", #30 >= X <40
	50:"▅", #40 >= X <50
	60:"▆", #50 >= X <60
	80:"▇", #60 >= X <80
	100:"█"  #80 >= X <=100
}

def MinutoaTiempo(mins):
	return ":".join(map(lambda n:[str(n),"0{0}".format(n)][n<10],[11+(mins%60>=30)+int(mins)/60,int(mins)%60+(30*(-1)**(mins%60>=30))]))
	
def TiempoaMinuto(tiempo):
	return int(tiempo.split(":")[0])*60+int(tiempo.split(":")[1])-11*60-30

#Nombre Apellido Apellido;SOPpreferida;ENSpreferida;PFpreferido;POSpreferido;Clases2;Tiempocomer;Hambretot/Hambreact
def CreadorAlumnos():
	with open("NombresApellidos.txt") as of:
		nombres=map(lambda q: q.capitalize() ,of.readline().strip().split(","))
		apellidos=map(lambda q: q.capitalize() ,of.readline().strip().split(","))
		LN=len(nombres)-1;LA=len(apellidos)-1
		lista=[" ".join([nombres[randint(0,LN)],apellidos[randint(0,LA)],apellidos[randint(0,LA)]]) for x in xrange(2000)]
		alumnos=[x+";"+";".join(map(str,[randint(1,2),randint(1,2),randint(1,2),randint(1,2),choice(["SI","NO"]),randint(10,30)])) for x in lista]
		alumnos=[x+";"+"/".join(map(str,[randint(15,90)]*2)) for x in alumnos]
	with open("Alumnos.txt","w") as wf:
		map(lambda nom: wf.write(nom+"\n"),alumnos)
	return len(alumnos)

def CreadorAmistades():
	with open("Alumnos.txt") as rf:
		als=rf.readlines()
	als=[x.split(";")[0] for x in als]
	cant=len(als)
	with open("Amistades.txt","w") as wf:
		for alu in als:
			amigs=set([als[randint(0,cant-1)] for x in range(randint(0,8))])
			map(lambda q: wf.write(alu+"->"+q+"\n"),[n for n in amigs if n!=alu])
def CreadordeDia():
	#desde 11:30 a 14:00 hay 150 min.
	with open("Alumnos.txt") as of:
		als=of.readlines()
	als=[x.split(";")[0] for x in als]
	horas = [MinutoaTiempo(round(triangular(0,150))) for x in range(len(als))]
	with open("Entrada.txt","w") as wf:
		map(lambda n:wf.write(als[n]+"#"+horas[n]+"\n"), range(len(als)))
	fila=open("Fila.txt","w");fila.close()

CreadorAlumnos()
CreadorAmistades()
CreadordeDia()

#Revision de TM(MT(x))
#for x in range(10000):
#	if x==TiempoaMinuto(MinutoaTiempo(x)):
#		continue
#	else:
#		print "DUH"
