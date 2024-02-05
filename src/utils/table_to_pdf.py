from fpdf import FPDF

cabeceras = ['ID', 'Nombres', 'Apellidos', 'Cedula', 'Telefono', 'Fecha Nac.', 'Grado', 'Seccion', 'Inicio', 'Fin']
grado = ["Primer", "Segundo", "Tercero", "Cuarto", "Quinto"]


class PDF(FPDF):
    degree: int

    def header(self) -> None:
        self.image('src/assets/logo.jpeg', 10, 8, 33)
        self.set_font("Helvetica", "B", 25)
        
        self.cell(270, 30, f"Registro de los Estudiantes de {grado[self.degree - 1]} año", align="C")
        self.set_font("Helvetica", "B", 10)
        self.ln(40)
        for cabecera in cabeceras:
            if cabecera == 'Fecha Nac.':
                self.cell(40, 5, txt=cabecera, border=1, align='C')
            else:
                self.cell(26, 5, txt=cabecera, border=1, align='C')
        self.ln(5)
