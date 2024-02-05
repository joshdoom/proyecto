import tkinter 
from tkinter import RIGHT, Button, Entry, Frame, Label, Tk, messagebox
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
    
    def register():
        from .register import screen_register
        window.destroy()
        screen_register(tk, window=Tk())
    
    def recovery():
        from .recovery import screen_recovery
        window.destroy()
        screen_recovery(tk, window=Tk())

    verde="#15a35b"
    verdeoscuro="#01212e"    
    window.title("Login")    
    window.geometry("1000x650")    
    window.resizable(0,0)
    window.iconbitmap('C:\\Users\\VizcaIno\\Desktop\\proyecto-main\\src\\screens\\disenos\\LUMASIS.ico')    
    window.config(bg=verdeoscuro)
    

    loginFrameright=Frame(window)
    loginFrameright.configure(width="400", height="650")
    loginFrameright.pack(side=RIGHT)

    Framefondo=Frame(window)
    Framefondo.pack()
    fondo = tk.PhotoImage(file='C:\\Users\\VizcaIno\\Desktop\\proyecto-main\\src\\screens\\disenos\\fono2.png')
    imagenfondo = tk.Label(Framefondo,image=fondo)
    imagenfondo.pack()

    loginlabel= Label(window, text="Iniciar Sesion", bg="white")
    loginlabel.pack()
    loginlabel.place(x=170, y=100)
    loginlabel.configure(font=("Calisto Mt", 30, "bold"))

    username_label = Label(window, text="Usuario:", bg="white")
    username_label.pack()
    username_label.place(x=250, y=220)
    username_label.config(font=("Calisto Mt", 18, "bold"))

    username_entry = Entry(window)
    username_entry.pack()
    username_entry.place(x=185, y=290)
    username_entry.config(font=("Arial",15))


    password_label = Label(window, text="Contraseña:", bg="white")
    password_label.pack()
    password_label.place(x=233, y=350)
    password_label.config(font=("Calisto Mt", 18, "bold"))


    password_entry = Entry(window)
    password_entry.pack()
    password_entry.place(x=185, y=420)
    password_entry.config(font=("Arial",15))
    password_entry.config(show="*")

    botoninicio = tk.PhotoImage(file='C:\\Users\\VizcaIno\\Desktop\\proyecto-main\\src\\screens\\disenos\\botones\\botoneslogin\\botoninicio3.png')
    login_button = Button(window, image=botoninicio,command=login,bg=verde)
    login_button.pack()
    login_button.place(x=175, y=480)

    botonregis = tk.PhotoImage(file='C:\\Users\\VizcaIno\\Desktop\\proyecto-main\\src\\screens\\disenos\\botones\\botoneslogin\\botonesregistrar.png')
    login_button2 = Button(window, image=botonregis,command=register,bg=verde)
    login_button2.pack()
    login_button2.place(x=95, y=550)

    botonrecu = tk.PhotoImage(file='c:\\Users\\VizcaIno\\Desktop\\proyecto-main\\login\\login\\disenos\\botones\\botoneslogin\\botonesrecuperar2.png')
    login_button2 = Button(window, image=botonrecu,command=recovery,bg=verde)
    login_button2.pack()
    login_button2.place(x=350, y=550)

    fondoright= Frame(window)
    fondoright.pack()
    imagenfondo2= tk.PhotoImage(file='C:\\Users\\VizcaIno\\Desktop\\proyecto-main\\src\\screens\\disenos\\mejorescuela2.png')
    imagenfondoright = tk.Label(loginFrameright, image=imagenfondo2)
    imagenfondoright.pack()

    window.mainloop()   