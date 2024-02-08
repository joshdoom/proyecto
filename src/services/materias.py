from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
from ..models import Materias as Model

class Materias:
    def __init__(self, engine: Engine) -> None:
        self.session = sessionmaker(engine)
    
    def create(self, codigo: str, nombre: str, descripcion: str, id_grado: int):
        with self.session() as session:
            if session.query(Model).filter_by(nombre=nombre, id_grado=id_grado).first() is not None:
                raise ValueError("Una materia con este código y grado ya existe.")
            materia = Model(codigo=codigo,
                               nombre=nombre,
                               descripcion=descripcion,
                               id_grado=id_grado)
            session.add(materia)
            session.commit()

    def update(self, id: int, codigo: str, nombre: str, descripcion: str, id_grado: int):
        with self.session() as session:
            try:
                session.query(Model).filter_by(id=id).update({
                    Model.codigo: codigo,
                    Model.nombre: nombre,
                    Model.descripcion: descripcion,
                    Model.id_grado: id_grado
                })
                session.commit()
            except:
                raise ValueError("No se encuentra una materia con este id.")
            finally:
                session.close()
    
    def delete(self, id: int):
        with self.session() as session:
            try:
                materia = session.query(Model).filter_by(id=id).first()
                session.delete(materia)
                session.commit()
            except:
                raise ValueError("No se encuentra una materia con este id.")
            finally:
                session.close()
