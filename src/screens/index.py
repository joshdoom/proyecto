import tkinter
from tkinter import Tk

def screen_index(tk: tkinter, window: Tk):
    def create_button(text, command):
        button = tk.Button(loginFrame, text=text, command=command)
        button.pack(pady=10)
    
    from .professor import screen_professor
    from .grados.grado_i import screen_grado_i
    from .grados.grado_ii import screen_grado_ii
    from .grados.grado_iii import screen_grado_iii
    from .grados.grado_iv import screen_grado_iv
    from .grados.grado_v import screen_grado_v

    def primero():
        screen_grado_i(tk, window=Tk())

    def segundo():
        screen_grado_ii(tk, window=Tk())

    def tercero():
        screen_grado_iii(tk, window=Tk())

    def cuarto():
        screen_grado_iv(tk, window=Tk())

    def quinto():
        screen_grado_v(tk, window=Tk())

    def profesores():
        screen_professor(tk, window=Tk())

    window.title("Ventana Principal")
    window.geometry("400x600")
    window.resizable(0,0)

    loginFrame = tk.Frame(window)
    loginFrame.pack()

    titulo = tk.Label(loginFrame, text="Selecciona a donde quieras ir", font=("Helvetica", 16))
    titulo.pack(pady=20)

    create_button("Primer año", command=primero)
    create_button("Segundo año", command=segundo)
    create_button("Tercer año", command=tercero)
    create_button("Cuarto año", command=cuarto)
    create_button("Quinto año", command=quinto)
    create_button("Profesores", command=profesores)