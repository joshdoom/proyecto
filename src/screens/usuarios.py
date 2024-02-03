from sqlalchemy.orm import sessionmaker 
from sqlalchemy.engine import Engine
from ..models import usuarios as Model
import tkinter
from tkinter import Tk
from ..models import usuarios
from ..engine import engine
from sqlalchemy.orm import session

def agregar_usuario(nombre, rol, contraseña, pregunta_seguridad, respuesta_seguridad):
    nuevo_usuario = usuarios(nombre=nombre, rol=rol, contraseña=contraseña, pregunta_seguridad=pregunta_seguridad, respuesta_seguridad=respuesta_seguridad)
    session.add(nuevo_usuario)
    session.commit()


user = usuarios.nombre
pwd = usuarios.contraseña
rol = usuarios.rol
pregunta= usuarios.pregunta_seguridad
respuesta= usuarios.respuesta_seguridad

def screen_login(tk: tkinter, window: Tk):
    def login(usuario, contraseña):
        from .index import screen_index

        if usuario in usuarios and usuarios[user][pwd] == pwd:
            window.destroy()
            screen_index(tk, window=Tk())
         #if username == "admin" and password == "123":
        else:
         raise ValueError ("usuario o contraseña incorrecto")    
        


       

def recuperar_contraseña(usuario):
    if usuario in usuarios:
        pregunta = usuarios[user]['pregunta_seguridad']
        respuesta_ingresada = input(f"{pregunta}: ")
        
        if respuesta_ingresada.lower() == usuarios[user][respuesta].lower():
            nueva_contraseña = input(f"Ingrese la nueva contraseña para {user}: ")
            usuarios[user][pwd] = nueva_contraseña
            print("Contraseña actualizada con éxito.")
        else:
            print("Respuesta incorrecta. No se puede cambiar la contraseña.")
    else:
        print("El usuario no existe. Intente nuevamente.")







    
