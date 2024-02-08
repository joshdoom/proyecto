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

        respuesta_label = tk.Label(registerFrame, text="Respuesta:",bg="white", font=("Helvetica", 14))
        respuesta_label.pack()
        respuesta_label.place(x=150,y=260)

        respuesta_entry = tk.Entry(registerFrame, show="*", font=("Helvetica", 12))
        respuesta_entry.pack()
        respuesta_entry.place(x=110, y=300)

        password_label = tk.Label(registerFrame, text="Clave:",bg="white", font=("Helvetica", 14))
        password_label.pack()
        password_label.place(x=170,y=370)

        password_entry = tk.Entry(registerFrame, show="*", font=("Helvetica", 12))
        password_entry.pack()
        password_entry.place(x=110,y=450)

        check_button = tk.Button(registerFrame, text="Actualizar", command=update, font=("Helvetica", 14), bg="white")
        check_button.pack()
        check_button.place(x=155,y=500)


    window.title("Recuperar Sesión")
    window.geometry("400x600")
    window.resizable(0,0)
    window.iconbitmap('src/screens/disenos/LUMASIS.ico')
    verde="#15a35b"
    

    registerFrame = tk.Frame(window)
    registerFrame.pack()
    fondo = tk.PhotoImage(file='src/screens/disenos/fondoregistro.png')
    imagenfondo = tk.Label(registerFrame,image=fondo)
    imagenfondo.pack()
    

    titulo = tk.Label(registerFrame, text="Recuperar Sesión",bg="white", font=("Helvetica", 18))
    titulo.pack()
    titulo.place(x=110,y=20)

    username_label = tk.Label(registerFrame, text="Usuario:",bg="white", font=("Helvetica", 14))
    username_label.pack()
    username_label.place(x=165,y=100)

    username_entry = tk.Entry(registerFrame, font=("Helvetica", 12))
    username_entry.pack()
    username_entry.place(x=110,y=150)

    check_button = tk.Button(registerFrame, text="Verificar usuario", command=check_user, font=("Helvetica", 14), bg="white")
    check_button.pack()
    check_button.place(x=130,y=210)

    window.mainloop()
