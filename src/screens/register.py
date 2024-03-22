import tkinter 
from tkinter import Tk, messagebox
from sqlalchemy.orm import Session
from ..models import Usuario
from ..services.register import Usuario as UsuarioService
from ..engine import engine
import customtkinter

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
                if rol_select == "Director" and usuario.rol == rol_select:
                    messagebox.showinfo("Error", "No esta permitido crear mas de un director.")
                    return
            else:
                try:
                    connect.create(username, password, rol_select, question, answer)
                    messagebox.showinfo("Exito", f"Se ha registrado un(a) {rol_select}")
                    window.destroy()
                    screen_login(tk, window=Tk())
                except:
                    messagebox.showinfo("Error", "Usuario o contraseña es incorrecta")
        
    window.title("Registrar")
    window.geometry("800x500")
    window.resizable(0,0)
    window.iconbitmap('src/screens/disenos/LUMASIS.ico')
    verde="#15a35b"

    fondo = tk.PhotoImage(file='src/screens/disenos/fono2.png')
    image = tk.Label(window, image=fondo, width="800", height="500")
    image.place(x=0, y=0)
    image.image = fondo


    titulo = tk.Label(window, text="Registrar",bg="white", font=("Helvetica", 20))
    titulo.place(x=300,y=20)

    username_label = tk.Label(window, text="Usuario:",bg="white", font=("Helvetica", 16))
    username_label.place(x=185,y=140)

    username_entry = customtkinter.CTkEntry(master=window, width=200, height=36, border_width=0,
                                       font=(0, 18)) 
    #tk.Entry(window, font=("Helvetica", 12))
    username_entry.place(x=366,y=140)

    password_label = tk.Label(window, text="Clave:",bg="white", font=("Helvetica", 16))
    password_label.place(x=185,y=200)

    password_entry = customtkinter.CTkEntry(master=window, width=200, height=36, border_width=0,
                                       font=(0, 18), show="*")
    password_entry.place(x=366,y=200)

    rol = tk.StringVar(window)
    rol.set("Director")
    seleccionrol = ['Director', 'Profesor', 'Secretaria']
    opcion_rol = tk.OptionMenu(window, rol, *seleccionrol)
    opcion_rol.config(font=("Helvetica", 15),bg=verde, fg="#fff")
    opcion_rol.place(x=570,y=45)

    pregunta_label = tk.Label(window, text="Pregunta Seguridad:",bg="white", font=("Helvetica", 14))
    pregunta_label.place(x=185,y=260)

    pregunta_entry = customtkinter.CTkEntry(master=window, width=200, height=36, border_width=0,
                                       font=(0, 18)) 
    #tk.Entry(window, font=("Helvetica", 12))
    pregunta_entry.place(x=366,y=260)

    respuesta_label = tk.Label(window, text="Respuesta:",bg="white", font=("Helvetica", 16))
    respuesta_label.place(x=185,y=320)

    respuesta_entry = customtkinter.CTkEntry(master=window, width=200, height=36, border_width=0,
                                       font=(0, 18)) 
    #tk.Entry(window, show="*", font=("Helvetica", 12))
    respuesta_entry.place(x=366, y=320)

    #botonregistro = tk.PhotoImage(file='src/screens/disenos/botones/botoneslogin/botonesregistrar.png')
    register_button = customtkinter.CTkButton(master=window, width=160, height=40, text="Registrar Usuario",
                                              text_color="#fff", fg_color=verde, command=register, font=(0, 20),
                                              hover_color="#209c62")
    #tk.Button(window, image=botonregistro, command=register, font=("Helvetica", 14), bg=verde)
    register_button.place(x=330,y=420)

    gobackbutton = customtkinter.CTkButton(master=window, width=140, height=40, text="Regresar",
                                              text_color="#fff", fg_color=verde, command=volver, font=(0, 17),
                                              hover_color="#209c62")
    #tk.Button(window, text="regresar",command=volver,font=("Helvetica", 10), bg=verde)
    gobackbutton.place(x=10,y=20)
    
    window.mainloop()