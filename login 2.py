from tkinter import *


def login():
    username = username_entry.get()
    password = password_entry.get()

    # Verificar las credenciales
    if username == "sam" and password == "123":
        print("Inicio de sesión exitoso")
        raiz.destroy()
        root()



def root():    
    #Raiz sistema
 
    root = Tk()        
    root.title("control de notas")
    root.geometry("1280x680")
    root.resizable(0,0)
    fondo="#0da75e"
    root.config(bg=fondo)
    root.iconbitmap("Urbaneja.ico")
    root.config(bd=20)
    root.resizable(False, False)
    
    
    



        #Barramenu

    barramenu=Menu(root)
    root.config(menu=barramenu)
    Archivomenu=Menu(barramenu, tearoff=0)
    barramenu.add_cascade(label="Años", menu=Archivomenu)
    Archivomenu.add_command(label="Primer año")
    Archivomenu.add_command(label="Segundo año")
    Archivomenu.add_command(label="Tercer año")
    Archivomenu.add_command(label="Cuarto año")
    Archivomenu.add_command(label="Quinto año")


    archivoEdicion=Menu(barramenu)
    barramenu.add_cascade(label="Edicion", menu=Archivomenu)
    archivoHerramienta=Menu(barramenu)
    barramenu.add_cascade(label="Herramienta", menu=Archivomenu)




        #frame

    miFrame=Frame()
    miFrame.pack()
    miFrame.config(bg=fondo)
    miFrame.config(width="1200", height="250")
    miFrame.config(bd=5)
    miFrame.config(relief="groove")








        #frame botones 1

    miFrame1=Frame()
    miFrame1.pack()
    miFrame1.config(bg=fondo)
    miFrame1.config(width="1200", height="350")
    miFrame1.config(bd=1)
    miFrame1.place(x=800, y=210)
    miFrame1.config(relief="raised")


        #Boton 1

    botonnuevo=Button(miFrame1, text="Nuevo")
    botonnuevo.pack()
    botonnuevo.config(bg="white")
    botonnuevo.config(fg="black")
    botonnuevo.config(font=("Arial Black", 10))


        #frame botones 2

    miFrame12=Frame()
    miFrame12.pack()
    miFrame12.config(bg="white")
    miFrame12.config(width="1200", height="350")
    miFrame12.config(bd=1)
    miFrame12.place(x=900, y=210)
    miFrame12.config(relief="raised")


        #Boton 2

    botonguardar=Button(miFrame12, text="Guardar")
    botonguardar.pack()
    botonguardar.config(bg="white")
    botonguardar.config(fg="black")
    botonguardar.config(font=("Arial Black", 10))






        #frame botones 3

    miFrame13=Frame()
    miFrame13.pack(side="bottom", anchor="w")
    miFrame13.config(bg="red")
    miFrame13.config(width="1200", height="350")
    miFrame13.config(bd=1)
    miFrame13.config(relief="raised")


        #Boton 3

    botoneditar=Button(miFrame13, text="Editar")
    botoneditar.pack()
    botoneditar.config(bg="white")
    botoneditar.config(fg="black")
    botoneditar.config(font=("Arial Black", 10))





        #Label

    milabel= Label(miFrame, text="Nombre:")
    milabel.place(x=150, y=0)
    milabel.config(bg=fondo)
    milabel.config(font=("Arial Black", 15))



        #cuadro intrducir texto

    cuadrotexto=Entry(root)
    cuadrotexto.place(x=455, y=7)
    cuadrotexto.config(font=("Arial",20))



        #Label 1.2

    milabel2= Label(miFrame, text="Apellido:")
    milabel2.place(x=150, y=80)
    milabel2.config(bg=fondo)
    milabel2.config(font=("Arial Black", 15))



        #cuadro intrducir texto 2

    cuadrotexto2=Entry(root)
    cuadrotexto2.place(x=455, y=85)
    cuadrotexto2.config(font=("Arial",20))



        #Label 1.3


    milabel3= Label(miFrame, text="ID:")
    milabel3.place(x=150, y=160)
    milabel3.config(bg=fondo)
    milabel3.config(font=("Arial Black", 15))


        #cuadro intrducir texto 3

    cuadrotexto3=Entry(root)
    cuadrotexto3.place(x=455, y=165)
    cuadrotexto3.config(font=("Arial",20))





        #frame2

    miFrame2=Frame()
    miFrame2.pack(fill="y", expand="true")
    miFrame2.pack(side="bottom")
    miFrame2.config(bg="white")
    miFrame2.config(width="1400", height="350")
    miFrame2.config(bd=10)
    miFrame2.config(relief="groove")


        #label 2

    milabel4= Label(miFrame2, text="ID")
    milabel4.place(x=50, y=0)
    milabel4.config(fg="black")
    milabel4.config(bg="white")
    milabel4.config(font=("Arial", 15))


        #label 2.2

    milabel5= Label(miFrame2, text="Nombre")
    milabel5.place(x=250, y=0)
    milabel5.config(fg="black")
    milabel5.config(bg="white")
    milabel5.config(font=("Arial", 15))

        #label 2.3

    milabel6= Label(miFrame2, text="Apellido")
    milabel6.place(x=550, y=0)
    milabel6.config(fg="black")
    milabel6.config(bg="white")
    milabel6.config(font=("Arial", 15))


        #label 2.4

    milabel7= Label(miFrame2, text="Nota")
    milabel7.place(x=850, y=0)
    milabel7.config(fg="black")
    milabel7.config(bg="white")
    milabel7.config(font=("Arial", 15))



        #label 2.5


    milabel8= Label(miFrame2, text="Promedio")
    milabel8.place(x=1100, y=0)
    milabel8.config(fg="black")
    milabel8.config(bg="white")
    milabel8.config(font=("Arial", 15))



        #Barra

    scrollvert=Scrollbar(miFrame2, command=Frame)
    scrollvert.place(x=1200, y=125)



        #frame botones menu

    miFramemenu=Frame()
    miFramemenu.pack()
    miFramemenu.config(bg="orange")
    miFramemenu.config(width="10", height="35")
    miFramemenu.config(bd=1)
    miFramemenu.place(x=1010, y=210)
    miFramemenu.config(relief="raised")


        #Boton menu

    #botonmateria=Button(miFramemenu, text="Materias")
    #botonmateria.pack()
    #botonmateria.config(bg="orange")
    #botonmateria.config(fg="black")
    #botonmateria.config(font=("Arial Black", 10))


    var = StringVar(miFramemenu)
    var.set ("Materias")
    opciones=["Arte y patrimonio","Castellano","Ciencias Naturales","Educacion Fisica","Geografía, historia y ciudadanía (GHC)","Ingles","Matematicas","Orientación y convivencia ","Participación en grupos de creación, recreación y producción (G.E.R.P)"]
    opcion=OptionMenu(miFramemenu, var, *opciones)
    opcion.config(width=15)
    opcion.config(bg="white")
    botonguardar.config(fg="black")
    botoneditar.config(font=("Arial Black", 10))
    opcion.pack()


    root.mainloop()  
        
        
   


raiz = Tk()
raiz.title("Login")
raiz.geometry("400x600")
raiz.resizable(0,0)
raiz.iconbitmap("Urbaneja.ico")
fondo="#0da75e"
loginFrame=Frame()
loginFrame.configure(bg=fondo)
loginFrame.configure(width="400", height="600")
#imagen = PhotoImage(file="urbanejalogin2.png")
#etiqueta = Label(raiz, image=imagen)
#etiqueta.place(x=120, y=110)
#etiqueta.pack()
loginFrame.pack()



            

loginlabel= Label(loginFrame, text="Login")
loginlabel.pack()
loginlabel.place(x=170, y=0)
loginlabel.configure(bg=fondo)
loginlabel.configure(font=("Calisto Mt", 18, "bold"))




# Crear los elementos de la interfaz
username_label = Label(loginFrame, text="Usuario:")
username_label.pack()
username_label.place(x=40, y=400)
username_label.config(bg=fondo)
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
password_label.config(bg=fondo)
password_label.config(font=("Calisto Mt", 18, "bold"))




login_button = Button(loginFrame, text="Entrar", command=login)
login_button.pack()
login_button.place(x=140, y=550)
login_button.config(font=("Arial", 16))
login_button.config(bg= "white")






raiz.mainloop()





        






