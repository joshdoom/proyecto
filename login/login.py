from tkinter import *
from tkinter import ttk
import tkinter as tk

def login():
    username = username_entry.get()
    password = password_entry.get()
   
    if username == "admin" and password == "123" or username == "a" and password == "a":   
        raiz.destroy()
        from inter import iniciar
        iniciar()   

raiz = Tk()
raiz.title("Login")
raiz.geometry("400x600")
raiz.resizable(0,0)
loginFrame=Frame(raiz)
loginFrame.configure(width="400", height="600")
loginFrame.pack()    

loginlabel= Label(loginFrame, text="Login")
loginlabel.pack()
loginlabel.place(x=170, y=0)
loginlabel.configure(font=("Calisto Mt", 18, "bold"))

username_label = Label(loginFrame, text="Usuario:")
username_label.pack()
username_label.place(x=40, y=400)
username_label.config(font=("Calisto Mt", 18, "bold"))

username_entry = Entry(loginFrame)
username_entry.pack()
username_entry.place(x=140, y=400)
username_entry.config(font=("Arial",15))

password_label = Label(loginFrame, text="Clave:")
password_label.pack()
password_entry = Entry(loginFrame)
password_entry.pack()
password_entry.place(x=140, y=500)
password_entry.config(font=("Arial",15))
password_entry.config(show="*")

password_label.place(x=40, y=500)
password_label.config(font=("Calisto Mt", 18, "bold"))

login_button = Button(loginFrame, text="Entrar", command=login)
login_button.pack()
login_button.place(x=140, y=550)
login_button.config(font=("Arial", 16))
login_button.config(bg= "white")

raiz.mainloop()