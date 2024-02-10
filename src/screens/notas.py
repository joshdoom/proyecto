import tkinter
from tkinter import Tk, ttk, messagebox
from sqlalchemy.orm import Session

from ..services.nota import Nota
from ..models import Estudiante as Model, Materias as ModelMaterias, Nota as ModelNotas
from ..engine import engine
from ..utils.table_to_pdf import PDFNotas

def screen_notas(tk: tkinter, window: Tk, degree: int):
    connect_nota = Nota(engine)

    def update_table():
        for i in table.get_children():
            table.delete(i)

    def create_table(frame, columns):
        table = ttk.Treeview(frame, columns=columns)
        table.pack(fill="both", expand=True)

        for column in columns:
            table.column(column, width=100, anchor='center')
            table.heading(column, text=column)
        
        return table

    def show_notas(table, estudiante, materias, lapso):
        with Session(engine) as session:
            for materia in materias:
                notas = session.query(ModelNotas).filter_by(id_estudiante=estudiante.id, id_materia=materia.id).all()
                for nota in notas:
                    if str(nota.id_lapso) == str(lapso):
                        lista = [nota.nota1, nota.nota2, nota.nota3, nota.nota4]
                        table.insert('', 'end', values=(nota.id, estudiante.id, estudiante.nombres, estudiante.cedula, materia.nombre, nota.unidad, lista[int(nota.unidad) - 1], lapso))
        table.pack(fill="both", expand=True)

    frame = tk.Frame(window, bg="white", width="1400", height="350", bd=10)
    frame.pack(fill="both", expand=True)
    columns = ('ID', 'ID Estudiante', 'Nombre del estudiante', 'Cedula', 'Materia', 'Evaluacion', 'Nota', 'Lapso')
    table = create_table(frame, columns)

    def buscar():
        with Session(engine) as session:
            select_by_cedula = entryCedula.get()
            lapso = lapsosSeleccionada.get()
            estudiante = session.query(Model).filter_by(cedula=select_by_cedula).first()

            if estudiante is not None:
                materias = session.query(ModelMaterias).filter_by(id_grado=degree).all()
                update_table()  # Llama a update_table para borrar el contenido existente
                show_notas(table, estudiante, materias, lapso)
    
    def guardar():
        try:
            with Session(engine) as session:
                cedula = entryCedula.get() 
                nota = entryNota.get()
                materia = materiaSeleccionada.get()
                evaluacion = notasSeleccionada.get()
                lapso = lapsosSeleccionada.get()

                if not all([cedula, nota, materia, evaluacion, lapso]):
                    messagebox.showerror("Error", "Todos los campos deben estar rellenos")
                    return
                
                estudiante = session.query(Model).filter_by(cedula=cedula).first()
                materia = session.query(ModelMaterias).filter_by(nombre=materia).first()
                connect_nota.create(nota, evaluacion, lapso, estudiante.id, materia.id)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminar():
        selected_item = table.selection()[0]
        selected_nota = table.item(selected_item)['values'][0]
        connect_nota.delete(selected_nota)
        update_table()

    def mostrar_detalles():
        # Crear una nueva ventana
        detalles_window = tk.Toplevel(window)
        detalles_window.title("Detalles de las Notas")
        detalles_window.geometry("600x400")

        with Session(engine) as session:
            select_by_cedula = entryCedula.get()
            lapso = lapsosSeleccionada.get()
            estudiante = session.query(Model).filter_by(cedula=select_by_cedula).first()

            if estudiante is not None:
                materias = session.query(ModelMaterias).filter_by(id_grado=degree).all()

                # Crear y empaquetar una nueva etiqueta con el nombre y la cédula del estudiante
                estudiante_label = tk.Label(detalles_window, text="Nombre del estudiante: " + estudiante.nombres + "\nCédula: " + estudiante.cedula, font=("Helvetica", 12, "bold"))
                estudiante_label.pack()

                for materia in materias:
                    notas = session.query(ModelNotas).filter_by(id_estudiante=estudiante.id, id_materia=materia.id, id_lapso=lapso).all()
                    valores = []
                    for nota_obj in notas:
                        if nota_obj.unidad == 1:
                            valores.append(nota_obj.nota1)
                        elif nota_obj.unidad == 2:
                            valores.append(nota_obj.nota2)
                        elif nota_obj.unidad == 3:
                            valores.append(nota_obj.nota3)
                        elif nota_obj.unidad == 4:
                            valores.append(nota_obj.nota4)

                    nota_label = tk.Label(detalles_window, text="Materia: " + materia.nombre + "\nValor: " + str((sum(valores)) / 4), font=("Helvetica", 12))
                    nota_label.pack()

                # Crear y empaquetar una nueva etiqueta con el lapso
                lapso_label = tk.Label(detalles_window, text="Lapso: " + str(lapso), font=("Helvetica", 12, "bold"))
                lapso_label.pack()

    def generar_pdf():
        pdf = PDFNotas('L', 'mm', 'A4')
        pdf.degree = degree

        with Session(engine) as session:
            select_by_cedula = entryCedula.get()
            lapso = lapsosSeleccionada.get()
            estudiante = session.query(Model).filter_by(cedula=select_by_cedula).first()
            pdf.cedula = estudiante.cedula
            pdf.estudiante = f"{estudiante.nombres} {estudiante.apellidos}"

            if estudiante is not None:
                pdf.cedula = estudiante.cedula
                pdf.estudiante = f"{estudiante.nombres} {estudiante.apellidos}"
                pdf.add_page()
                pdf.set_font("Helvetica","", 10)

                materias = session.query(ModelMaterias).filter_by(id_grado=degree).all()
                for materia in materias:
                    pdf.cell(20)
                    notas = session.query(ModelNotas).filter_by(id_estudiante=estudiante.id, id_materia=materia.id, id_lapso=lapso).all()
                    valores = []
                    for nota_obj in notas:
                        if nota_obj.unidad == 1:
                            valores.append(nota_obj.nota1)
                        elif nota_obj.unidad == 2:
                            valores.append(nota_obj.nota2)
                        elif nota_obj.unidad == 3:
                            valores.append(nota_obj.nota3)
                        elif nota_obj.unidad == 4:
                            valores.append(nota_obj.nota4)

                    if not len(valores) == 4:
                        for x in range(4 - len(valores)):
                            valores.append(0)

                    valor_neto = (sum(valores)) / 4
                    datos = [materia.nombre, *valores, valor_neto]
                    for dato in datos:
                        pdf.cell(40, 5, txt=str(dato), border=1, align='C')
                    pdf.ln(5)

        pdf.output(f"src/pdfs/nota_de_grado{degree}_de_{estudiante.cedula}.pdf")

    window.title("Control de Notas")
    window.geometry("1280x680")
    window.config(bd=20)
    window.resizable(False, False)
    window.iconbitmap('src/screens/disenos/LUMASIS.ico')
    verdeclaro="#b8f2ca"
    window.config(bg=verdeclaro)

    def create_label_and_entry(miFrame, text, side='left', padx=5, pady=5):
        label = tk.Label(miFrame, text=text)
        label.pack(side=side, padx=padx, pady=pady)
        entry = tk.Entry(miFrame)
        entry.pack(side=side, padx=padx, pady=pady)
        return entry

    def create_button(miFrame, text, command, side='left', padx=5, pady=5):
        button = tk.Button(miFrame, text=text, bg="white", fg="black", command=command)
        button.pack(side=side, padx=padx, pady=pady)
        return button

    def create_option_menu(miFrame, options, initial_option, side='left', padx=5, pady=5):
        selected_option = tk.StringVar()
        selected_option.set(initial_option)
        menu = tk.OptionMenu(miFrame, selected_option, *options)
        menu.pack(side=side, padx=padx, pady=pady)
        return selected_option

    miFrame = tk.Frame(window, width=1200, height=250, bd=5, relief="groove")
    miFrame.pack()

    botonGuardar = create_button(miFrame, "Guardar", guardar)
    botonEliminar = create_button(miFrame, "Eliminar", eliminar)
    botonBuscar = create_button(miFrame, "Buscar", buscar)
    botonDetalles = create_button(miFrame, "Detalles", mostrar_detalles)
    botonDescargar = create_button(miFrame, "Descargar", generar_pdf)

    entryNota = create_label_and_entry(miFrame, "Total de la nota:")
    entryCedula = create_label_and_entry(miFrame, "Cedula:")

    materias = ["Arte y patrimonio", "Castellano", "Ciencias Naturales", "Educacion Fisica", "G.H.C", "Ingles", "Matematicas", "Orientación y convivencia", "G.E.R.P", "Fisica", "Quimica"]
    materiaSeleccionada = create_option_menu(miFrame, materias, 'Materias')

    notas = [1, 2, 3, 4]
    notasSeleccionada = create_option_menu(miFrame, notas, 'Notas')

    lapso = [1, 2, 3]
    lapsosSeleccionada = create_option_menu(miFrame, lapso, 'Lapsos')