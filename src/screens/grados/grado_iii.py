import tkinter
from datetime import datetime
from tkinter import Tk, ttk
from tkcalendar import DateEntry
from sqlalchemy.orm import Session

from ...services.grado import Grado
from ...services.estudiante import Estudiante
from ...services.anioescolar import AnioEscolar
from ...models import Estudiante as Model
from ...models import Grado as ModelGrado
from ...models import AnioEscolar as ModelAnioEscolar
from ...engine import engine


def screen_grado_iii(tk: tkinter, window: Tk):
    connect_grado = Grado(engine)
    connect_estudiante = Estudiante(engine)
    connect_anioescolar = AnioEscolar(engine)

    def update_table():
        for i in table.get_children():
            table.delete(i)
        
        with Session(engine) as session:
            estudiantes = session.query(ModelGrado).filter_by(inscrito=1).all()

            for x in estudiantes:
                estudiante = session.query(Model).filter_by(id=x.id_estudiante).first()
                anioescolar = session.query(ModelAnioEscolar).filter_by(id_estudiante=x.id_estudiante).first()
                seccion = "U"

                table.insert('', 'end', values=(estudiante.id, estudiante.nombres, estudiante.apellidos, estudiante.cedula, estudiante.telefono, estudiante.fecha_nacimiento, x.inscrito, seccion, anioescolar.fin))
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
            estudiantes = session.query(ModelGrado).filter_by(inscrito=3).all()

            for x in estudiantes:
                estudiante = session.query(Model).filter_by(id=x.id_estudiante).first()
                anioescolar = session.query(ModelAnioEscolar).filter_by(id_estudiante=x.id_estudiante).first()
                seccion = "U"

                table.insert('', 'end', values=(estudiante.id, estudiante.nombres, estudiante.apellidos, estudiante.cedula, estudiante.telefono, estudiante.fecha_nacimiento, x.inscrito, seccion, anioescolar.inicio, anioescolar.fin))
        table.pack(fill="both", expand=True)
   
    def nuevo():
        nombres = entries[0].get()
        apellidos = entries[1].get()
        cedula = entries[2].get()
        telefono = entries[3].get()
        fecha_nacimiento = datetime.strptime(entries[4].get(), '%m/%d/%y')
        grado = entries[5].get()
        seccion = entries[6].get()
        inicio = datetime.strptime(entries[7].get(), '%m/%d/%y')
        fin = datetime.strptime(entries[8].get(), '%m/%d/%y')

        connect_estudiante.create(nombres, apellidos, cedula, telefono, fecha_nacimiento, 1)
        with Session(engine) as session:
            estudiante = session.query(Model).filter_by(cedula=cedula).first()
            connect_grado.create(grado, estudiante.id)
            connect_anioescolar.create(inicio, fin, estudiante.id)
        
        update_table()

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
        for i, entry in enumerate(entries):
            entry.delete(0, 'end')
            entry.insert(0, selected_estudiante[i+1])

    def guardar():
        nombres = entries[0].get()
        apellidos = entries[1].get()
        cedula = entries[2].get()
        telefono = entries[3].get()
        fecha_nacimiento = datetime.strptime(entries[4].get(), '%m/%d/%y')
        inscrito = entries[5].get()
        seccion = entries[6].get()
        inicio = datetime.strptime(entries[7].get(), '%m/%d/%y')
        fin = datetime.strptime(entries[8].get(), '%m/%d/%y')

        with Session(engine) as session:
            estudiante = session.query(Model).filter_by(id=selected_estudiante[0]).first()
            anio_escolar = session.query(ModelAnioEscolar).filter_by(id_estudiante=estudiante.id).first()
            grado = session.query(ModelGrado).filter_by(id_estudiante=estudiante.id).first()

            connect_estudiante.update(estudiante.id, nombres, apellidos, cedula, telefono, fecha_nacimiento, 1)
            connect_anioescolar.update(anio_escolar.id, inicio, fin, estudiante.id)
            connect_grado.update(grado.id, inscrito, estudiante.id)

        update_table()


    window.title("Tercero año")
    window.geometry("1280x680")
    window.resizable(False, False)

    miFrame = tk.Frame(window, width="1200", height="250", bd=5)
    miFrame.pack()

    labels = ["Nombres", "Apellidos", "Cedula", "Telefono", "Fecha de Nacimiento", "Grado", "Seccion", "Inicio", "Fin"]
    entries = [tk.Entry(window) if label not in ["Fecha de Nacimiento", "Inicio", "Fin"] else DateEntry(window) for label in labels]

    for i, (label, entry) in enumerate(zip(labels, entries)):
        if i < 4:  # Para los primeros cuatro labels y entries
            tk.Label(miFrame, text=label).place(x=150, y=i*50)
            entry.place(x=255, y=i*50+7)
        else:  # Para los siguientes labels y entries
            tk.Label(miFrame, text=label).place(x=450, y=(i-4)*50)
            entry.place(x=555, y=(i-4)*50+7)


    button_new = tk.Button(window, text="Nuevo", command=nuevo, bg="white", fg="black")
    button_new.pack()
    button_new.place(x=600, y=210)

    button_save = tk.Button(window, text="Guardar", command=guardar, bg="white", fg="black")
    button_save.pack()
    button_save.place(x=800, y=210)

    button_delete = tk.Button(window, text="Eliminar", command=eliminar, bg="white", fg="black")
    button_delete.pack()
    button_delete.place(x=700, y=210)

    miFrame13 = tk.Frame(window, width="1200", height="350", bd=1)
    miFrame13.pack(side="bottom", anchor="w")

    tk.Button(miFrame13, text="Editar", command=editar, bg="white").pack()

    miFramemenu = tk.Frame(window, width="10", height="35", bd=1, relief="raised")
    miFramemenu.place(x=1010, y=210)

    var = tk.StringVar(window)
    var.set("Materias")
    opciones = ["Arte y patrimonio", "Castellano", "Ciencias Naturales", "Educacion Fisica", "Geografía, historia y ciudadanía (GHC)", "Ingles", "Matematicas", "Orientación y convivencia", "Participación en grupos de creación, recreación y producción (G.E.R.P)", "Fisica", "Quimica"]
    opcion = tk.OptionMenu(miFramemenu, var, *opciones)
    opcion.config(width=15, bg="white", fg="black", font=("Arial Black", 10))
    opcion.pack()

    show_students()