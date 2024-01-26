from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
from ..models import Evaluacion as Model

class Evaluacion:
    def __init__(self, engine: Engine) -> None:
        self.session = sessionmaker(engine)
    
    def create(self, unidad: int, contenido: str, metodo: str, fecha: datetime, id_profesor: int):
        with self.session() as session:
            if session.query(Model).filter_by(unidad=unidad, id_profesor=id_profesor).first() is not None:
                raise ValueError("Una evaluación con esta unidad y profesor ya existe.")
            evaluacion = Model(unidad=unidad,
                                    contenido=contenido,
                                    metodo=metodo,
                                    fecha=fecha,
                                    id_profesor=id_profesor)
            session.add(evaluacion)
            session.commit()

    def update(self, id: int, unidad: int, contenido: str, metodo: str, fecha: datetime, id_profesor: int):
        with self.session() as session:
            try:
                session.query(Model).filter_by(id=id).update({
                    Model.unidad: unidad,
                    Model.contenido: contenido,
                    Model.metodo: metodo,
                    Model.fecha: fecha,
                    Model.id_profesor: id_profesor
                })
                session.commit()
            except:
                raise ValueError("No se encuentra una evaluación con este id.")
            finally:
                session.close()
    
    def delete(self, id: int):
        with self.session() as session:
            try:
                evaluacion = session.query(Model).filter_by(id=id).first()
                session.delete(evaluacion)
                session.commit()
            except:
                raise ValueError("No se encuentra una evaluación con este id.")
            finally:
                session.close()
