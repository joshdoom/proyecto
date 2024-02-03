import tkinter
from tkinter import Tk, messagebox
from sqlalchemy.orm import Session
from ..models import Usuario
from ..engine import engine


def screen_login(tk: tkinter, window: Tk):
    def login():
        from .index import screen_index

        username = username_entry.get()
        password = password_entry.get()

        with Session(engine) as session:
            users = session.query(Usuario).all()
            for user in users:
                if username == user.nombre and password == user.contrasena:
                    window.destroy()
                    screen_index(tk, window=Tk())
                    return
            else:
                messagebox.showinfo("Error", "Usuario o contraseña es incorrecta")
    
    window.title("Iniciar Sesión")
    window.geometry("400x600")
    window.resizable(0,0)

    loginFrame = tk.Frame(window)
    loginFrame.pack()

    titulo = tk.Label(loginFrame, text="Iniciar Sesión", font=("Helvetica", 18))
    titulo.pack(pady=20)

    username_label = tk.Label(loginFrame, text="Usuario:", font=("Helvetica", 14))
    username_label.pack(pady=10)

    username_entry = tk.Entry(loginFrame, font=("Helvetica", 12))
    username_entry.pack(pady=10)

    password_label = tk.Label(loginFrame, text="Clave:", font=("Helvetica", 14))
    password_label.pack(pady=10)

    password_entry = tk.Entry(loginFrame, show="*", font=("Helvetica", 12))
    password_entry.pack(pady=10)

    login_button = tk.Button(loginFrame, text="Entrar", command=login, font=("Helvetica", 14), bg="white")
    login_button.pack(pady=20)