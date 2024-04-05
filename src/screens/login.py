import tkinter 
import os
import customtkinter
from tkinter import RIGHT, Button, Entry, Frame, Label, Tk, messagebox
from sqlalchemy.orm import Session

from ..models import Usuario
from ..engine import engine



def screen_login(tk: tkinter, window: Tk):
    def login():
        from .index import screen_index
        from .superusuario import screen_superusuario

        username = username_entry.get()
        password = password_entry.get()

        with Session(engine) as session:
            users = session.query(Usuario).all()
            if username == "admin" and password == "admin":
                    messagebox.showinfo("Exito", "Iniciaste sesion")
                    screen_superusuario(tk, window=tk.Toplevel(),)
                    return
            
            for user in users:
                if username == user.nombre and password == user.contrasena:
                    messagebox.showinfo("Exito", "Iniciaste sesion")
                    window.destroy()
                    screen_index(tk, window=Tk(), rol=user.rol, cedula_profesor=user.profesor_cedula)
                    return
            else:
                messagebox.showinfo("Error", "Usuario o contraseña es incorrecta")
    
    def register():
        from .register import screen_register
        window.destroy()
        screen_register(tk, window=Tk())
    
    def recovery():
        from .recovery import screen_recovery
        window.destroy()
        screen_recovery(tk, window=Tk())

    def abrir_manual():
        os.startfile('src\\pdfs\\Manual_de_usuario.pdf')


    verde="#15a35b"
    verdeoscuro="#01212e"    
    window.title("Login")    
    window.geometry("1000x650")    
    window.resizable(0,0)
    window.iconbitmap('src/screens/disenos/logonuevoB.ico')   
    window.config(bg=verdeoscuro)
    

    loginFrameright=Frame(window)
    loginFrameright.configure(width="400", height="650")
    loginFrameright.pack(side=RIGHT)  

    Framefondo=Frame(window)
    Framefondo.pack()
    fondo = tk.PhotoImage(file='src/screens/disenos/fono2.png')
    imagenfondo = tk.Label(Framefondo,image=fondo)
    imagenfondo.pack()

    loginlabel= Label(window, text="Iniciar Sesión", bg="white")
    loginlabel.place(x=170, y=100)
    loginlabel.configure(font=("Calisto Mt", 30, "bold"))

    username_label = Label(window, text="Usuario:", bg="white")
    username_label.place(x=250, y=220)
    username_label.config(font=("Calisto Mt", 18, "bold"))

    frames = Frame(window, width=450, height=55, bg="#fff")
    frames.place(x=180, y=265)
    
    frames2 = Frame(window, width=450, height=55, bg="#fff")
    frames2.place(x=180, y=400)
    
    verde="#3ddc8f"
    
    framebuttons1 = Frame(window, width=200, height=80, bg=verde)
    framebuttons1.place(x=215, y=460)
    
    framebuttons2 = Frame(window, width=200, height=80, bg=verde)
    framebuttons2.place(x=95, y=540)
    
    framebuttons3 = Frame(window, width=200, height=80, bg=verde)
    framebuttons3.place(x=350, y=540)
    
    username_entry =  customtkinter.CTkEntry(master=frames, width=250, height=42, border_width=0,bg_color=verde,
                                       font=(0, 18))
    username_entry.pack()
    #username_entry.config(font=("Arial",15))


    password_label = Label(window, text="Contraseña:", bg="white")
    password_label.place(x=233, y=350)
    password_label.config(font=("Calisto Mt", 18, "bold"))


    password_entry = Entry(window)
    
    password_entry = customtkinter.CTkEntry(master=frames2, width=250, height=42, border_width=0,bg_color=verde,
                                       font=(0, 18), show="*")
    password_entry.pack()

    #botoninicio = tk.PhotoImage(file='src/screens/disenos/botones/botoneslogin/botoninicio3.png')
    login_button = customtkinter.CTkButton(master=framebuttons1, width=160, height=40, text="Iniciar Sesión",
                                              text_color="#fff", fg_color=verde, command=login, font=(0, 20),
                                              hover_color="#209c62")
    
    #login_button = Button(window, image=botoninicio,command=login,bg=verde)
    
    login_button.pack()

    botonregis = tk.PhotoImage(file='src/screens/disenos/botones/botoneslogin/botonesregistrar.png')
    login_button2 = customtkinter.CTkButton(master=framebuttons2, width=160, height=40, text="Crear Usuario",
                                              text_color="#fff", fg_color=verde, command=register, font=(0, 20),
                                              hover_color="#209c62")
    
    login_button2.pack()

    botonrecu = tk.PhotoImage(file='src/screens/disenos/botones/botoneslogin/botonesrecuperar2.png')
    login_button3 = customtkinter.CTkButton(master=framebuttons3, width=160, height=40, text="Recuperar Usuario",
                                              text_color="#fff", fg_color=verde, command=recovery, font=(0, 20),
                                              hover_color="#209c62")
    
    #login_button3 = Button(window, image=botonrecu,command=recovery,bg=verde)
    
    login_button3.pack()

    botonmanu= tk.PhotoImage(file='src/screens/disenos/logonuevomini.png')
    Manu_button= Button(window,image=botonmanu, command=abrir_manual,bg="white")
    Manu_button.pack()
    Manu_button.place(x=60,y=70)

    urbanejaico = tk.PhotoImage(file='src/screens/disenos/urbaneja.png')
    instiico = tk.Label(window, image=urbanejaico,bg=verde, relief="solid")
    instiico.place(x=465,y=70)

    fondoright= Frame(window)
    fondoright.pack()
    imagenfondo2= tk.PhotoImage(file='src/screens/disenos/mejorescuela2.png')
    imagenfondoright = tk.Label(loginFrameright, image=imagenfondo2)
    imagenfondoright.pack()


    window.mainloop()   