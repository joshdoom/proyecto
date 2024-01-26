from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
from ..models import AnioEscolar as Model

class AnioEscolar:
    def __init__(self, engine: Engine) -> None:
        self.session = sessionmaker(engine)
    
    def create(self, inicio: datetime, fin: datetime, id_estudiante: int):
        with self.session() as session:
            if session.query(Model).filter_by(id_estudiante=id_estudiante, inicio=inicio).first() is not None:
                raise ValueError("Un año escolar con este estudiante e inicio ya existe.")
            anio_escolar = Model(inicio=inicio,
                                       fin=fin,
                                       id_estudiante=id_estudiante)
            session.add(anio_escolar)
            session.commit()

    def update(self, id: int, inicio: datetime, fin: datetime, id_estudiante: int):
        with self.session() as session:
            try:
                session.query(Model).filter_by(id=id).update({
                    Model.inicio: inicio,
                    Model.fin: fin,
                    Model.id_estudiante: id_estudiante
                })
                session.commit()
            except:
                raise ValueError("No se encuentra un año escolar con este id.")
            finally:
                session.close()
    
    def delete(self, id: int):
        with self.session() as session:
            try:
                anio_escolar = session.query(Model).filter_by(id=id).first()
                session.delete(anio_escolar)
                session.commit()
            except:
                raise ValueError("No se encuentra un año escolar con este id.")
            finally:
                session.close()
