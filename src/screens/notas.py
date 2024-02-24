import tkinter
from tkinter import Tk, ttk, messagebox
from ttkthemes import ThemedStyle
from sqlalchemy.orm import Session
import customtkinter
from ..services.nota import Nota
from ..models import Estudiante as Model, Materias as ModelMaterias, Nota as ModelNotas, Grado as ModelGrado
from ..engine import engine
from ..utils.table_to_pdf import PDFNotas
from ..utils.validate import is_number

def screen_notas(tk: tkinter, window: Tk, degree: int, rol: str):
    connect_nota = Nota(engine)

    def verificar_rol():
        if rol == "Profesor":
            botonGuardar = create_button(rame, 620, 280, "Guardar", guardar)
            botonBuscar = create_button(rame, 730, 280, "Buscar", buscar)
            botonDetalles = create_button(rame, "Detalles", mostrar_detalles)
        elif rol == "Secretaria":
            botonGuardar = create_button(rame, 620, 280, "Guardar", guardar)
            botonBuscar = create_button(rame, 730, 280, "Buscar", buscar)
            botonDetalles = create_button(rame, 840, 280, "Detalles", mostrar_detalles)
            botonDescargar = create_button(rame, 950, 280, "Descargar", generar_pdf)
        else:
            botonGuardar = create_button(rame, 620, 280, "Guardar", guardar)
            botonEliminar = create_button(rame, 730, 280, "Eliminar", eliminar)
            botonBuscar = create_button(rame, 840, 280, "Buscar", buscar)
            botonDetalles = create_button(rame, 950, 280, "Detalles", mostrar_detalles)
            botonDescargar = create_button(rame, 1060, 280, "Descargar", generar_pdf)
    
    def update_table():
        for i in table.get_children():
            table.delete(i)

    def create_table(frame, columns):
        
        table = ttk.Treeview(frame, columns=columns, show="headings")
        table.pack(fill="both", expand=True)

        for column in columns:
            table.column(column, width=150, anchor='center')
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

    #style = ThemedStyle (window)
    #style.set_theme("adapta")
    frame = tk.Frame(window, bg="white", width="1200", height="400")
    frame.pack(fill="both", expand=True)
    frame.place(x=0, y=350)
    columns = ('ID', 'ID Estudiante', 'Nombre Estudiante', 'Cedula', 'Materia', 'Evaluacion', 'Nota', 'Lapso')
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
        detalles_window.geometry("600x500")
        
        fondo = tk.PhotoImage(file='src/screens/disenos/fono2.png')
        image = tk.Label(detalles_window, image=fondo, width="600", height="500")
        image.place(x=0, y=0)
        image.image = fondo
        
        with Session(engine) as session:
            select_by_cedula = entryCedula.get()
            lapso = lapsosSeleccionada.get()
            estudiante = session.query(Model).filter_by(cedula=select_by_cedula).first()

            if estudiante is not None:
                materias = session.query(ModelMaterias).filter_by(id_grado=degree).all()

                # Crear y empaquetar una nueva etiqueta con el nombre y la cédula del estudiante
                estudiante_label = customtkinter.CTkLabel(master=detalles_window, text=f"Nombre del Estudiante: {estudiante.nombres}\n\nCédula: {estudiante.cedula}", 
                                                          width=120, height=25, fg_color="#fff", text_color="#000", corner_radius=8, font=customtkinter.CTkFont(size=18))
            
                estudiante_label.place(x=150,y=50)

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

                    nota_label = customtkinter.CTkLabel(master=detalles_window, text=f"Materia: {materia.nombre}\n\nValor: {str((sum(valores)) / 4)}", 
                                                          width=120, height=25, fg_color="#fff", text_color="#000", corner_radius=8, font=customtkinter.CTkFont(size=18))
                    #tk.Label(detalles_window, text="Materia: " + materia.nombre + "\nValor: " + str((sum(valores)) / 4), font=("Helvetica", 12))
                    nota_label.place(x=150, y=120)

                # Crear y empaquetar una nueva etiqueta con el lapso
                lapso_label = customtkinter.CTkLabel(master=detalles_window, text=f"Lapso: {str(lapso)}", 
                                                          width=120, height=25, fg_color="#fff", text_color="#000", corner_radius=8, font=customtkinter.CTkFont(size=18))
                #tk.Label(detalles_window, text="Lapso: " + str(lapso), font=("Helvetica", 12, "bold"))
                lapso_label.place(x=220, y=190)

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

    def create_button(rame, x, y, text, command):
        button = customtkinter.CTkButton(master=rame, width=100, height=40, text=text,
                                              text_color="#fff", fg_color="#0d487e", command=command, font=(0, 15),
                                              hover_color="#288a94")
        
        button.place(x=x, y=y)
        return button

    def create_option_menu(rame, options, initial_option, x, y):
        selected_option = tk.StringVar()
        selected_option.set(initial_option)
        menu = tk.OptionMenu(rame, selected_option, *options)
        menu.place(x=x, y=y)
        return selected_option
    
    def go_back():
        from .grados import screen_grado
        window.destroy()
        screen_grado(tk, window=tk.Toplevel(), degree=degree, rol=rol)

    def show_estudiantes_in_list():
        lista_estudiantes = []

        with Session(engine) as session:
            for estudiante in session.query(Model).all():
                if session.query(ModelGrado).filter_by(id_estudiante=estudiante.id).first():
                    lista_estudiantes.append(estudiante.cedula)
            return lista_estudiantes 
        
#///////////////////////////////////////////////////
    window.title("Control de Notas")
    window.geometry("1280x680")
    window.resizable(False, False)
    window.iconbitmap('src/screens/disenos/LUMASIS.ico')
    verdeclaro="#287678"
    vcomd = window.register(is_number)
    
    rame = tk.Frame(window, width=1280, height=350, bg="#287678")
    rame.place(x=0, y=0)
    
    piza = tk.PhotoImage(file='imagen.png')
    img = tk.Label(rame, image=piza, width="1200", height="250")
    img.place(x=0, y=96)
    img.image = piza
    
    icono= tk.PhotoImage(file='src/screens/disenos/urbaneja.png')
    
    cintillo = tk.Label(rame, text="Registro de Estudiantes", bd=5, bg=verdeclaro, fg="white", 
                        font=("Calisto Mt", 16))
    cintillo.config(image=icono)
    cintillo.image = icono 
    cintillo.place(x=485, y=10)
    
    nombre = tk.Label(rame, text="Notas de Estudiantes", bd=5, bg=verdeclaro, fg="white", 
                        font=("Calisto Mt", 16))
    
    nombre.place(x=565, y=28)
    
#///////////////////////////////////////////////////

    gobackboton = customtkinter.CTkButton(master=rame, width=95, height=37, text="Volver",
                                              text_color="#fff", fg_color="#0d487e", command=go_back, font=(0, 15),
                                              hover_color="#288a94")
    #tk.Button(rame, text="Volver", command=go_back, bg=verdeclaro)
    gobackboton.place(x=15,y=10)

    customtkinter.CTkLabel(master=rame, text="Cedula:", width=120, height=25,
                                               fg_color="#287678", text_color="#fff", corner_radius=8,
                                               font=customtkinter.CTkFont(size=18)).place(x=130, y=170)
    
    values = show_estudiantes_in_list()
    entryCedula = customtkinter.CTkComboBox(master=rame, width=150, height=30, border_width=0, corner_radius=10,
                                   font=(0, 16), values=values)
    entryCedula.place(x=280, y=170)

    customtkinter.CTkLabel(master=rame, text="Total de la nota:", width=120, height=25,
                                               fg_color="#287678", text_color="#fff", corner_radius=8,
                                               font=customtkinter.CTkFont(size=18)).place(x=130, y=220)
    entryNota = customtkinter.CTkEntry(master=rame, width=150, height=30, border_width=0, corner_radius=10,
                                       font=(0, 16), validate='key', validatecommand=(vcomd, '%P'))
    entryNota.place(x=280, y=220)


    materias = ["Arte y patrimonio", "Castellano", "Ciencias Naturales", "Educacion Fisica", "G.H.C", "Ingles", "Matematicas", "Orientación y convivencia", "G.E.R.P", "Fisica", "Quimica"]
    materiaSeleccionada = create_option_menu(rame, materias, 'Materias', 730, 170)

    notas = [1, 2, 3, 4]
    notasSeleccionada = create_option_menu(rame, notas, 'Notas', 850, 170)

    lapso = [1, 2, 3]
    lapsosSeleccionada = create_option_menu(rame, lapso, 'Lapsos', 960, 170)
    
    verificar_rol()