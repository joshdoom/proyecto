import tkinter as tk
from tkinter import LEFT, TOP, Button, Frame, Tk

from sqlalchemy import Label

negro="#00292d"
verdeoscuro="#01212e"
def screen_index(tk: tk, window: Tk):
    def create_button(bg, command, image):
        button = tk.Button(Frame,command=command,bg=bg,image=image)
        button.pack(pady=10)
    
    from .professor import screen_professor
    from .grados.grado_i import screen_grado_i
    from .grados.grado_ii import screen_grado_ii
    from .grados.grado_iii import screen_grado_iii
    from .grados.grado_iv import screen_grado_iv
    from .grados.grado_v import screen_grado_v

    def primero():
        screen_grado_i(tk, window=Tk())

    def segundo():
        screen_grado_ii(tk, window=Tk())

    def tercero():
        screen_grado_iii(tk, window=Tk())

    def cuarto():
        screen_grado_iv(tk, window=Tk())

    def quinto():
        screen_grado_v(tk, window=Tk())

    def profesores():
        screen_professor(tk, window=Tk())


    
    window.title("sam")
    window.geometry("1000x650")
    color = "#20232a" 
    color2 = "#32363f"
    window.config(bg="white")
    window.resizable(0,0)

    
    barra_superior= Frame(window)
    barra_superior.config(bg=verdeoscuro,height=60)    
    barra_superior.pack(side=TOP, fill="both")
    #Urbaneja= Label(barra_superior,text="Jose Rafael Urbaeja Achepolh", fg="white", bg=verdeoscuro,font=("Bodoni", 18, ))    
    #Urbaneja.pack(side="left")
    
    menu_lateral= Frame(window)
    menu_lateral.config(bg=negro,width="100",height=150)
    menu_lateral.pack(side="left", fill="both",expand=False)
                
                

    imagen = tk.PhotoImage(file='src/screens/disenos/boton1t.png')
    buttonDashBoard = Button(menu_lateral,command=primero, bg=color,image=imagen)    
    buttonDashBoard.place(x=0, y=0)
    buttonDashBoard.pack()
    imagen2 = tk.PhotoImage(file='src/screens/disenos/boton2t.png')
    buttonDashBoard2 = Button(menu_lateral, command=segundo, bg=color,image=imagen2)    
    buttonDashBoard2.pack() 
    imagen3 = tk.PhotoImage(file='src/screens/disenos/boton3t.png')
    buttonDashBoard3 = Button(menu_lateral,command=tercero, bg=color,image=imagen3)    
    buttonDashBoard3.pack() 
    imagen4 = tk.PhotoImage(file='src/screens/disenos/boton4t.png')
    buttonDashBoard4 = Button(menu_lateral,command=cuarto, bg=color,image=imagen4)    
    buttonDashBoard4.pack()
    imagen5 = tk.PhotoImage(file='src/screens/disenos/boton5t.png')
    buttonDashBoard5 = Button(menu_lateral,command=quinto, bg=color,image=imagen5)    
    buttonDashBoard5.pack()
    imagen6 = tk.PhotoImage(file='src/screens/disenos/boton6t.png')
    buttonDashBoard6 = Button(menu_lateral,command=profesores, bg=color,image=imagen6)    
    buttonDashBoard6.pack()
            

            
    fondo= Frame(window)
    fondo.pack()
    imagenfondo = tk.PhotoImage(file='src/screens/disenos/menu.png')    
    etiquetafondo = tk.Label(fondo, image=imagenfondo)
    etiquetafondo.pack()
        
#---------------------------Funciones de los botones-----------------------------

    
    
    
    window.mainloop()
    
    
    
    
    
    
    
    
    
    #window.title("Ventana Principal")
    #window.geometry("400x600")
    #window.resizable(0,0)

    #loginFrame = tk.Frame(window)
    #loginFrame.pack()

    #titulo = tk.Label(loginFrame, text="Selecciona a donde quieras ir", font=("Helvetica", 16))
    #titulo.pack(pady=20)

    #create_button("Primer año", command=primero)
    #create_button("Segundo año", command=segundo)
    #create_button("Tercer año", command=tercero)
    #create_button("Cuarto año", command=cuarto)
    #create_button("Quinto año", command=quinto)
    #create_button("Profesores", command=profesores)