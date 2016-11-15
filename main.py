#-*- coding: utf-8 -*-
from Tkinter import *
from recursos import *
from funciones import *


VIVOS = CreadorAlumnos()
MUERTOS = 0
CreadorAmistades()
CreadordeDia()
ordenarDatos()

SO1,SO2,EN1,EN2,FO1,FO2,PO1,PO2=0,0,0,0,0,0,0,0
def iniciardia():
	fila="Alumnos en Fila: {0}"
	with open("Alumnos.txt") as of:
		VIVOS=len(of.readlines())
	MUERTOS = 0
	df,dt,da=0,0,0
	f=0;t=0;atr=0
	rsop1.configure(text=qsop1.get())
	rsop2.configure(text=qsop2.get())
	rens1.configure(text=qent1.get())
	rens2.configure(text=qent2.get())
	rfond1.configure(text=qpf1.get())
	rfond2.configure(text=qpf2.get())
	rpos1.configure(text=qpst1.get())
	rpos2.configure(text=qpst2.get())
	SO1,SO2,EN1,EN2,FO1,FO2,PO1,PO2=map(int,[qsop1.get(),qsop2.get(),qent1.get(),qent2.get(),qpf1.get(),qpf2.get(),qpst1.get(),qpst2.get()])
	for x in range(0,150):
		h=MinutoaTiempo(x)
		hr.configure(text=h)
		if COLARSE.get()==1:
			FilaColandose(h)
		else:
			FilaNormal(h)
		atr,(f,t),(SO1,SO2,EN1,EN2,FO1,FO2,PO1,PO2) = ProcesarHora(h,int(apm.get()),(SO1,SO2,EN1,EN2,FO1,FO2,PO1,PO2))
		da+=atr
		df+=f
		dt+=t
		qf_hoy.configure(text=df)
		qa_hoy.configure(text=da)
		lf=ProcesarHambre()
		fl.configure(text=fila.format(lf))
		m=EliminarPorHambre()
		MUERTOS+=m
		VIVOS-=m
		qvivos.configure(text=VIVOS)
		qmuertos.configure(text=MUERTOS)
		rsop1.configure(text=SO1)
		rsop2.configure(text=SO2)
		rens1.configure(text=EN1)
		rens2.configure(text=EN2)
		rfond1.configure(text=FO1)
		rfond2.configure(text=FO2)
		rpos1.configure(text=PO1)
		rpos2.configure(text=PO2)
		lfil.configure(text=Visualizar())
		ventana.update()


ventana = Tk(className="Simulador Fila de Almuerzo")

secframe = Frame(ventana)
controles = Frame(secframe)
dia = Label(controles,text="Controles del Dia");dia.pack()
inciar = Button(controles, text="INICIAR",fg="green", command=iniciardia).pack(side=LEFT)
almlabel = Label(controles, text="  Almuerzos x minuto: ").pack(side=LEFT)
apm = Entry(controles);apm.pack(side=LEFT)
COLARSE=IntVar()
colcheck = Checkbutton(controles,text="Colarse",onvalue=1,offvalue=0,variable=COLARSE);colcheck.pack(side=LEFT)
controles.pack(side=TOP)
alimframe=Frame(secframe)
dia = Label(alimframe,text="Cantidad alimentos del Dia").grid(row=0,columnspan=3)
comida = Label(alimframe,text="Comidas").grid(row=1,column=0)
typ1 = Label(alimframe,text="Tipo 1").grid(row=1,column=1)
ryp2 = Label(alimframe,text="Tipo 2").grid(row=1,column=2)

sop = Label(alimframe, text="Sopa",fg="yellow");sop.grid(row=2,column=0)
ent = Label(alimframe, text="Entradas",fg="green");ent.grid(row=3,column=0)
pf = Label(alimframe, text="Platos de fondo");pf.grid(row=4,column=0)
pst = Label(alimframe, text="Postre",fg="green");pst.grid(row=5,column=0)

qsop1 = Entry(alimframe);qsop1.grid(row=2,column=1)
qent1 = Entry(alimframe);qent1.grid(row=3,column=1)
qpf1 = Entry(alimframe);qpf1.grid(row=4,column=1)
qpst1 = Entry(alimframe);qpst1.grid(row=5,column=1)
qsop2 = Entry(alimframe);qsop2.grid(row=2,column=2)
qent2 = Entry(alimframe);qent2.grid(row=3,column=2)
qpf2 = Entry(alimframe);qpf2.grid(row=4,column=2)
qpst2 = Entry(alimframe);qpst2.grid(row=5,column=2)
alimframe.pack(side=BOTTOM)
secframe.pack()

stframe = Frame(ventana)
data  = Label(stframe,text="Datos del Dia").grid(row=0,column=0)
hrl  = Label(stframe,text="Hora :").grid(row=0,column=1)
hr  = Label(stframe,text="");hr.grid(row=0,column=2)
fl  = Label(stframe,text="");fl.grid(row=0,column=3)
vivos = Label(stframe,text="Estudiantes Vivos: ").grid(row=1,column=0)
muertos = Label(stframe,text="Estudiantes Muertos: ").grid(row=2,column=0)
f_hoy = Label(stframe,text="Felices Hoy : ").grid(row=3,column=0)
a_hoy = Label(stframe,text="Atrasos de Hoy : ").grid(row=4,column=0)
qvivos =Label(stframe,text="");qvivos.grid(row=1,column=1)
qmuertos =Label(stframe,text="");qmuertos.grid(row=2,column=1)
qf_hoy =Label(stframe,text="");qf_hoy.grid(row=3,column=1)
qa_hoy =Label(stframe,text="");qa_hoy.grid(row=4,column=1)
stframe.pack()
qtframe = Frame(ventana)
lsop1 = Label(qtframe,text="Sopa 1 : ").grid(row=0,column=0)
lsop2 = Label(qtframe,text="Sopa 2 : ").grid(row=1,column=0)
lens1 = Label(qtframe,text="Ensalada 1 : ").grid(row=2,column=0)
lens2 = Label(qtframe,text="Ensalada 2 : ").grid(row=3,column=0)
lfond1 = Label(qtframe,text="Fondo 1 : ").grid(row=0,column=2)
lfond2 = Label(qtframe,text="Fondo 2 : ").grid(row=1,column=2)
lpos1 = Label(qtframe,text="Postre 1 : ").grid(row=2,column=2)
lpos2 = Label(qtframe,text="Postre 2 : ").grid(row=3,column=2)
rsop1 = Label(qtframe,text=" ");rsop1.grid(row=0,column=1)
rsop2 = Label(qtframe,text=" ");rsop2.grid(row=1,column=1)
rens1 = Label(qtframe,text=" ");rens1.grid(row=2,column=1)
rens2 = Label(qtframe,text=" ");rens2.grid(row=3,column=1)
rfond1 = Label(qtframe,text=" ");rfond1.grid(row=0,column=3)
rfond2 = Label(qtframe,text=" ");rfond2.grid(row=1,column=3)
rpos1 = Label(qtframe,text=" ");rpos1.grid(row=2,column=3)
rpos2 = Label(qtframe,text=" ");rpos2.grid(row=3,column=3)
qtframe.pack()
lfil=Label(ventana,fg="blue",text="")
lfil.pack()
ventana.mainloop()
