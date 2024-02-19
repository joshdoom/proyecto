from tkinter import *
from tkinter import ttk
import tkinter as tk
import customtkinter

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
loginlabel.place(x=170, y=150)
loginlabel.configure(font=("Calisto Mt", 30, "bold"))

username_label = Label(raiz, text="Usuario:", bg="white")
username_label.place(x=250, y=280)
username_label.config(font=("Calisto Mt", 18, "bold"))

username_entry = customtkinter.CTkEntry(master=raiz, width=150, height=30, border_width=0, corner_radius=10,
                                       font=(0, 16))
username_entry.place(x=185, y=300)


password_label = Label(raiz, text="Contraseña:", bg="white")
password_label.place(x=233, y=400)
password_label.config(font=("Calisto Mt", 18, "bold"))

password_entry = customtkinter.CTkEntry(master=raiz, width=150, height=30, border_width=0, corner_radius=10,
                                       font=(0, 16))
password_entry.place(x=185, y=450)
password_entry.config(show="*")

#botoninicio = tk.PhotoImage(file='C:\\Users\\USUARIO\\Downloads\\Nueva carpeta\\login\\disenos\\botoninicio.png')
login_button =customtkinter.CTkButton(master=raiz, width=160, height=40, text="botoninicio", fg_color="#fff",
                                              text_color="#000", hover_color="#999", command=ray, font=(0, 20))
login_button.place(x=95, y=520)

fondoright= Frame(raiz)
fondoright.pack()
imagenfondo2= tk.PhotoImage(file='C:\\Users\\USUARIO\\Downloads\\Nueva carpeta\\login\\disenos\\mejorescuela2.png')
imagenfondoright = tk.Label(loginFrameright, image=imagenfondo2)
imagenfondoright.pack()

raiz.mainloop()
