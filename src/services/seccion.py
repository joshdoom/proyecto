from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
from ..models import Seccion as Model

class Seccion:
    def __init__(self, engine: Engine) -> None:
        self.session = sessionmaker(engine)
    
    def create(self, seccion: str, id_grado: int):
        with self.session() as session:
            if session.query(Model).filter_by(seccion=seccion, id_grado=id_grado).first() is not None:
                raise ValueError("Una sección con este nombre y grado ya existe.")
            seccion = Model(seccion=seccion,
                              id_grado=id_grado)
            session.add(seccion)
            session.commit()

    def update(self, id: int, seccion: str, id_grado: int):
        with self.session() as session:
            try:
                session.query(Model).filter_by(id=id).update({
                    Model.seccion: seccion,
                    Model.id_grado: id_grado
                })
                session.commit()
            except:
                raise ValueError("No se encuentra una sección con este id.")
            finally:
                session.close()
    
    def delete(self, id: int):
        with self.session() as session:
            try:
                seccion = session.query(Model).filter_by(id=id).first()
                session.delete(seccion)
                session.commit()
            except:
                raise ValueError("No se encuentra una sección con este id.")
            finally:
                session.close()
