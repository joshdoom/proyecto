from datetime import datetime
import tkinter
from tkinter import Tk, ttk, messagebox, Canvas, Scrollbar
from ttkthemes import ThemedStyle
import customtkinter
from sqlalchemy.orm import Session

from ..services.register import Usuario as ServiceUsuario
from ..models import Usuario
from ..engine import engine

def screen_superusuario(tk: tkinter, window: Tk):
    connect = ServiceUsuario(engine)

    def update_table():
        for i in table.get_children():
            table.delete(i)
        
        with Session(engine) as session:
            users = session.query(Usuario).all()
            for user in users:
                table.insert('', 'end', values=(user.id, user.nombre, user.contrasena, user.rol))
            table.pack(fill="both", expand=True)

    def show_users():
        global table

        scroll_canvas = Canvas(window, background='#3a7ff6')
        scroll_canvas.pack(side='left', fill='both', expand=True)

        scrollbar = Scrollbar(window, command=scroll_canvas.yview)
        scrollbar.pack(side='left', fill='y')

        scroll_canvas.configure(yscrollcommand=scrollbar.set)
        scroll_canvas.bind('<Configure>', lambda e: scroll_canvas.configure(scrollregion=scroll_canvas.bbox('all')))

        frame = tk.Frame(scroll_canvas, bg="white", width="1400", height="200", bd=10)
        frame.pack(fill="both", expand=True)
        table = ttk.Treeview(frame, columns=('ID', 'Nombre de Usuario', 'Clave', 'Rol'), show='headings')
        estilo_tablaA = ttk.Style()

        estilo_tablaA.configure("Treeview.Heading", background="#565b5e", foreground="#000",
                                                relief="flat", font=("Calisto mt", 13, "bold"))
        estilo_tablaA.configure("Treeview", font=("Arial", 12, "bold"))
    
        table.column('ID', width=50, anchor='center')
        table.column('Nombre de Usuario', width=100, anchor='center')
        table.column('Clave', width=100, anchor='center')
        table.column('Rol', width=100, anchor='center')
        table.heading('ID', text='ID')
        table.heading('Nombre de Usuario', text='Nombre de Usuario')
        table.heading('Clave', text='Clave')
        table.heading('Rol', text='Rol')
                
        with Session(engine) as session:
            users = session.query(Usuario).all()
            for user in users:
                table.insert('', 'end', values=(user.id, user.nombre, user.contrasena, user.rol))
            table.pack(fill="both", expand=True)

    def eliminar():
        selected_item = table.selection()[0]
        selected_user = table.item(selected_item)['values'][0]

        connect.delete(selected_user)
        update_table()

    def editar():
        global selected_user
        selected_item = table.selection()[0]
        selected_user = table.item(selected_item)['values']
        
        for i, entry in enumerate(entries):
            entry.delete(0, 'end')
            entry.insert(0, selected_user[i+1])

    def guardar():
        try:
            username = entries[0].get()
            password = entries[1].get()

            if not all([username, password]):
                messagebox.showerror("Error", "Todos los campos deben estar rellenos")
                return

            connect.update(selected_user[0], username, password)

            update_table()
            limpiar_campos()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def limpiar_campos():
       for entry in entries:
            entry.config(validate="none")
            entry.delete(0, 'end')
                
    window.title("Lista de usuarios")
    window.geometry("1280x680")
    window.resizable(False, False)
    window.iconbitmap('src/screens/disenos/LUMASIS.ico')
    azul =  "#7beaf5"
    blue = "#288a94"
    verdeclaro="#287678"
    verde="#fff"
    window.config(bg=verdeclaro)

    icono= tk.PhotoImage(file='src/screens/disenos/urbaneja.png')
    
    cintillo = tk.Label(window, text="Lista de Usuarios", bd=5, bg=verdeclaro, fg="white", 
                        font=("Calisto Mt", 16), padx=20, pady=10)
    cintillo.config(image=icono, compound=tk.LEFT)  # Establecer la imagen a la izquierda del texto
    cintillo.image = icono 
    cintillo.pack(side="top")
    
    miFrame = tk.Frame(window, width="1200", height="250", bd=5, bg="#287678")
    miFrame.pack()
    
    
    style = ThemedStyle (window) 
    style.set_theme("adapta")
    
    pizarra = tk.PhotoImage(file='imagen.png')
    cosa = tk.Label(miFrame, image=pizarra, width="1200", height="250")
    cosa.place(x=0, y=0)
    cosa.image = pizarra
   

    labels = ["Username", "Contraseña"]

    entries = [
        tk.Entry(window, font=("Calisto Mt", 16))
        for label in labels
    ]
            

    for i, (label, entry) in enumerate(zip(labels, entries)):
        tt = customtkinter.CTkLabel(master=miFrame, text=label, width=120, height=25,
                                                fg_color="#287678", text_color="#fff", corner_radius=8,
                                                font=customtkinter.CTkFont(size=18, weight="bold"))
                
        tt.place(x=180, y=30+i*50)
        entry.place(x=360, y=125+i*50+7)
        
    button_save = customtkinter.CTkButton(master=window, width=95, height=37, text="Guardar",
                                              text_color="#fff", fg_color="#0d487e", command=guardar, font=("bold", 15),
                                              hover_color=blue)
    button_save.place(x=740, y=295)

    button_editar = customtkinter.CTkButton(master=window, width=95, height=37, text="Editar",
                                                    text_color="#fff", fg_color="#0d487e", command=editar, font=(0, 15),
                                                    hover_color=blue)            
    button_editar.place(x=840, y=295)
                    
    button_delete = customtkinter.CTkButton(master=window, width=95, height=37, text="Eliminar",
                                                    text_color="#fff", fg_color="#0d487e", command=eliminar, font=(0, 15),
                                                    hover_color=blue)
    button_delete.place(x=940, y=295)
    show_users()