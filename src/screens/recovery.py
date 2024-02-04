import tkinter
from tkinter import Tk, messagebox
from sqlalchemy.orm import Session
from ..models import Usuario
from ..services.register import Usuario as UsuarioService
from ..engine import engine
def screen_recovery(tk: tkinter, window: Tk):
    connect = UsuarioService(engine)

    def check_user():
        user = username_entry.get()
        with Session(engine) as session:
            if session.query(Usuario).filter_by(nombre=user).first():
                recovery()
            else:
                tk.messagebox.showerror("Error", "Usuario no encontrado")

    def update():
        from .login import screen_login

        user = username_entry.get()
        answer = respuesta_entry.get()
        password = password_entry.get()

        with Session(engine) as session:
            user = session.query(Usuario).filter_by(nombre=user, respuesta_seguridad=answer).first()
            if user:
                connect.update(user.id, password)
                window.destroy()
                screen_login(tk, window=Tk())
            else:
                tk.messagebox.showerror("Error", "Usuario no encontrado")
    def recovery():
        global respuesta_entry
        global password_entry

        respuesta_label = tk.Label(registerFrame, text="Respuesta:", font=("Helvetica", 14))
        respuesta_label.pack(pady=10)

        respuesta_entry = tk.Entry(registerFrame, show="*", font=("Helvetica", 12))
        respuesta_entry.pack(pady=10)

        password_label = tk.Label(registerFrame, text="Clave:", font=("Helvetica", 14))
        password_label.pack(pady=10)

        password_entry = tk.Entry(registerFrame, show="*", font=("Helvetica", 12))
        password_entry.pack(pady=10)

        check_button = tk.Button(registerFrame, text="Actualizar", command=update, font=("Helvetica", 14), bg="white")
        check_button.pack(pady=20)


    window.title("Recuperar Sesión")
    window.geometry("400x600")
    window.resizable(0,0)

    registerFrame = tk.Frame(window)
    registerFrame.pack()

    titulo = tk.Label(registerFrame, text="Recuperar Sesión", font=("Helvetica", 18))
    titulo.pack(pady=20)

    username_label = tk.Label(registerFrame, text="Usuario:", font=("Helvetica", 14))
    username_label.pack(pady=10)

    username_entry = tk.Entry(registerFrame, font=("Helvetica", 12))
    username_entry.pack(pady=10)

    check_button = tk.Button(registerFrame, text="Verificar usuario", command=check_user, font=("Helvetica", 14), bg="white")
    check_button.pack(pady=20)
