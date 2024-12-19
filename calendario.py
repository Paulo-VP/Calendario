from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import calendar
import locale


root=""
botones=[]    
options=[]
notas=[]
fecha = datetime.now()
ventanaFechas=""
ventanaAgregar=""

def verNotas():
    try:
        tareas = []
        with open('notas.txt', 'r') as archivo:
                for linea in archivo:
                    if(linea.strip()!=""):
                        date, note = linea.strip().split('|')
                        tareas.append({"fecha":datetime.strptime(date, "%d-%m-%Y %H:%M"),"nota":note})
    except:
        with open('C:/Users/solo_/Desktop/New folder/notas.txt', 'w') as archivo:
            archivo.write('')
    mostrarNotas(tareas)

def ventanaNota(fecha):
    global ventanaAgregar
    ventanaAgregar = Toplevel(root)
    ventanaAgregar.resizable(False, False) 
    ventanaAgregar.title("Fechas")
    ventanaAgregar.focus_set()
    labelFecha=Label(ventanaAgregar,text="Especificar hora")
    labelFecha.grid(row=0,column=0,columnspan=4)
    labelHora=Label(ventanaAgregar,text="Hora: ")
    labelHora.grid(row=1,column=0,pady=5)
    comboHora = ttk.Combobox(ventanaAgregar)
    comboHora.grid(row=1,column=1,pady=5)
    comboHora['values']=list(range(24))
    comboHora.current(12)
    labelMinuto=Label(ventanaAgregar,text="Minuto: ")
    labelMinuto.grid(row=1,column=2,pady=5)
    comboMinuto = ttk.Combobox(ventanaAgregar)
    comboMinuto.grid(row=1,column=3,pady=5)
    comboMinuto['values']=list(range(60))
    comboMinuto.current(0)
    labelFecha=Label(ventanaAgregar,text="Especificar tarea")
    labelFecha.grid(row=2,column=0,columnspan=4)
    areaTexto = Text(ventanaAgregar,height = 5,width = 50,bg = "light yellow")
    areaTexto.grid(row=3,column=0,columnspan=4,pady=5, padx=5)
    botonCancelar=Button(ventanaAgregar,text="Cancelar",command= lambda ventana=ventanaAgregar:ventana.destroy())
    botonCancelar.grid(row=4,column=0,columnspan=2)
    botonGuardar=Button(ventanaAgregar,text="Guardar",command=lambda hora=comboHora,minuto=comboMinuto,texto=areaTexto: agregarNota(fecha+" "+str(hora.current())+":"+str(minuto.current()),texto.get("1.0",'end-1c')))
    botonGuardar.grid(row=4,column=2,columnspan=2)

def agregarNota(fecha,tarea):
    global ventanaAgregar
    try:
        fecha=datetime.strptime(fecha, "%d-%m-%Y %H:%M")
        if(ventanaAgregar):
            ventanaAgregar.destroy()
        if(tarea):
            with open('notas.txt', 'a') as archivo: 
                archivo.write(fecha.strftime("%d-%m-%Y %H:%M")+"|"+tarea.replace("\n"," ")+"\n")
        verNotas()
    except:
        pass

def DibujarCalendario(year,month):    
    global root
    global botones
    if(month==13):
        month=1
        year+=1
    elif(month==0):
        month=12
        year-=1
    for boton in botones:
        boton.grid_forget()
    botones.clear()
    calendario = calendar.monthcalendar(year,month)
    botonL = Button(root, text="<",width=3, height=2,command=lambda year=year,month=month-1:DibujarCalendario(year,month))
    botonL.grid(row=0, column=0)
    botones.append(botonL)
    labelFecha = Label(root, text=calendar.month_name[month].capitalize()+" ("+str(month)+"/"+str(year)+")", height=2, font=(15))
    labelFecha.grid(row=0, column=1,columnspan=6)
    botones.append(labelFecha)
    botonC = Button(root, text="c",width=4, height=2,command=lambda year=year,month=month:cambiarFecha(year,month))
    botonC.grid(row=0, column=7)
    botones.append(botonC)
    botonR = Button(root, text=">",width=3, height=2,command=lambda year=year,month=month+1:DibujarCalendario(year,month))
    botonR.grid(row=0, column=8)
    botones.append(botonR)
    for i,semana in enumerate(calendario):
        for j,dia in enumerate(semana):
            if(dia!=0):
                if(datetime.strptime(str(year)+"-"+str(month)+"-"+str(dia), '%Y-%m-%d').date()<datetime.now().date()):
                    boton = Button(root, text=str(dia),fg="red" ,width=10, height=3, state=DISABLED)
                    boton.grid(row=i+2, column=j+1)
                else:
                    boton = Button(root, text=str(dia),width=10, height=3,command=lambda dia=dia:ventanaNota(str(dia)+"-"+str(month)+"-"+str(year)))
                    boton.grid(row=i+2, column=j+1)
            else:
                boton = Button(root, text="",width=10, height=3, state=DISABLED)
                boton.grid(row=i+2, column=j+1)
            botones.append(boton)

def cambiarFecha(year,month):
    global fecha   
    global options 
    global ventanaFechas
    ventanaFechas = Toplevel(root)
    ventanaFechas.resizable(False, False) 
    ventanaFechas.title("Fechas")
    ventanaFechas.focus_set()
    years = fecha.date().year-1
    labelAños = Label(ventanaFechas, text="Años", width=10, height=2)
    labelAños.grid(row=0)
    options.clear()
    for i in range(4):
        boton = Button(ventanaFechas,text=years+i, width=15, height=3,command=lambda year=years+i:cambioOpcion(year))
        boton.grid(row=1, column=i)
        if(year==years+i):
            boton.config(state=DISABLED)
        options.append(boton)
    labelMeses = Label(ventanaFechas, text="Meses", width=10, height=2)
    labelMeses.grid(row=2)
    for i in range(3):
        for j in range(4):
            boton = Button(ventanaFechas,text=calendar.month_name[((i*4)+j)+1].capitalize(), width=15, height=3,command=lambda month=(((i*4)+j)+1):cambioOpcion(month))
            boton.grid(row=i+3, column=j)
            if(month==((i*4)+j)+1):
                boton.config(state=DISABLED)
            options.append(boton)

def cambioOpcion(cambio):
    aux=[]
    for i,option in enumerate(options):
        if(option.cget("state") == "disabled"):
            aux.append(i) 
    if(cambio<13):
        options[aux[1]].config(state=NORMAL)
        options[cambio+3].config(state=DISABLED)
        DibujarCalendario(aux[0]+fecha.year-1,cambio)
    else:
        options[aux[0]].config(state=NORMAL)
        options[cambio-fecha.year+1].config(state=DISABLED)
        DibujarCalendario(cambio,aux[1]-3)

def mostrarNotas(tareas):
    global root
    global notas
    total_filas, _ = root.grid_size()
    for nota in notas:
        nota.grid_forget()
    notas.clear()
    frameTareas=Frame(root)
    frameTareas.grid(row=total_filas-1, column=1, columnspan=7,sticky='nsew')
    notas.append(frameTareas)
    tareas_ordenadadas = sorted(tareas, key=lambda x: x["fecha"])
    for i,tarea in enumerate(tareas_ordenadadas):
        frameTarea=Frame(frameTareas)
        frameTarea.grid(row=i, column=0,sticky='nsew')
        notas.append(frameTarea)
        texto=str((tarea["fecha"].date()-fecha.date()).days)+" días restantes"
        labelTiempo=Label(frameTarea,text=texto,fg="red",width=15, anchor='w')
        labelTiempo.grid(row=0, column=0,sticky='w')
        notas.append(labelTiempo)
        labelTarea=Label(frameTarea,text=tarea["fecha"].strftime('%Y-%m-%d %H:%M')+"\t"+tarea["nota"])
        labelTarea.grid(row=0, column=1, columnspan=4,sticky="ew")
        notas.append(labelTarea)
    
def on_focus_in(event):
    global ventanaFechas
    global ventanaAgregar
    if(ventanaFechas):
        ventanaFechas.destroy()
    if(ventanaAgregar):
        ventanaAgregar.destroy()

def main(fecha):
    global root
    root = Tk()
    root.bind("<FocusIn>", on_focus_in)
    root.title("Calendario")
    root.resizable(False, False) 
    for i in range(7):
        labelDias = Label(root, text=calendar.day_name[i].capitalize(), width=10, height=3)
        labelDias.grid(row=1, column=i+1)
    DibujarCalendario(fecha.year,fecha.month)
    verNotas()
    root.mainloop()
    
if __name__=="__main__":
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    main(fecha.date())

