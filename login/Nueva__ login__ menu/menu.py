from tkinter import *
import tkinter as tk

negro="#00292d"
verdeoscuro="#01212e"
    

def josh():    
    from grado1 import primero
    primero()
    
    
   
class todo:
  root=Tk()
  root.title("sam")
  root.geometry("1000x650")
  color = "#20232a" 
  color2 = "#32363f"
  root.config(bg="white")
  root.resizable(0,0)

 
  barra_superior= Frame(root)
  barra_superior.config(bg=verdeoscuro,height=60)    
  barra_superior.pack(side=TOP, fill="both")
  Urbaneja= Label(barra_superior,text="Jose Rafael Urbaeja Achepolh", fg="white", bg=verdeoscuro,font=("Bodoni", 18, ))    
  Urbaneja.pack(side=LEFT)
  
  menu_lateral= Frame(root)
  menu_lateral.config(bg=negro,width="100",height=150)
  menu_lateral.pack(side="left", fill="both",expand=False)
        
        

  imagen = tk.PhotoImage(file='C:\\Users\\USUARIO\\Downloads\\Nueva carpeta\\login\\disenos\\boton1t.png')
  buttonDashBoard = Button(menu_lateral,command=josh, bg=color,image=imagen)    
  buttonDashBoard.place(x=0, y=0)
  buttonDashBoard.pack()
  imagen2 = tk.PhotoImage(file='C:\\Users\\USUARIO\\Downloads\\Nueva carpeta\\login\\disenos\\boton2t.png')
  buttonDashBoard2 = Button(menu_lateral, bg=color,image=imagen2)    
  buttonDashBoard2.pack() 
  imagen3 = tk.PhotoImage(file='C:\\Users\\USUARIO\\Downloads\\Nueva carpeta\\login\\disenos\\boton3t.png')
  buttonDashBoard3 = Button(menu_lateral, bg=color,image=imagen3)    
  buttonDashBoard3.pack() 
  imagen4 = tk.PhotoImage(file='C:\\Users\\USUARIO\\Downloads\\Nueva carpeta\\login\\disenos\\boton4t.png')
  buttonDashBoard4 = Button(menu_lateral, bg=color,image=imagen4)    
  buttonDashBoard4.pack()
  imagen5 = tk.PhotoImage(file='C:\\Users\\USUARIO\\Downloads\\Nueva carpeta\\login\\disenos\\boton5t.png')
  buttonDashBoard5 = Button(menu_lateral, bg=color,image=imagen5)    
  buttonDashBoard5.pack()
  imagen6 = tk.PhotoImage(file='C:\\Users\\USUARIO\\Downloads\\Nueva carpeta\\login\\disenos\\boton6t.png')
  buttonDashBoard6 = Button(menu_lateral, bg=color,image=imagen6)    
  buttonDashBoard6.pack()
        

        
  fondo= Frame(root)
  fondo.pack()
  imagenfondo = tk.PhotoImage(file='C:\\Users\\USUARIO\\Downloads\\Nueva carpeta\\login\\\\disenos\\menu.png')    
  etiquetafondo = tk.Label(fondo, image=imagenfondo)
  etiquetafondo.pack()

  root.mainloop()