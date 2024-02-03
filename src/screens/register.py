import tkinter
from tkinter import Tk, messagebox
from sqlalchemy.orm import Session
from ..models import Usuario
from ..services.register import Usuario as UsuarioService
from ..engine import engine


def screen_register(tk: tkinter, window: Tk):
    connect = UsuarioService(engine)

    def register():
        from .login import screen_login

        username = username_entry.get()
        password = password_entry.get()
        rol_select = rol.get()
        question = pregunta_entry.get()
        answer = respuesta_entry.get()

        try:
            connect.create(username, password, rol_select, question, answer)
            window.destroy()
            screen_login(tk, window=Tk())
        except:
            messagebox.showinfo("Error", "Usuario o contraseña es incorrecta")
    
    window.title("Registrar")
    window.geometry("400x600")
    window.resizable(0,0)

    registerFrame = tk.Frame(window)
    registerFrame.pack()

    titulo = tk.Label(registerFrame, text="Registrar", font=("Helvetica", 18))
    titulo.pack(pady=20)

    username_label = tk.Label(registerFrame, text="Usuario:", font=("Helvetica", 14))
    username_label.pack(pady=10)

    username_entry = tk.Entry(registerFrame, font=("Helvetica", 12))
    username_entry.pack(pady=10)

    password_label = tk.Label(registerFrame, text="Clave:", font=("Helvetica", 14))
    password_label.pack(pady=10)

    password_entry = tk.Entry(registerFrame, show="*", font=("Helvetica", 12))
    password_entry.pack(pady=10)

    rol = tk.StringVar(registerFrame)
    rol.set("Rol")
    seleccionrol = ['Director', 'Profesor', 'Secretaria']
    opcion_rol = tk.OptionMenu(registerFrame, rol, *seleccionrol)
    opcion_rol.config(font=("Helvetica", 16))
    opcion_rol.pack(pady=10)

    pregunta_label = tk.Label(registerFrame, text="Pregunta de Seguridad:", font=("Helvetica", 14))
    pregunta_label.pack(pady=10)

    pregunta_entry = tk.Entry(registerFrame, font=("Helvetica", 12))
    pregunta_entry.pack(pady=10)

    respuesta_label = tk.Label(registerFrame, text="Respuesta:", font=("Helvetica", 14))
    respuesta_label.pack(pady=10)

    respuesta_entry = tk.Entry(registerFrame, show="*", font=("Helvetica", 12))
    respuesta_entry.pack(pady=10)

    register_button = tk.Button(registerFrame, text="Registrar", command=register, font=("Helvetica", 14), bg="white")
    register_button.pack(pady=20)