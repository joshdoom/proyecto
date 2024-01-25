from colorama import Fore
from sqlalchemy.orm import session
from engine import engine 
from models import Estudiante, Representante, Seccion, AnioEscolar, Nota, Grado, Materias, Profesor, Lapso, Evaluacion

def create_profesor(id: int):
        with session(engine) as session:
                for Profesor in session.query(Profesor):
                    if not Profesor.id == id:
                        new_profesor= Profesor(id=id)
                        session.add(new_profesor)
                        session.commit()


                            
                           
                    else:
                          raise ValueError("El profesor ya existe")

def create_evaluacion(id: int):
        with session(engine) as session:
                for Profesor in session.query(Evaluacion):
                    if not Evaluacion.id == id:
                        new_evaluacion= Evaluacion(id=id)
                        session.add(new_evaluacion)
                        session.commit()


                            
                           
                    else:
                          raise ValueError("La evaluacion esta registrada")

def create_nota(id: int):
        with session(engine) as session:
                for Profesor in session.query(Nota):
                    if not Nota.id == id:
                        new_nota= Nota(id=id)
                        session.add(new_nota)
                        session.commit()


                            
                           
                    else:
                          raise ValueError("La nota es igual")

def create_lapso(id: int):
        with session(engine) as session:
                for Profesor in session.query(Lapso):
                    if not Lapso.id == id:
                        new_lapso= Lapso(id=id)
                        session.add(new_lapso)
                        session.commit()


                            
                           
                    else:
                          raise ValueError("Lapso ya esta registrado")
                    
def create_evaluacion(id: int):
        with session(engine) as session:
                for Profesor in session.query(Evaluacion):
                    if not Evaluacion.id == id:
                        new_evaluacion= Evaluacion(id=id)
                        session.add(new_evaluacion)
                        session.commit()


                            
                           
                    else:
                          raise ValueError("La evaluacion esta registrada")
                    

def update_profesor():