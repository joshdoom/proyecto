import tkinter 
from tkinter import Tk, messagebox
from sqlalchemy.orm import Session
from ..models import Usuario
from ..services.register import Usuario as UsuarioService
from ..engine import engine

def screen_register(tk: tkinter, window: Tk):
    connect = UsuarioService(engine)

    def volver():
        from .login import screen_login
        window.destroy()
        screen_login(tk, window=Tk())

    def register():
        from .login import screen_login

        username = username_entry.get()
        password = password_entry.get()
        rol_select = rol.get()
        question = pregunta_entry.get()
        answer = respuesta_entry.get()

        with Session(engine) as session:
            usuarios = session.query(Usuario).all()

            for usuario in usuarios:
                if usuario.rol == rol_select:
                    messagebox.showinfo("Error", "No esta permitido crear mas de un director.")
                    return
            else:
                try:
                    connect.create(username, password, rol_select, question, answer)
                    window.destroy()
                    screen_login(tk, window=Tk())
                except:
                    messagebox.showinfo("Error", "Usuario o contraseña es incorrecta")
        
    window.title("Registrar")
    window.geometry("400x600")
    window.resizable(0,0)
    window.iconbitmap('src/screens/disenos/LUMASIS.ico')
    verde="#15a35b"

    registerFrame = tk.Frame(window)
    registerFrame.pack()
    fondo = tk.PhotoImage(file='src/screens/disenos/fondoregistro.png')
    imagenfondo = tk.Label(registerFrame,image=fondo)
    imagenfondo.pack()
    
    
   

    titulo = tk.Label(registerFrame, text="Registrar",bg="white", font=("Helvetica", 18))
    titulo.pack()
    titulo.place(x=150,y=20)

    username_label = tk.Label(registerFrame, text="Usuario:",bg="white", font=("Helvetica", 14))
    username_label.pack()
    username_label.place(x=165,y=100)

    username_entry = tk.Entry(registerFrame, font=("Helvetica", 12))
    username_entry.pack()
    username_entry.place(x=110,y=150)

    password_label = tk.Label(registerFrame, text="Clave:",bg="white", font=("Helvetica", 14))
    password_label.pack()
    password_label.place(x=175,y=210)

    password_entry = tk.Entry(registerFrame, show="*", font=("Helvetica", 12))
    password_entry.pack()
    password_entry.place(x=110,y=260)

    rol = tk.StringVar(registerFrame)
    rol.set("Rol")
    seleccionrol = ['Director', 'Profesor', 'Secretaria']
    opcion_rol = tk.OptionMenu(registerFrame, rol, *seleccionrol)
    opcion_rol.config(font=("Helvetica", 16),bg=verde)
    opcion_rol.pack()
    opcion_rol.place(x=165,y=300)

    pregunta_label = tk.Label(registerFrame, text="Pregunta de Seguridad:",bg="white", font=("Helvetica", 14))
    pregunta_label.pack()
    pregunta_label.place(x=100,y=360)

    pregunta_entry = tk.Entry(registerFrame, font=("Helvetica", 12))
    pregunta_entry.pack()
    pregunta_entry.place(x=110,y=410)

    respuesta_label = tk.Label(registerFrame, text="Respuesta:",bg="white", font=("Helvetica", 14))
    respuesta_label.pack()
    respuesta_label.place(x=150,y=460)

    respuesta_entry = tk.Entry(registerFrame, show="*", font=("Helvetica", 12))
    respuesta_entry.pack()
    respuesta_entry.place(x=110,y=510)

    botonregistro = tk.PhotoImage(file='src/screens/disenos/botones/botoneslogin/botonesregistrar.png')
    register_button = tk.Button(registerFrame, image=botonregistro, command=register, font=("Helvetica", 14), bg=verde)
    register_button.pack()
    register_button.place(x=150,y=550)

    gobackbutton = tk.Button(registerFrame, text="regresar",command=volver,font=("Helvetica", 10), bg=verde)
    gobackbutton.pack()
    gobackbutton.place(x=20,y=20)
    
    window.mainloop()