from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
from ..models import Profesor as Model

class Profesor:
    def __init__(self, engine: Engine) -> None:
        self.session = sessionmaker(engine)
    
    def create(self, nombres: str, apellidos: str, cedula: str, telefono: str, titulo: str, id_materia: int):
        with self.session() as session:
            if session.query(Model).filter_by(cedula=cedula).first() is not None:
                raise ValueError("Un profesor con esta cédula ya existe.")
            profesor = Model(nombres=nombres,
                                apellidos=apellidos,
                                cedula=cedula,
                                telefono=telefono,
                                titulo=titulo,
                                id_materia=id_materia)
            session.add(profesor)
            session.commit()

    def update(self, id: int, nombres: str, apellidos: str, cedula: str, telefono: str, titulo: str, id_materia: int):
        with self.session() as session:
            try:
                session.query(Model).filter_by(id=id).update({
                    Model.nombres: nombres,
                    Model.apellidos: apellidos,
                    Model.cedula: cedula,
                    Model.telefono: telefono,
                    Model.titulo: titulo,
                    Model.id_materia: id_materia
                })
                session.commit()
            except:
                raise ValueError("No se encuentra un profesor con este id.")
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
