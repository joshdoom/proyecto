import tkinter as tk
from tkinter import LEFT, TOP, Button, Frame, Tk
from tkinter import messagebox

negro="#00292d"
verdeoscuro="#01212e"
verde="#15a35b"


def screen_index(tk: tk, window: Tk, rol: str, cedula_profesor: str = None):

    
    def create_button(bg, command, image):
        button = tk.Button(Frame,command=command,bg=bg,image=image)
        button.pack(pady=10)
    
    from .professor import screen_professor
    from .grados import screen_grado

    def primero():
        window.destroy()
        screen_grado(tk, window=tk.Tk(), degree=1, rol=rol, cedula_profesor=cedula_profesor)

    def segundo():
        window.destroy()
        screen_grado(tk, window=tk.Tk(), degree=2, rol=rol, cedula_profesor=cedula_profesor)

    def tercero():
        window.destroy()
        screen_grado(tk, window=tk.Tk(), degree=3, rol=rol, cedula_profesor=cedula_profesor)

    def cuarto():
        window.destroy()
        screen_grado(tk, window=tk.Tk(), degree=4, rol=rol, cedula_profesor=cedula_profesor)

    def quinto():
        window.destroy()
        screen_grado(tk, window=tk.Tk(), degree=5, rol=rol, cedula_profesor=cedula_profesor)

    def profesores():
        window.destroy()
        screen_professor(tk, window=tk.Tk(), rol=rol)

    def cerrasesion():
        from .login import screen_login
        window.destroy()
        screen_login(tk, window=Tk())
    
    def ventanacerrar():
        seguro = messagebox.askyesno("Cerrar Sesión", "¿Estás seguro de querer cerrar sesión?")
        if seguro:
            cerrasesion()
        
            

    window.title("MENU PRINCIPAL")
    window.geometry("1000x650")    
    color = "#20232a" 
    color2 = "#32363f"
    window.config(bg="white")
    window.resizable(0,0)
    window.iconbitmap('src/screens/disenos/logonuevoB.ico')

    
    barra_superior= Frame(window)
    barra_superior.config(bg=verdeoscuro,height=60)    
    barra_superior.pack(side=TOP, fill="both")
    Urbaneja= tk.Label(barra_superior,text="Luis Manuel Urbaneja Achelpohl", fg="white", bg=verdeoscuro,font=("Bodoni", 18, ))    
    Urbaneja.pack(side="left")
    Urbaneja= tk.Label(barra_superior,text=rol, fg="white", bg=verdeoscuro,font=("Bodoni", 18, ))    
    Urbaneja.pack(side="right")

    
    
    
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
    

    if not rol == 'Profesor': 
        imagen6 = tk.PhotoImage(file='src/screens/disenos/boton6t.png')
        buttonDashBoard6 = Button(menu_lateral,command=profesores, bg=color,image=imagen6)    
        buttonDashBoard6.pack()
    
    imagen7 = tk.PhotoImage(file='src/screens/disenos/botoncerrar.png')
    buttonDashBoard7 = Button(menu_lateral,image=imagen7,command=ventanacerrar, bg=color)    
    buttonDashBoard7.pack()
    buttonDashBoard7.place(x=0,y=570)

            
    fondo= Frame(window)
    fondo.pack()
    imagenfondo = tk.PhotoImage(file='src/screens/disenos/menu2.png')    
    etiquetafondo = tk.Label(fondo, image=imagenfondo)
    etiquetafondo.pack()
        
#---------------------------Funciones de los botones-----------------------------

    
    
    
    
    window.mainloop()
    
    
    
    
    
    
    
    
    
    