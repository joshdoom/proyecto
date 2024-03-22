import tkinter
from tkinter import Tk, messagebox
from sqlalchemy.orm import Session
from ..models import Usuario
from ..services.register import Usuario as UsuarioService
from ..engine import engine
import customtkinter

def screen_recovery(tk: tkinter, window: Tk):
    connect = UsuarioService(engine)

    def volver():
        from .login import screen_login
        window.destroy()
        screen_login(tk, window=Tk())

    def check_user():
        user = username_entry.get()
        with Session(engine) as session:
            user_found = session.query(Usuario).filter_by(nombre=user).first()
            if user_found:
                recovery(user_found.pregunta_seguridad)
            else:
                messagebox.showerror("Error", "Usuario no encontrado")

    def update():
        from .login import screen_login

        user = username_entry.get()
        answer = respuesta_entry.get()
        password = password_entry.get()

        with Session(engine) as session:
            user = session.query(Usuario).filter_by(nombre=user, respuesta_seguridad=answer).first()
            if user:
                connect.update(user.id, password)
                messagebox.showinfo("Exito", "Has recuperado tu cuenta")
                window.destroy()
                screen_login(tk, window=Tk())
            else:
                messagebox.showerror("Error", "Usuario no encontrado")
                
    def recovery(question: str):
        global respuesta_entry
        global password_entry

        pregunta_label = tk.Label(window, text=f"{question}", bg="white", font=("Helvetica", 16))
        pregunta_label.place(x=200,y=150)

        respuesta_label = tk.Label(window, text="Respuesta:", bg="white", font=("Helvetica", 16))
        respuesta_label.place(x=200,y=180)

        respuesta_entry = customtkinter.CTkEntry(master=window, width=200, height=36, border_width=0,
                                       font=(0, 18), show="*") 
                                       
        #tk.Entry(window, show="*", font=("Helvetica", 12))
        respuesta_entry.place(x=330, y=180)

        password_label = tk.Label(window, text="Clave:",bg="white", font=("Helvetica", 16))
        password_label.place(x=200,y=260)

        password_entry = customtkinter.CTkEntry(master=window, width=200, height=36, border_width=0,
                                       font=(0, 18), show="*")
        
        #tk.Entry(window, show="*", font=("Helvetica", 12))
        password_entry.place(x=330,y=260)

        check_button = customtkinter.CTkButton(master=window, width=160, height=40, text="Actualizar Datos",
                                              text_color="#fff", fg_color=verde, command=update, font=(0, 20),
                                              hover_color="#209c62")
        #tk.Button(window, text="Actualizar", command=update, font=("Helvetica", 14), bg="white")
        check_button.place(x=400,y=380)


    window.title("Recuperar Sesión")
    window.geometry("800x500")
    window.resizable(0,0)
    window.iconbitmap('src/screens/disenos/LUMASIS.ico')
    
    verde="#15a35b"
    
    fondo = tk.PhotoImage(file='src/screens/disenos/fono2.png')
    image = tk.Label(window, image=fondo, width="800", height="500")
    image.place(x=0, y=0)
    image.image = fondo
    

    titulo = tk.Label(window, text="Recuperar Sesión",bg="white", font=("Helvetica", 20))
    titulo.place(x=300,y=20)

    username_label = tk.Label(window, text="Usuario:", bg="white", font=("Helvetica", 16))
    username_label.place(x=200,y=100)

    username_entry = customtkinter.CTkEntry(master=window, width=200, height=36, border_width=0,
                                       font=(0, 18)) 
    #tk.Entry(window, font=("Helvetica", 12))
    username_entry.place(x=330,y=100)

    check_button =customtkinter.CTkButton(master=window, width=160, height=40, text="Verificar Usuario",
                                              text_color="#fff", fg_color=verde, command=check_user, font=(0, 20),
                                              hover_color="#209c62")
    #tk.Button(window, text="Verificar usuario", command=check_user, font=("Helvetica", 14), bg="white")
    check_button.place(x=200,y=380)

    gobackbutton = customtkinter.CTkButton(master=window, width=140, height=40, text="Regresar",
                                              text_color="#fff", fg_color=verde, command=volver, font=(0, 17),
                                              hover_color="#209c62")
    #tk.Button(window, text="regresar", command=volver,font=("Helvetica", 10), bg=verde)
    gobackbutton.place(x=10,y=20)

    window.mainloop()
