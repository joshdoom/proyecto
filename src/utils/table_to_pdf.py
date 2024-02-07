from fpdf import FPDF

cabeceras_grados = ['ID', 'Nombres', 'Apellidos', 'Cedula', 'Telefono', 'Fecha Nac.', 'Grado', 'Seccion', 'Inicio', 'Fin']
cabeceras_notas = ['Asignaturas', 'Evaluacion 1', 'Evaluacion 2', 'Evaluacion 3', 'Evaluacion 4', 'TOTAL']
grado = ["Primer", "Segundo", "Tercero", "Cuarto", "Quinto"]


class PDFGrado(FPDF):
    degree: int

    def header(self) -> None:
        self.image('src/assets/logo.jpeg', 10, 8, 33)
        self.set_font("Helvetica", "B", 25)
        
        self.cell(270, 30, f"Registro de los Estudiantes de {grado[self.degree - 1]} año", align="C")
        self.set_font("Helvetica", "B", 10)
        self.ln(40)
        for cabecera in cabeceras_grados:
            if cabecera == 'Fecha Nac.':
                self.cell(40, 5, txt=cabecera, border=1, align='C')
            else:
                self.cell(26, 5, txt=cabecera, border=1, align='C')
        self.ln(5)

class PDFNotas(FPDF):
    degree: int
    estudiante: str
    cedula: str

    def header(self) -> None:
        self.image('src/assets/logo.jpeg', 10, 8, 33)
        self.set_font("Helvetica", "B", 25)
        
        self.cell(270, 30, f"Notas del Estudiante de {grado[self.degree - 1]} año", align="C")
        self.set_font("Helvetica", "B", 10)
        self.ln(20)
        self.cell(150, 30, txt=f'Alumno(a): {self.estudiante} Cedula: {self.cedula}', align='C')
        self.ln(20)
        self.cell(20)
        for cabecera in cabeceras_notas:
           self.cell(40, 5, txt=cabecera, border=1, align='C')
        self.ln(5)

