import tkinter
from tkinter import LEFT, TOP, Frame, Label, Tk

root=Tk()
root.title("sam")
root.geometry("1000x650")
color = "#20232a" 
color2 = "#32363f"
root.config(bg="white")
root.resizable(0,0)


    


def screen_index(tk: tkinter, window: Tk):
  def create_button(text, command):
        button = tk.Button(loginFrame, text=text, command=command)
        button.pack(pady=10)
    
  from .professor import screen_professor
  


    
  window.title("Ventana Principal")
  window.geometry("1000x650")
  color = "#20232a" 
  color2 = "#32363f"
  window.config("white")
  window.resizable(0,0)

  negro="#00292d"
  verdeoscuro="#01212e"

  loginFrame = tk.Frame(window)
  loginFrame.pack()
  


 
  barra_superior= Frame(window)
  barra_superior.config(bg=verdeoscuro,height=60)    
  barra_superior.pack(side=TOP, fill="both")
  Urbaneja= Label(barra_superior,text="Jose Rafael Urbaeja Achepolh", fg="white", bg=verdeoscuro,font=("Bodoni", 18, ))    
  Urbaneja.pack(side=LEFT)
  
  menu_lateral= Frame(window)
  menu_lateral.config(bg=negro,width="100",height=150)
  menu_lateral.pack(side="left", fill="both",expand=False)
        
        

  imagen = tk.PhotoImage()
  buttonDashBoard = create_button(menu_lateral, bg=color,image=imagen)    
  buttonDashBoard.place(x=0, y=0)
  buttonDashBoard.pack()
  imagen2 = tk.PhotoImage(file='c:\\Users\\VizcaIno\\Desktop\\proyecto-main\\src\\screens\\disenos\\boton2t.png')
  buttonDashBoard2 = create_button(menu_lateral, bg=color,image=imagen2)    
  buttonDashBoard2.pack() 
  imagen3 = tk.PhotoImage(file='c:\\Users\\VizcaIno\\Desktop\\proyecto-main\\src\\screens\\disenos\\boton3t.png')
  buttonDashBoard3 = create_button(menu_lateral, bg=color,image=imagen3)    
  buttonDashBoard3.pack() 
  imagen4 = tk.PhotoImage(file='c:\\Users\\VizcaIno\\Desktop\\proyecto-main\\src\\screens\\disenos\\boton4t.png')
  buttonDashBoard4 = create_button(menu_lateral, bg=color,image=imagen4)    
  buttonDashBoard4.pack()
  imagen5 = tk.PhotoImage(file='c:\\Users\\VizcaIno\\Desktop\\proyecto-main\\src\\screens\\disenos\\boton5t.png')
  buttonDashBoard5 = create_button(menu_lateral, bg=color,image=imagen5)    
  buttonDashBoard5.pack()
  imagen6 = tk.PhotoImage(file='c:\\Users\\VizcaIno\\Desktop\\proyecto-main\\src\\screens\\disenos\\boton6t.png')
  buttonDashBoard6 = create_button(menu_lateral, bg=color,image=imagen6)    
  buttonDashBoard6.pack()
        

        
  #fondo= Frame(root)
  #fondo.pack()
 # imagenfondo = tk.PhotoImage(file='C:\\Users\\USUARIO\\Downloads\\Nueva carpeta\\login\\\\disenos\\menu.png')    
  #etiquetafondo = tk.Label(fondo, image=imagenfondo)
 # etiquetafondo.pack()

  root.mainloop()