from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3 

def primero():    
    from grado1 import primero
    primero()

def segundo():    
    from grado2 import Segundo
    Segundo()

def tercero():    
    from grado3 import Tercero
    Tercero()

def cuarto():    
    from grado4 import Cuarto
    Cuarto()    

def quinto():    
    from grado5 import Quinto
    Quinto()
    
def profesores():    
    from profesores import profesor
    profesor()    

class iniciar():
    raiz = tk.Tk()
    raiz.title("Ventana Pincipal")
    raiz.geometry("400x600")
    raiz.resizable(0,0)    
    loginFrame=Frame(raiz)        
    loginFrame.pack() 

    botomio=Button(loginFrame, text="Primer año",command=primero)
    botomio.pack()
    botomio=Button(loginFrame, text="Segundo año",command=segundo)
    botomio.pack() 
    botomio=Button(loginFrame, text="Tercer año",command=tercero)
    botomio.pack() 
    botomio=Button(loginFrame, text="Cuarto año",command=cuarto)
    botomio.pack() 
    botomio=Button(loginFrame, text="Quinto año",command=quinto)
    botomio.pack()   
    botomio=Button(loginFrame, text="Profesores",command=profesores)
    botomio.pack() 

    raiz.mainloop() 