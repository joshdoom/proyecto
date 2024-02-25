import tkinter 
from tkinter import Tk
from PIL import ImageTk
from pdf2image import convert_from_path
from ttkthemes import ThemedTk

def screen_vista_previa(tk: tkinter, window: Tk, ruta_pdf: str):
    window.title("Vista Previa")

    paginas = convert_from_path(ruta_pdf, poppler_path=r"src\utils\poppler-24.02.0\Library\bin")
    
    window.configure(background='#209c62')

    imagen_reducida = paginas[0].resize((600, 400))

    window.imagen = ImageTk.PhotoImage(imagen_reducida)
    etiqueta_imagen = tk.Label(window, image=window.imagen, borderwidth=2, relief="solid")
    etiqueta_imagen.grid(row=0, column=0, padx=10, pady=10)
    titulo = tk.Label(window, text="Esta es una vista previa del PDF.", font=('Helvetica', 14), fg="black", bg='#209c62')
    titulo.grid(row=1, column=0, padx=10, pady=10)

    boton_confirma = tk.Button(window, text="Confirmar", font=('Helvetica', 14), bg='white', bd=0, fg="black", command=lambda: window.destroy())
    boton_confirma.grid(row=2, column=0, padx=10, pady=10)
