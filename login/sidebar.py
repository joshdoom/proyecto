from tkinter import *


    

def josh():
    root.destroy()
    from grado1 import primero
    primero()
    
    
     

root=Tk()
root.title("sam")
root.geometry("650x650")
color = "#aeb6bf" 


class barra_superior():
    barra_superior= Frame(root)
    barra_superior.config(bg="black",height=50)
    barra_superior.pack(side=TOP, fill="both")

    botonmenu= Button(barra_superior, text="menu")
    botonmenu.pack(side=LEFT)


    

    

class menu_lateral():
    menu_lateral= Frame(root)
    menu_lateral.config(bg=color,width="100",height=150)
    menu_lateral.pack(side="left", fill="both",expand=False)

    buttonDashBoard = Button(menu_lateral,text="Primer año",command=josh)    
    buttonDashBoard.pack(side=TOP)    
    buttonProfile = Button(menu_lateral,text="Segundo año")  
    buttonProfile.pack()      
    buttonPicture = Button(menu_lateral,text="Tercero año")
    buttonPicture.pack()
    buttonInfo = Button(menu_lateral,text="Cuarto año")  
    buttonInfo.pack()      
    buttonSettings = Button(menu_lateral,text="Quinto año")
    buttonSettings.pack()






root.mainloop()