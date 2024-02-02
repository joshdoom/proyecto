import tkinter
from datetime import datetime
from tkinter import Tk, ttk
from sqlalchemy.orm import Session

from ..services.estudiante import Estudiante
from ..services.materias import Materias
from ..services.nota import Nota
from ..services.lapso import Lapso
from ..models import Estudiante as Model, Materias as ModelMaterias, Nota as ModelNotas, Lapso as ModelLapso
from ..engine import engine


def screen_notas(tk: tkinter, window: Tk, degree: int=5):
    table = ttk.Treeview(window, columns=('ID', 'Nombre del estudiante', 'Cedula', 'Materia', 'Nota', 'Lapso'))
    table.pack()
    table.heading('ID', text='ID')
    table.heading('Nombre del estudiante', text='Nombre del estudiante')
    table.heading('Cedula', text='Cedula')
    table.heading('Materia', text='Materia')
    table.heading('Nota', text='Nota')
    table.heading('Lapso', text='Lapso')

    def show_notas(estudiante, materias):
        with Session(engine) as session:
            for materia in materias:
                notas = session.query(ModelNotas).filter_by(id_estudiante=estudiante.id, id_materia=materia.id).all()
                for nota in notas:
                    lapso = session.query(ModelLapso).filter_by(nota_id=nota.id).first()
                    table.insert('', 'end', text=estudiante.nombres, values=(estudiante.id, estudiante.cedula, materia.nombre, nota.total, f'{lapso.inicio} - {lapso.fin}'))

    def buscar():
        with Session(engine) as session:
            select_by_cedula = entryCedula.get()
            estudiante = session.query(Model).filter_by(cedula=select_by_cedula).first()

            if estudiante is not None:
                materias = session.query(ModelMaterias).filter_by(id_grado=degree).all()
                show_notas(estudiante, materias)

    def nuevo():
        # Capturar los valores ingresados
        nota = entryNota.get()
        materia = materiaSeleccionada.get()

        # Aquí puedes agregar el código para agregar una nueva nota con los valores capturados
        print(f'Nota: {nota}, Materia: {materia}')

    def guardar():
        # Aquí va el código para guardar las notas
        pass

    def eliminar():
        # Aquí va el código para eliminar una nota
        pass

    window.title("Control de Notas")
    window.geometry("1280x680")
    window.config(bd=20)
    window.resizable(False, False)

    miFrame = tk.Frame(window, width=1200, height=250, bd=5, relief="groove")
    miFrame.pack()

    botonNuevo = tk.Button(miFrame, text="Nuevo", bg="white", fg="black", command=nuevo)
    botonNuevo.pack(side='left', padx=5, pady=5)

    botonGuardar = tk.Button(miFrame, text="Guardar", bg="white", fg="black", command=guardar)
    botonGuardar.pack(side='left', padx=5, pady=5)

    botonEliminar = tk.Button(miFrame, text="Eliminar", bg="white", fg="black", command=eliminar)
    botonEliminar.pack(side='left', padx=5, pady=5)

    botonBuscar = tk.Button(miFrame, text="Buscar", bg="white", fg="black", command=buscar)
    botonBuscar.pack(side='left', padx=5, pady=5)

    labelNota = tk.Label(miFrame, text="Total de la nota:")
    labelNota.pack(side='left', padx=5, pady=5)

    entryNota = tk.Entry(miFrame)
    entryNota.pack(side='left', padx=5, pady=5)

    labelCedula = tk.Label(miFrame, text="Cedula:")
    labelCedula.pack(side='left', padx=5, pady=5)

    entryCedula = tk.Entry(miFrame)
    entryCedula.pack(side='left', padx=5, pady=5)

    labelMateria = tk.Label(miFrame, text="Materia:")
    labelMateria.pack(side='left', padx=5, pady=5)

    materias = ["Arte y patrimonio", "Castellano", "Ciencias Naturales", "Educacion Fisica", "Geografía, historia y ciudadanía (GHC)", "Ingles", "Matematicas", "Orientación y convivencia ", "Participación en grupos de creación, recreación y producción (G.E.R.P)"]
    materiaSeleccionada = tk.StringVar()
    materiaSeleccionada.set('Materias')
    menuMaterias = tk.OptionMenu(miFrame, materiaSeleccionada, *materias)
    menuMaterias.pack(side='left', padx=5, pady=5)

    labelNota = tk.Label(miFrame, text="Notas:")
    labelNota.pack(side='left', padx=5, pady=5)

    notas = [1, 2, 3, 4]
    notasSeleccionada = tk.StringVar()
    notasSeleccionada.set('Notas')
    menuNotas = tk.OptionMenu(miFrame, notasSeleccionada, *notas)
    menuNotas.pack(side='left', padx=5, pady=5)

    labelLapso = tk.Label(miFrame, text="Lapso:")
    labelLapso.pack(side='left', padx=5, pady=5)

    lapso = [1, 2, 3]
    lapsosSeleccionada = tk.StringVar()
    lapsosSeleccionada.set('Lapsos')
    menulapso = tk.OptionMenu(miFrame, lapsosSeleccionada, *lapso)
    menulapso.pack(side='left', padx=5, pady=5)