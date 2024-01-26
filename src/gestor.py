from colorama import Fore
from sqlalchemy.orm import session
from engine import engine 
from models import Estudiante, Representante, Seccion, AnioEscolar, Nota, Grado, Materias, Profesor, Lapso, Evaluacion

def create_representante(id: int):
        with session(engine) as session:
                for Representante in session.query(Representante):
                    if not Representante.id == id:
                        new_Representante= Representante(id=id)
                        session.add(new_Representante)
                        session.commit()


                            
                           
                    else:
                          raise ValueError("El Representante ya existe") 
                    
def update_representante(id: int):
        with session(engine) as session:
                try:
                     session.query(Representante).\
                        filter(Representante.id == id)
                        
                     session.commit()
                except:
                    raise ValueError ("El Representante no existe")                    

def create_estudiante(id: int):
        with session(engine) as session:
                for Estudiante in session.query(Estudiante):
                    if not Estudiante.id == id:
                        new_Estudiante= Estudiante(id=id)
                        session.add(new_Estudiante)
                        session.commit()


                            
                           
                    else:
                          raise ValueError("El Estudiante ya existe")
                    
def update_estudiante(id: int):
        with session(engine) as session:
                try:
                     session.query(Estudiante).\
                        filter(Estudiante.id == id).\
                        update({
                              Estudiante.id_representante: Representante, 
                              Estudiante.id_representante: AnioEscolar                       
                              
                        })

                     session.commit()
                except:
                    raise ValueError ("El Estudiante no existe")                          

def create_anioEscolar(id: int):
        with session(engine) as session:
                for AnioEscolar in session.query(AnioEscolar):
                    if not AnioEscolar.id == id:
                        new_AnioEscolar= AnioEscolar(id=id)
                        session.add(new_AnioEscolar)
                        session.commit()


                            
                           
                    else:
                          raise ValueError("El AnioEscolar ya existe") 

def update_anioEscolar(id: int):
        with session(engine) as session:
                try:
                     session.query(AnioEscolar).\
                        filter(AnioEscolar.id == id).\
                        update({
                              AnioEscolar.id_estudiante: Estudiante, 
                              AnioEscolar.id_estudiante: Grado                       
                              
                        })

                     session.commit()
                except:
                    raise ValueError ("El Año Escolar no existe")                     

def create_grado(id: int):
        with session(engine) as session:
                for Grado in session.query(Grado):
                    if not Grado.id == id:
                        new_Grado= Grado(id=id)
                        session.add(new_Grado)
                        session.commit()


                            
                           
                    else:
                          raise ValueError("El Grado ya existe") 
                    
def update_grador(id: int):
        with session(engine) as session:
                try:
                     session.query(Grado).\
                        filter(Grado.id == id).\
                        update({
                              Grado.id_estudiante: AnioEscolar, 
                              Grado.id_estudiante: Materias                       
                              
                        })

                     session.commit()
                except:
                    raise ValueError ("El Grado no existe")

def create_seccion(id: int):
        with session(engine) as session:
                for Seccion in session.query(Seccion):
                    if not Seccion.id == id:
                        new_Seccion= Seccion(id=id)
                        session.add(new_Seccion)
                        session.commit()


                            
                           
                    else:
                          raise ValueError("La Seccion ya existe")
                    
def update_seccion(id: int):
        with session(engine) as session:
                try:
                     session.query(Seccion).\
                        filter(Seccion.id == id).\
                        update({
                              Seccion.id_grado: Grado 
                                                                                   
                        })

                     session.commit()
                except:
                    raise ValueError ("La Seccion no existe")

def create_materias(id: int):
        with session(engine) as session:
                for Materias in session.query(Materias):
                    if not Materias.id == id:
                        new_Materias= Materias(id=id)
                        session.add(new_Materias)
                        session.commit()


                            
                           
                    else:
                          raise ValueError("La Materias ya existe")    
                          
def update_materias(id: int):
        with session(engine) as session:
                try:
                     session.query(Materias).\
                        filter(Materias.id == id).\
                        update({
                              Materias.id_grado: Grado,
                              Materias.id_grado: Profesor 
                                                                                   
                        })

                     session.commit()
                except:
                    raise ValueError ("Las Materia no existe")

def create_profesor(id: int):
        with session(engine) as session:
                for Profesor in session.query(Profesor):
                    if not Profesor.id == id:
                        new_profesor= Profesor(id=id)
                        session.add(new_profesor)
                        session.commit()


                            
                           
                    else:
                          raise ValueError("El profesor ya existe")
                    
def update_profesor(id: int):
        with session(engine) as session:
                try:
                     session.query(Profesor).\
                        filter(Profesor.id == id).\
                        update({
                              Profesor.id_materia: Materias, 
                              Profesor.id_materia: Evaluacion                       
                              
                        })

                     session.commit()
                except:
                    raise ValueError ("El profesor no existe") 
                           

def create_evaluacion(id: int):
        with session(engine) as session:
                for Evaluacion in session.query(Evaluacion):
                    if not Evaluacion.id == id:
                        new_evaluacion= Evaluacion(id=id)
                        session.add(new_evaluacion)
                        session.commit()


                            
                           
                    else:
                          raise ValueError("La evaluacion esta registrada")

def update_evaluacion(id: int):
        with session(engine) as session:
                try:
                     session.query(Evaluacion).\
                        filter(Evaluacion.id == id).\
                        update({
                              Evaluacion.id_profesor: Nota,     
                              Evaluacion.id_profesor: Profesor                        
                        })

                     session.commit()
                except:
                    raise ValueError ("La evaluacion no existe")                    

def create_nota(id: int):
        with session(engine) as session:
                for Nota in session.query(Nota):
                    if not Nota.id == id:
                        new_nota= Nota(id=id)
                        session.add(new_nota)
                        session.commit()


                            
                           
                    else:
                          raise ValueError("La nota es igual")

def update_nota(id: int):
        with session(engine) as session:
                try:
                     session.query(Nota).\
                        filter(Nota.id == id).\
                        update({
                              Nota.id_estudiante: Lapso,
                              Nota.id_materia: Materias
                        })

                     session.commit()
                except:
                    raise ValueError ("La nota no existe")

def create_lapso(id: int):
        with session(engine) as session:
                for Lapso in session.query(Lapso):
                    if not Lapso.id == id:
                        new_lapso= Lapso(id=id)
                        session.add(new_lapso)
                        session.commit()


                            
                           
                    else:
                          raise ValueError("Lapso ya esta registrado")
                    
def update_lapso(id: int):
        with session(engine) as session:
                try:
                     session.query(Lapso).\
                        filter(Lapso.id == id).\
                        update({
                              Lapso.nota_id:Nota 
                              
                        })

                     session.commit()
                except:
                    raise ValueError ("El lapso no existe")