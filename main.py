import tkinter as tk
from src.screens.login import screen_login

if __name__ == '__main__':
    window = tk.Tk()
    screen_login(tk, window=window)

    window.mainloop()