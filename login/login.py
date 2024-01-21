from tkinter import *

def login():
    username = username_entry.get()
    password = password_entry.get()
   
    if username == "a" and password == "a":   
        raiz.destroy()
        rayo()
        
        
def rayo():
        def primero():
            raiz.destroy()
            from grado1 import primero
            primero()

        def segundo():
            raiz.destroy()
            from grado2 import segundo
            segundo()

        def tercero():
            raiz.destroy()
            from grado3 import tercero
            tercero()

        def cuarto():
            raiz.destroy()
            from grado4 import cuarto
            cuarto()

        def quinto():
            raiz.destroy()
            from grado5 import quinto
            quinto()
        
                        

        raiz = Tk()
        raiz.title("Login")
        raiz.geometry("400x600")
        raiz.resizable(0,0)
        raiz.iconbitmap("Urbaneja.ico")
        loginFrame=Frame()
        loginFrame.configure(width="400", height="600")
        loginFrame.pack() 

        barramenu=Menu(raiz)
        raiz.config(menu=barramenu)
        Archivomenu=Menu(barramenu, tearoff=0)
        barramenu.add_cascade(label="Años", menu=Archivomenu)
        Archivomenu.add_command(label="Primer año",command=primero)
        Archivomenu.add_command(label="Segundo año",command=segundo)
        Archivomenu.add_command(label="Tercer año",command=tercero)
        Archivomenu.add_command(label="Cuarto año",command=cuarto)
        Archivomenu.add_command(label="Quinto año",command=quinto)
        raiz.mainloop()                
 
raiz = Tk()
raiz.title("Login")
raiz.geometry("400x600")
raiz.resizable(0,0)
raiz.iconbitmap("Urbaneja.ico")
loginFrame=Frame()
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