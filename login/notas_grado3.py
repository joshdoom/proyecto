import sqlite3 
from tkinter import *
from tkinter import ttk
import tkinter as tk



class Tercero:
        root = Tk()        
        root.title("Tercer año")
        root.geometry("1280x680")      
        root.config(bd=20)
        root.resizable(False, False)

        miFrame=Frame(root)
        miFrame.pack()  
        miFrame.config(width="1200", height="250")
        miFrame.config(bd=5)
        miFrame.config(relief="groove")
      
        botoneliminar=Button(root, text="Nuevo")
        botoneliminar.pack()
        botoneliminar.config(bg="white")
        botoneliminar.config(fg="black")
        botoneliminar.place(x=600, y=210)
       
    
        botonnuevo=Button(root, text="Guardar")
        botonnuevo.pack()
        botonnuevo.config(bg="white")
        botonnuevo.config(fg="black")
        botonnuevo.place(x=800, y=210)
        
  
    
        botonguardar=Button(root, text="Eliminar")
        botonguardar.pack()
        botonguardar.config(bg="white")
        botonguardar.config(fg="black")
        botonguardar.place(x=700, y=210)
       

        miFrame13=Frame(root)
        miFrame13.pack(side="bottom", anchor="w")
      
        miFrame13.config(width="1200", height="350")
        miFrame13.config(bd=1)
       

        botoneditar=Button(miFrame13, text="Editar")        
        botoneditar.pack()
        botoneditar.config(bg="white")
        
       
        milabel= Label(miFrame, text="Valor de nota:")
        milabel.place(x=150, y=0)  

        cuadrotexto=Entry(root)
        cuadrotexto.place(x=255, y=7)
       

        milabel2= Label(miFrame, text="procentaje de nota:")
        milabel2.place(x=150, y=50)

        cuadrotexto2=Entry(root)       
        cuadrotexto2.place(x=285, y=55)

        milabel= Label(miFrame, text="Total de la nota:")
        milabel.place(x=150, y=100) 

        cuadrotexto=Entry(root)
        cuadrotexto.place(x=265, y=107)

       
       
        miFrame2=Frame(root)
        miFrame2.pack(fill="y", expand="true")
        miFrame2.pack(side="bottom")
        miFrame2.config(bg="white")
        miFrame2.config(width="1400", height="350")

        
        miFramemenu=Frame(root)
        miFramemenu.pack()
        miFramemenu.config(width="10", height="35")
        miFramemenu.config(bd=1)
        miFramemenu.place(x=1010, y=210)
        miFramemenu.config(relief="raised")

        var = StringVar(miFramemenu)
        var.set ("Materias")
        opciones=["Castellano","Ciencias Biologicas","Fisica","Quimica","Geografía, historia y ciudadanía (GHC)","Ingles","Matematicas","Orientación y convivencia ","Participación en grupos de creación, recreación y producción (G.E.R.P)"]
        opcion=OptionMenu(miFramemenu, var, *opciones)
        opcion.config(width=15)
        opcion.config(bg="white")
        botonguardar.config(fg="black")
        botoneditar.config(font=("Arial Black", 10))
        opcion.pack()

        miFramemenulapso=Frame(root)
        miFramemenulapso.pack()
        miFramemenulapso.config(width="10", height="35")
        miFramemenulapso.config(bd=1)
        miFramemenulapso.place(x=1010, y=170)
        miFramemenulapso.config(relief="raised")

        var = StringVar(root)
        
        var.set ("lapsos")
        opciones=["Primer lapso","Segundo lapso","Tercer lapso"]
        opcion=OptionMenu(miFramemenulapso, var, *opciones) 
        opcion.place(x=1000,y=210)       
        opcion.config(width=15)
        opcion.config(bg="white")
        botonguardar.config(fg="black")
        botoneditar.config(font=("Arial Black", 10))
        opcion.pack()

        root.mainloop()
      