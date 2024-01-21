from tkinter import *
class quinto:
        root = Tk()        
        root.title("Quinto año")
        root.geometry("1280x680")      
        root.iconbitmap("Urbaneja.ico")
        root.config(bd=20)
        root.resizable(False, False)
        miFrame=Frame()
        miFrame.pack()  
        miFrame.config(width="1200", height="250")
        miFrame.config(bd=5)
        miFrame.config(relief="groove")
            #frame botones 1

        miFrame1=Frame()
        miFrame1.pack()   
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
        milabel.config(font=("Arial Black", 15))



                #cuadro intrducir texto

            #cuadrotexto=Entry(root)
            #cuadrotexto.place(x=455, y=7)
            #cuadrotexto.config(font=("Arial",20))



                #Label 1.2

        milabel2= Label(miFrame, text="Apellido:")
        milabel2.place(x=150, y=80)   
        milabel2.config(font=("Arial Black", 15))



                #cuadro intrducir texto 2

            #cuadrotexto2=Entry(root)
            #cuadrotexto2.place(x=455, y=85)
            #cuadrotexto2.config(font=("Arial",20))



                #Label 1.3


        milabel3= Label(miFrame, text="ID:")
        milabel3.place(x=150, y=160)   
        milabel3.config(font=("Arial Black", 15))


                #cuadro intrducir texto 3

            #cuadrotexto3=Entry(root)
            #cuadrotexto3.place(x=455, y=165)
            #cuadrotexto3.config(font=("Arial",20))





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





                #frame botones menu

        miFramemenu=Frame()
        miFramemenu.pack()
        miFramemenu.config(bg="orange")
        miFramemenu.config(width="10", height="35")
        miFramemenu.config(bd=1)
        miFramemenu.place(x=1010, y=210)
        miFramemenu.config(relief="raised")


            


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