from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
from ..models import Usuario as Model

class Usuario:
    def __init__(self, engine: Engine) -> None:
        self.session = sessionmaker(engine)
    
    def create(self, nombre_de_usuario: str, password: str, rol: str, question: str, answer: str):
        with self.session() as session:
            if session.query(Model).filter_by(nombre=nombre_de_usuario).first():
                raise Exception('Se encuentra un usuario con ese username.')
            
            user = Model(nombre=nombre_de_usuario,
                             rol=rol,
                             contrasena=password,
                             pregunta_seguridad=question,
                             respuesta_seguridad=answer)
            session.add(user)
            session.commit()

    def update(self, id: int, password: str):
        with self.session() as session:
            try:
                session.query(Model).filter_by(id=id).update({
                    Model.contrasena: password,
                })
                session.commit()
            except:
                raise ValueError("No se encuentra un usuario con este id.")
            finally:
                session.close()
    
    def delete(self, id: int):
        with self.session() as session:
            try:
                profesor = session.query(Model).filter_by(id=id).first()
                session.delete(profesor)
                session.commit()
            except:
                raise ValueError("No se encuentra un profesor con este id.")
            finally:
                session.close()
