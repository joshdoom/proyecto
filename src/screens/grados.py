import tkinter
from datetime import datetime
from tkinter import Tk, ttk
from tkcalendar import DateEntry
from sqlalchemy.orm import Session

from ..services.grado import Grado
from ..services.estudiante import Estudiante
from ..services.anioescolar import AnioEscolar
from ..models import Estudiante as Model
from ..models import Grado as ModelGrado
from ..models import AnioEscolar as ModelAnioEscolar
from ..engine import engine

grado = ["Primer", "Segundo", "Tercero", "Cuarto", "Quinto"]

def screen_grado(tk: tkinter, window: Tk, degree: int):
    connect_grado = Grado(engine)
    connect_estudiante = Estudiante(engine)
    connect_anioescolar = AnioEscolar(engine)

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

        frame = tk.Frame(window, bg="white", width="1400", height="350", bd=10)
        frame.pack(fill="both", expand=True)
        table = ttk.Treeview(frame, columns=('ID', 'Nombres', 'Apellidos', 'Cedula', 'Telefono', 'Fecha de Nacimiento', 'Grado', 'Seccion', 'Inicio', 'Fin'), show='headings')
        table.column('ID', width=100, anchor='center')
        table.column('Nombres', width=100, anchor='center')
        table.column('Apellidos', width=100, anchor='center')
        table.column('Cedula', width=100, anchor='center')
        table.column('Telefono', width=100, anchor='center')
        table.column('Fecha de Nacimiento', width=100, anchor='center')
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
        nombres = entries[0].get()
        apellidos = entries[1].get()
        cedula = entries[2].get()
        telefono = entries[3].get()
        fecha_nacimiento = datetime.strptime(entries[4].get(), '%m/%d/%y')
        inicio = datetime.strptime(entries[5].get(), '%m/%d/%y')
        fin = datetime.strptime(entries[6].get(), '%m/%d/%y')

        connect_estudiante.create(nombres, apellidos, cedula, telefono, fecha_nacimiento, 1)
        with Session(engine) as session:
            estudiante = session.query(Model).filter_by(cedula=cedula).first()
            connect_grado.create(degree, estudiante.id)
            connect_anioescolar.create(inicio, fin, estudiante.id)
        
        update_table()
        limpiar_campos()

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
        nombres = entries[0].get()
        apellidos = entries[1].get()
        cedula = entries[2].get()
        telefono = entries[3].get()
        fecha_nacimiento = datetime.strptime(entries[4].get(), '%m/%d/%y')
        inicio = datetime.strptime(entries[5].get(), '%m/%d/%y')
        fin = datetime.strptime(entries[6].get(), '%m/%d/%y')

        with Session(engine) as session:
            estudiante = session.query(Model).filter_by(id=selected_estudiante[0]).first()
            anio_escolar = session.query(ModelAnioEscolar).filter_by(id_estudiante=estudiante.id).first()
            grado = session.query(ModelGrado).filter_by(id_estudiante=estudiante.id).first()

            connect_estudiante.update(estudiante.id, nombres, apellidos, cedula, telefono, fecha_nacimiento, 1)
            connect_anioescolar.update(anio_escolar.id, inicio, fin, estudiante.id)
            connect_grado.update(grado.id, 233333333333333, estudiante.id)

        update_table()
        limpiar_campos()

    def limpiar_campos():
        for entry in entries:
            entry.delete(0, 'end')

    def notas():
        from .notas import screen_notas
        window.destroy()
        screen_notas(tkinter, window=tk.Toplevel(), degree=degree)

    window.title(f"{grado[degree - 1]} año")
    window.geometry("1280x680")
    window.resizable(False, False)
    window.iconbitmap('C:\\Users\\VizcaIno\\Desktop\\proyecto-main\\src\\screens\\disenos\\LUMASIS.ico')
    verdeclaro="#b8f2ca"
    verde="#15a35b"
    window.config(bg=verdeclaro)

    miFrame = tk.Frame(window, width="1200", height="250", bd=5)
    miFrame.pack()

    labels = ["Nombres", "Apellidos", "Cedula", "Telefono", "Fecha de Nacimiento", "Inicio", "Fin"]
    entries = [tk.Entry(window) if label not in ["Fecha de Nacimiento", "Inicio", "Fin"] else DateEntry(window) for label in labels]

    for i, (label, entry) in enumerate(zip(labels, entries)):
        if i < 4:  # Para los primeros cuatro labels y entries
            tk.Label(miFrame, text=label).place(x=150, y=i*50)
            entry.place(x=255, y=i*50+7)
        else:  # Para los siguientes labels y entries
            tk.Label(miFrame, text=label).place(x=450, y=(i-4)*50)
            entry.place(x=655, y=(i-4)*50+7)


    button_new = tk.Button(window, text="Nuevo", command=nuevo, bg=verdeclaro, fg="black")
    button_new.pack()
    button_new.place(x=750, y=210)

    button_save = tk.Button(window, text="Guardar", command=guardar, bg=verdeclaro, fg="black")
    button_save.pack()
    button_save.place(x=850, y=210)

    button_delete = tk.Button(window, text="Eliminar", command=eliminar, bg=verdeclaro, fg="black")
    button_delete.pack()
    button_delete.place(x=950, y=210)

    button_notas = tk.Button(window, text="Notas", command=notas, bg=verdeclaro, fg="black")
    button_notas.pack()
    button_notas.place(x=1050, y=210)

    button_descargar = tk.Button(window, text="Descargar", command=notas, bg=verdeclaro, fg="black")
    button_descargar.pack()
    button_descargar.place(x=1150, y=210)

    miFrame13 = tk.Frame(window, width="1200", height="350", bd=1)
    miFrame13.pack(side="bottom", anchor="w")

    tk.Button(miFrame13, text="Editar", command=editar, bg=verdeclaro).pack()

    

   

    show_students()