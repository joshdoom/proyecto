import tkinter
from tkinter import Tk, ttk, messagebox
from ttkthemes import ThemedStyle
from sqlalchemy.orm import Session
import customtkinter
from ..services.profesor import Profesor
from ..services.materias import Materias
from ..models import Profesor as Model
from ..models import Materias as ModelMaterias
from ..engine import engine
from ..utils.validate import is_number

def screen_professor(tk: tkinter, window: Tk, rol: str):
    connect = Profesor(engine)
    connect_materias = Materias(engine)

    def update_table():
        for i in table.get_children():
            table.delete(i)
        
        with Session(engine) as session:
            professores = session.query(Model).all()
            for profesor in professores:
                table.insert('', 'end', values=(profesor.id, profesor.nombres, profesor.apellidos, profesor.cedula, profesor.telefono, profesor.titulo, profesor.id_materia))
        table.pack(fill="both", expand=True)

    def show_professores():
        
        global table
        frame = tk.Frame(window, bg="white", width="1400", height="200", bd=10)
        frame.pack(fill="both", expand=True)
        table = ttk.Treeview(frame, columns=('ID', 'Nombres', 'Apellidos', 'Cedula', 'Telefono', 'Titulo', 'ID Materia'), show='headings')
        estilo_tablaB = ttk.Style()

        estilo_tablaB.configure("Treeview.Heading", background="#565b5e", foreground="#000",
                                                relief="flat", font=("Calisto mt", 13, "bold"))
        estilo_tablaB.configure("Treeview", font=("Arial", 12, "bold"))
        table = ttk.Treeview(frame, columns=('ID', 'Nombres', 'Apellidos', 'Cedula', 'Telefono', 'Titulo', 'ID Materia'), show='headings')
        table.column('ID', width=100, anchor='center')
        table.column('Nombres', width=100, anchor='center')
        table.column('Apellidos', width=100, anchor='center')
        table.column('Cedula', width=100, anchor='center')
        table.column('Telefono', width=100, anchor='center')
        table.column('Titulo', width=100, anchor='center')
        table.column('ID Materia', width=100, anchor='center')
        table.heading('ID', text='ID')
        table.heading('Nombres', text='Nombres')
        table.heading('Apellidos', text='Apellidos')
        table.heading('Cedula', text='Cedula')
        table.heading('Telefono', text='Telefono')
        table.heading('Titulo', text='Titulo')
        table.heading('ID Materia', text='ID Materia')
        
        with Session(engine) as session:
            professores = session.query(Model).all()
            for profesor in professores:
                table.insert('', 'end', values=(profesor.id, profesor.nombres, profesor.apellidos, profesor.cedula, profesor.telefono, profesor.titulo, profesor.id_materia))
        table.pack(fill="both", expand=True)

    def nuevo():
        try:
            nombres = entries[0].get()
            apellidos = entries[1].get()
            cedula = entries[2].get()
            telefono = entries[3].get()
            titulo = MateriaAsignada.get()
            grado = Grado.get()

            if not all([nombres, apellidos, cedula, telefono, titulo, grado]):
                messagebox.showerror("Error", "Todos los campos deben estar rellenos")
                return

            with Session(engine) as session:
                connect_materias.create(titulo[0].upper(), titulo, None, grado)
                materia = session.query(ModelMaterias).filter(ModelMaterias.nombre == titulo, ModelMaterias.id_grado == grado).first()
                
            connect.create(nombres, apellidos, cedula, telefono, titulo, materia.id)
            limpiar_campos()
            update_table()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminar():
        selected_item = table.selection()[0]
        selected_profesor = table.item(selected_item)['values'][0]

        connect.delete(selected_profesor)
        update_table()

    def editar():
        global selected_profesor 
        selected_item = table.selection()[0]
        selected_profesor = table.item(selected_item)['values']
        for i, entry in enumerate(entries):
            entry.delete(0, 'end')
            entry.insert(0, selected_profesor[i+1])

    def guardar():
        try:
            id, nombres, apellidos, cedula, telefono, titulo, id_materia = selected_profesor
            nombres = entries[0].get()
            apellidos = entries[1].get()
            cedula = entries[2].get()
            telefono = entries[3].get()
            titulo = MateriaAsignada.get()
            grado = Grado.get()

            if not all([nombres, apellidos, cedula, telefono, titulo, grado]):
                messagebox.showerror("Error", "Todos los campos deben estar rellenos")
                return

            with Session(engine) as session:
                materia = session.query(ModelMaterias).filter(ModelMaterias.nombre == titulo, ModelMaterias.id_grado == grado).first()
                if not materia:
                    connect_materias.create(titulo[0].upper(), titulo, None, grado)
                    materia = session.query(ModelMaterias).filter(ModelMaterias.nombre == titulo, ModelMaterias.id_grado == grado).first()
                
            connect.update(id, nombres, apellidos, cedula, telefono, titulo, materia.id)
            limpiar_campos()
            update_table()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def limpiar_campos():
        for entry in entries:
            entry.config(validate="none")
            entry.delete(0, 'end')
            if entry in [entries[2], entries[3]]:
                entry.config(validate="key")

    window.title("Profesores")
    window.geometry("1280x680")
    window.resizable(False, False)
    window.iconbitmap('src/screens/disenos/LUMASIS.ico')
    azul =  "#7beaf5"
    blue = "#288a94"
    verdeclaro = "#287678"
    window.config(bg=verdeclaro)

    icono= tk.PhotoImage(file='src/screens/disenos/urbaneja.png')
    cintillo = tk.Label(window, text="Registros de Profesores",bd=5, bg=verdeclaro, fg="#fff", 
                        font=("Calisto Mt", 16), padx=20, pady=10)
    cintillo.config(image=icono, compound=tk.LEFT)  # Establecer la imagen a la izquierda del texto
    cintillo.image = icono 
    cintillo.pack(side="top")


    miFrame = tk.Frame(window, width="1200", height="250", bd=5, bg="#287678")
    miFrame.pack()

    pizara = tk.PhotoImage(file='imagen.png')
    imagen = tk.Label(miFrame, image=pizara, width="1200", height="250")
    #cosa.config(image=pizarra)
    imagen.place(x=0, y=0)
    imagen.image = pizara
    
    style = ThemedStyle (window) # Cargar el archivo de estilo personalizado
    style.set_theme("adapta")

    vcomd_t = window.register(lambda value: is_number(value, max_lenght=11))
    vcomd_c = window.register(lambda value: is_number(value, max_lenght=8))
    labels = ["Nombres", "Apellidos", "Cedula", "Telefono", "Materia Asignada", "Grado"]
    
    entries = [
        tk.Entry(window, validate='key', validatecommand=(vcomd_t, '%P'), font=("Calisto Mt", 16))
        if label == "Telefono" else
        tk.Entry(window, validate='key', validatecommand=(vcomd_c, '%P'), font=("Calisto Mt", 16))
        if label == "Cedula" else
        tk.Entry(window,  font=("Calisto Mt", 16)) 
        for label in labels
    ]
    #entries = [customtkinter.CTkEntry(master=miFrame, width=150, height=30, border_width=0, corner_radius=10, font=(0, 16), 
     #                   validate=vals, validatecommand=(vcomd, '%P'), ) if label in ["Cedula", "Telefono"] else customtkinter.CTkEntry(master=miFrame,  width=150, height=30, border_width=0, corner_radius=10, font=(0, 16)) 
      #                  for label in labels]
    
    #[tk.Entry(window, validate='key', validatecommand=(vcomd, '%P')) if label in ["Cedula", "Telefono"] else tk.Entry(window) for label in labels]

    for i, (label, entry) in enumerate(zip(labels, entries)):
       
        if i < 4:  # Para los primeros cuatro labels y entries
            
            tl = customtkinter.CTkLabel(master=miFrame, text=label, width=120, height=25,
                                               fg_color="#287678", text_color="#fff", corner_radius=8,
                                               font=customtkinter.CTkFont(size=18))
            
            tl.place(x=190, y=30+i*50)
            
            entry.place(x=370, y=125+i*50+7)
            
            #tk.Label(miFrame, text=label).place(x=350, y=30+i*50)
            #entry.place(x=455, y=125+i*50+7)
       
        elif i == 4:  # Para el quinto label y entry
            MateriaAsignada = tk.StringVar(miFrame)
            MateriaAsignada.set("Materias")
            opciones = ["Arte y patrimonio", "Castellano", "Ciencias Naturales", "Educacion Fisica", "G.H.C", "Ingles", "Matematicas", "Orientación y convivencia", "G.E.R.P", "Fisica", "Quimica"]
            opcion = tk.OptionMenu(miFrame, MateriaAsignada, *opciones)
            opcion.place(x=820, y=70+(i-4)*50+7)
       
        else:  # Para el sexto label y entry
            Grado = tk.StringVar(miFrame)
            Grado.set("Grados")
            grados = [str(i) for i in range(1, 6)]
            opcion_grado = tk.OptionMenu(miFrame, Grado, *grados)
            opcion_grado.place(x=720, y=20+(i-4)*50+7)


    bc = "#0d487e" 
    
    button_new = customtkinter.CTkButton(master=window, width=95, height=37, text="Nuevo",
                                              text_color="#fff", fg_color=bc, command=nuevo, font=(0, 15),
                                              hover_color=blue)
    
    #tk.Button(window, text="Nuevo", command=nuevo, bg=bc, fg="#fff")
    button_new.place(x=680, y=295)

    button_save = customtkinter.CTkButton(master=window, width=95, height=37, text="Guardar",
                                              text_color="#fff", fg_color=bc, command=guardar, font=(0, 15),
                                              hover_color=blue)
    
    #tk.Button(window, text="Guardar", command=guardar, bg=bc, fg="#fff")
   
    button_save.place(x=780, y=295)

    
    button_editar = customtkinter.CTkButton(master=window, width=95, height=37, text="Editar",
                                              text_color="#fff", fg_color="#0d487e", command=editar, font=(0, 15),
                                              hover_color=blue)
            
    button_editar.place(x=880, y=295)
    
    
    button_delete = customtkinter.CTkButton(master=window, width=95, height=37, text="Eliminar",
                                              text_color="#fff", fg_color=bc, command=eliminar, font=(0, 15),
                                              hover_color=blue)
    
    #tk.Button(window, text="Eliminar", command=Eliminar, bg=bc, fg="#fff")
 
    button_delete.place(x=980, y=295)


    show_professores()