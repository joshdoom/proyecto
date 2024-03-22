import tkinter
from datetime import datetime
from tkinter import Tk, ttk, messagebox
from tkcalendar import DateEntry
from ttkthemes import ThemedStyle
from sqlalchemy.orm import Session
import customtkinter
from ..services.grado import Grado
from ..services.estudiante import Estudiante
from ..services.anioescolar import AnioEscolar
from ..models import Estudiante as Model
from ..models import Grado as ModelGrado
from ..models import AnioEscolar as ModelAnioEscolar
from ..engine import engine
from ..utils.table_to_pdf import PDFGrado
from ..utils.validate import is_number
from PIL import Image

grado = ["Primer", "Segundo", "Tercero", "Cuarto", "Quinto"]

def screen_grado(tk: tkinter, window: Tk, degree: int, rol: str):
    connect_grado = Grado(engine)
    connect_estudiante = Estudiante(engine)
    connect_anioescolar = AnioEscolar(engine)



    def verificar_rol():
        if rol == "Profesor":
            button_notas = customtkinter.CTkButton(master=window, width=95, height=37, text="Notas",
                                              text_color="#fff", fg_color="#0d487e", command=notas, font=("bold", 15),
                                              hover_color=blue)
            
            #tk.Button(window, text="Notas", command=notas, bg=verdeclaro, fg="black")
            
            button_notas.place(x=1000, y=295)
            
        elif rol == "Secretaria":
            #botonew = tk.PhotoImage(file='src/screens/disenos/botones/botonestablas/botonesnuevo.png')
            
            button_new = customtkinter.CTkButton(master=window, width=95, height=37, text="Nuevo",
                                              text_color="#fff", fg_color="#0d487e", command=nuevo, font=("bold", 15),
                                              hover_color=blue)
            
            button_new.place(x=640, y=295)

            button_save = customtkinter.CTkButton(master=window, width=95, height=37, text="Guardar",
                                              text_color="#fff", fg_color="#0d487e", command=guardar, font=("bold", 15),
                                              hover_color=blue)
            
            button_save.place(x=740, y=295)
            
            button_editar = customtkinter.CTkButton(master=window, width=95, height=37, text="Editar",
                                              text_color="#fff", fg_color="#0d487e", command=editar, font=(0, 15),
                                              hover_color=blue)
            
            button_editar.place(x=840, y=295)

            button_notas = customtkinter.CTkButton(master=window, width=95, height=37, text="Notas",
                                              text_color="#fff", fg_color="#0d487e", command=notas, font=(0, 15),
                                              hover_color=blue)
            button_notas.place(x=940, y=295)

            button_descargar = customtkinter.CTkButton(master=window, width=95, height=37, text="Descargar",
                                              text_color="#fff", fg_color="#0d487e", command=generar_pdf, font=(0, 15),
                                              hover_color=blue)
            
            button_descargar.place(x=1040, y=295)

        else:
            
            button_new = customtkinter.CTkButton(master=window, width=95, height=37, text="Nuevo",
                                              text_color="#fff", fg_color="#0d487e", command=nuevo, font=("bold", 15),
                                              hover_color=blue)
            button_new.place(x=640, y=295)

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

            button_notas = customtkinter.CTkButton(master=window, width=95, height=37, text="Notas",
                                              text_color="#fff", fg_color="#0d487e", command=notas, font=(0, 15),
                                              hover_color=blue)
            button_notas.place(x=1040, y=295)
            
            button_descargar = customtkinter.CTkButton(master=window, width=95, height=37, text="Descargar",
                                              text_color="#fff", fg_color="#0d487e", command=generar_pdf, font=(0, 15),
                                              hover_color=blue)
            button_descargar.place(x=1140, y=295)

            

    def update_table():
        for i in table.get_children():
            table.delete(i)
        
        with Session(engine) as session:
            estudiantes = session.query(Model).all()

            for estudiante in estudiantes:
                grado = session.query(ModelGrado).filter(ModelGrado.id_estudiante == estudiante.id, ModelGrado.inscrito == degree).first()
                anioescolar = session.query(ModelAnioEscolar).filter_by(id_estudiante=estudiante.id).first()
                seccion = "U"

                if grado is not None and anioescolar is not None:
                    table.insert('', 'end', values=(estudiante.id, estudiante.nombres, estudiante.apellidos, estudiante.cedula, estudiante.telefono, estudiante.fecha_nacimiento, grado.inscrito, seccion, anioescolar.inicio, anioescolar.fin))
                    
            table.pack(fill="both", expand=True)

    

    def show_students():
        global table
        


        frame = tk.Frame(window, bg="white", width="1400", height="200", bd=10)
        frame.pack(fill="both", expand=True)
        table = ttk.Treeview(frame, columns=('ID', 'Nombres', 'Apellidos', 'Cedula', 'Telefono', 'Fecha de Nacimiento', 'Grado', 'Seccion', 'Inicio', 'Fin'), show='headings')
        #table.tag_configure("odd", background=verdeclaro)
        #table.tag_configure("even",background="white")
        estilo_tablaA = ttk.Style()

        estilo_tablaA.configure("Treeview.Heading", background="#565b5e", foreground="#000",
                                                relief="flat", font=("Calisto mt", 13, "bold"))
        estilo_tablaA.configure("Treeview", font=("Arial", 12, "bold"))
    
        
        table.column('ID', width=70, anchor='center')
        table.column('Nombres', width=100, anchor='center')
        table.column('Apellidos', width=100, anchor='center')
        table.column('Cedula', width=100, anchor='center')
        table.column('Telefono', width=100, anchor='center')
        table.column('Fecha de Nacimiento', width=140, anchor='center')
        table.column('Grado', width=100, anchor='center')
        table.column('Seccion', width=100, anchor='center')
        table.column('Inicio', width=100, anchor='center')
        table.column('Fin', width=100, anchor='center')
        table.heading('ID', text='ID')
        table.heading('Nombres', text='Nombres')
        table.heading('Apellidos', text='Apellidos')
        table.heading('Cedula', text='Cedula')
        table.heading('Telefono', text='Telefono')
        table.heading('Fecha de Nacimiento', text='Fecha de Nacimiento')
        table.heading('Grado', text='Grado')
        table.heading('Seccion', text='Seccion')
        table.heading('Inicio', text='Inicio')
        table.heading('Fin', text='Fin')
        
        
                
        with Session(engine) as session:
            estudiantes = session.query(Model).all()

            for estudiante in estudiantes:
                grado = session.query(ModelGrado).filter(ModelGrado.id_estudiante == estudiante.id, ModelGrado.inscrito == degree).first()
                anioescolar = session.query(ModelAnioEscolar).filter_by(id_estudiante=estudiante.id).first()
                seccion = "U"

                if grado is not None and anioescolar is not None:
                    table.insert('', 'end', values=(estudiante.id, estudiante.nombres, estudiante.apellidos, estudiante.cedula, estudiante.telefono, estudiante.fecha_nacimiento, grado.inscrito, seccion, anioescolar.inicio, anioescolar.fin))

            
            table.pack(fill="both", expand=True)
   
    def nuevo():
        try:
            nombres = entries[0].get()
            apellidos = entries[1].get()
            cedula = entries[2].get()
            telefono = entries[3].get()
            fecha_nacimiento = datetime.strptime(entries[4].get(), '%m/%d/%y')
            inicio = datetime.strptime(entries[5].get(), '%m/%d/%y')
            fin = datetime.strptime(entries[6].get(), '%m/%d/%y')

            if not all([nombres, apellidos, cedula, telefono, fecha_nacimiento, inicio, fin]):
                messagebox.showerror("Error", "Todos los campos deben estar rellenos")
                return

            connect_estudiante.create(nombres, apellidos, cedula, telefono, fecha_nacimiento, 1)
            with Session(engine) as session:
                estudiante = session.query(Model).filter_by(cedula=cedula).first()
                connect_grado.create(degree, estudiante.id)
                connect_anioescolar.create(inicio, fin, estudiante.id)
            
            update_table()
            limpiar_campos()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminar():
        selected_item = table.selection()[0]
        selected_estudiante = table.item(selected_item)['values'][0]

        with Session(engine) as session:
            estudiante = session.query(Model).filter_by(id=selected_estudiante).first()
            anio_escolar = session.query(ModelAnioEscolar).filter_by(id_estudiante=estudiante.id).first()
            grado = session.query(ModelGrado).filter_by(id_estudiante=estudiante.id).first()

            connect_anioescolar.delete(anio_escolar.id)
            connect_grado.delete(grado.id)
            connect_estudiante.delete(estudiante.id)

        update_table()

    def editar():
        global selected_estudiante
        selected_item = table.selection()[0]
        selected_estudiante = table.item(selected_item)['values']
        omitir = selected_estudiante.pop(6)
        omitir = selected_estudiante.pop(6)
        for i, entry in enumerate(entries):
            if i >= 4:
                dt = datetime.strptime(selected_estudiante[i+1], "%Y-%m-%d %H:%M:%S")
                str_dt = dt.strftime('%m/%d/%y')
                entry.delete(0, 'end')
                entry.insert(0, str_dt)
            else:
                entry.delete(0, 'end')
                entry.insert(0, selected_estudiante[i+1])

    def guardar():
        try:
            nombres = entries[0].get()
            apellidos = entries[1].get()
            cedula = entries[2].get()
            telefono = entries[3].get()
            fecha_nacimiento = datetime.strptime(entries[4].get(), '%m/%d/%y')
            inicio = datetime.strptime(entries[5].get(), '%m/%d/%y')
            fin = datetime.strptime(entries[6].get(), '%m/%d/%y')

            if not all([nombres, apellidos, cedula, telefono, fecha_nacimiento, inicio, fin]):
                messagebox.showerror("Error", "Todos los campos deben estar rellenos")
                return

            with Session(engine) as session:
                estudiante = session.query(Model).filter_by(id=selected_estudiante[0]).first()
                anio_escolar = session.query(ModelAnioEscolar).filter_by(id_estudiante=estudiante.id).first()
                grado = session.query(ModelGrado).filter_by(id_estudiante=estudiante.id).first()

                connect_estudiante.update(estudiante.id, nombres, apellidos, cedula, telefono, fecha_nacimiento, 1)
                connect_anioescolar.update(anio_escolar.id, inicio, fin, estudiante.id)
                connect_grado.update(grado.id, degree, estudiante.id)

            update_table()
            limpiar_campos()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def limpiar_campos():
       for entry in entries:
            entry.config(validate="none")
            entry.delete(0, 'end')
            if entry in [entries[2], entries[3]]:
                entry.config(validate="key")
                
    def generar_pdf():
        from .vista_previa import screen_vista_previa

        pdf = PDFGrado('L', 'mm', 'A4')
        pdf.degree = degree
        pdf.add_page()
        pdf.set_font("Helvetica","", 10)

        with Session(engine) as session:
            estudiantes = session.query(Model).all()

            for estudiante in estudiantes:
                grado = session.query(ModelGrado).filter(ModelGrado.id_estudiante == estudiante.id, ModelGrado.inscrito == degree).first()
                anioescolar = session.query(ModelAnioEscolar).filter_by(id_estudiante=estudiante.id).first()
                seccion = "U"

                if grado is not None and anioescolar is not None:
                    datos = [estudiante.id, estudiante.nombres, estudiante.apellidos, estudiante.cedula, estudiante.telefono, estudiante.fecha_nacimiento, grado.inscrito, seccion, anioescolar.inicio, anioescolar.fin]
                    for dato in datos:
                        str_dato = str(dato)
                        if str_dato == str(datos[5]):
                            dt = datetime.strptime(str_dato, "%Y-%m-%d %H:%M:%S")
                            str_dt = dt.strftime('%m/%d/%y')
                            pdf.cell(40, 5, txt = str_dt, border=1, align = 'C')
                        elif str_dato == str(datos[8]) or str_dato == str(datos[9]):
                            dt = datetime.strptime(str_dato, "%Y-%m-%d %H:%M:%S")
                            str_dt = dt.strftime('%m/%d/%y')
                            pdf.cell(26, 5, txt = str_dt, border=1, align = 'C')
                        else:
                            pdf.cell(26, 5, txt = str_dato, border=1, align = 'C')
                    pdf.ln(5)
        pdf.output(f"src/pdfs/tabla_de_grado{degree}.pdf")
        
        screen_vista_previa(tkinter, window=tk.Toplevel(), ruta_pdf=f"src/pdfs/tabla_de_grado{degree}.pdf")
    
    def notas():
        from .notas import screen_notas
        window.destroy()
        screen_notas(tkinter, window=tk.Toplevel(), degree=degree, rol=rol)

    window.title(f"{grado[degree - 1]} año")
    window.geometry("1280x680")
    window.resizable(False, False)
    window.iconbitmap('src/screens/disenos/LUMASIS.ico')
    azul =  "#7beaf5"
    blue = "#288a94"
    verdeclaro="#287678"
    verde="#fff"
    window.config(bg=verdeclaro)

    icono= tk.PhotoImage(file='src/screens/disenos/urbaneja.png')
    
    cintillo = tk.Label(window, text="Registro de Estudiantes", bd=5, bg=verdeclaro, fg="white", 
                        font=("Calisto Mt", 16), padx=20, pady=10)
    cintillo.config(image=icono, compound=tk.LEFT)  # Establecer la imagen a la izquierda del texto
    cintillo.image = icono 
    cintillo.pack(side="top")
    
    miFrame = tk.Frame(window, width="1200", height="250", bd=5, bg="#287678")
    miFrame.pack()
    
    
    style = ThemedStyle (window) # Cargar el archivo de estilo personalizado
    style.set_theme("adapta")
    
    pizarra = tk.PhotoImage(file='imagen.png')
    cosa = tk.Label(miFrame, image=pizarra, width="1200", height="250")
    #cosa.config(image=pizarra)
    cosa.place(x=0, y=0)
    cosa.image = pizarra
   
    if not rol == 'Profesor':
        vcomd_t = window.register(lambda value: is_number(value, max_lenght=11))
        vcomd_c = window.register(lambda value: is_number(value, max_lenght=8))
        
        labels = ["Nombres", "Apellidos", "Cedula", "Telefono", "Fecha de Nacimiento", "Inicio", "Fin"]

        entries = [
            tk.Entry(window, validate='key', validatecommand=(vcomd_t, '%P'), font=("Calisto Mt", 16))
            if label == "Telefono" else
            tk.Entry(window, validate='key', validatecommand=(vcomd_c, '%P'), font=("Calisto Mt", 16))
            if label == "Cedula" else
            tk.Entry(window, font=("Calisto Mt", 16))
            if label not in ["Fecha de Nacimiento", "Inicio", "Fin"] else
            DateEntry(window)
            for label in labels
        ]
            

        for i, (label, entry) in enumerate(zip(labels, entries)):
            if i < 4:  # Para los primeros cuatro labels y entries
                tt = customtkinter.CTkLabel(master=miFrame, text=label, width=120, height=25,
                                                fg_color="#287678", text_color="#fff", corner_radius=8,
                                                font=customtkinter.CTkFont(size=18, weight="bold"))
                
                tt.place(x=180, y=30+i*50)
                
                entry.place(x=360, y=125+i*50+7)
                
            else:  # Para los siguientes labels y entries
                tt = customtkinter.CTkLabel(master=miFrame, text=label, width=120, height=25,
                                                fg_color="#287678", text_color="#fff", corner_radius=8,
                                                font=customtkinter.CTkFont(size=18,))
                
                tt.place(x=570, y=30+(i-4)*50)
                
                entry.place(x=810, y=120+(i-4)*50+7)

        


    verificar_rol()
    show_students()