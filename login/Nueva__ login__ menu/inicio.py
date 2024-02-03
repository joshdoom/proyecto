from tkinter import *
from tkinter import ttk
import tkinter as tk

negro="#00292d"
verdeoscuro="#01212e"

def ray():
    raiz.destroy()
    from menu import todo
    

raiz = Tk()
raiz.title("Login")
raiz.geometry("1000x650")
raiz.resizable(0,0)
raiz.config(bg=verdeoscuro)

loginFrameright=Frame(raiz)
loginFrameright.configure(width="400", height="650")
loginFrameright.pack(side=RIGHT)

Framefondo=Frame(raiz)
Framefondo.pack()
fondo = tk.PhotoImage(file='C:\\Users\\USUARIO\\Downloads\\Nueva carpeta\\login\\disenos\\fono2.png')
imagenfondo = tk.Label(Framefondo,image=fondo)
imagenfondo.pack()

loginlabel= Label(raiz, text="Iniciar Sesion", bg="white")
loginlabel.pack()
loginlabel.place(x=170, y=150)
loginlabel.configure(font=("Calisto Mt", 30, "bold"))

username_label = Label(raiz, text="Usuario:", bg="white")
username_label.pack()
username_label.place(x=250, y=280)
username_label.config(font=("Calisto Mt", 18, "bold"))

username_entry = Entry(raiz)
username_entry.pack()
username_entry.place(x=185, y=340)
username_entry.config(font=("Arial",15))

password_label = Label(raiz, text="Contraseña:", bg="white")
password_label.pack()
password_label.place(x=233, y=400)
password_label.config(font=("Calisto Mt", 18, "bold"))

password_entry = Entry(raiz)
password_entry.pack()
password_entry.place(x=185, y=460)
password_entry.config(font=("Arial",15))
password_entry.config(show="*")

botoninicio = tk.PhotoImage(file='C:\\Users\\USUARIO\\Downloads\\Nueva carpeta\\login\\disenos\\botoninicio.png')
login_button = Button(raiz, image=botoninicio,command=ray)
login_button.pack()
login_button.place(x=95, y=520)

fondoright= Frame(raiz)
fondoright.pack()
imagenfondo2= tk.PhotoImage(file='C:\\Users\\USUARIO\\Downloads\\Nueva carpeta\\login\\disenos\\mejorescuela2.png')
imagenfondoright = tk.Label(loginFrameright, image=imagenfondo2)
imagenfondoright.pack()

raiz.mainloop()
