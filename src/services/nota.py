from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
from ..models import Nota as Model

class Nota:
    def __init__(self, engine: Engine) -> None:
        self.session = sessionmaker(engine)
    
    def create(self, valor: float, porcentaje: float, total: float, id_estudiante: int, id_materia: int):
        with self.session() as session:
            nota = Model(valor=valor,
                         porcentaje=porcentaje,
                         total=total,
                         id_estudiante=id_estudiante,
                         id_materia=id_materia)
            session.add(nota)
            session.commit()

    def update(self, id: int, valor: float, porcentaje: float, total: float, id_estudiante: int, id_materia: int):
        with self.session() as session:
            try:
                session.query(Model).filter_by(id=id).update({
                    Model.valor: valor,
                    Model.porcentaje: porcentaje,
                    Model.total: total,
                    Model.id_estudiante: id_estudiante,
                    Model.id_materia: id_materia
                })
                session.commit()
            except:
                raise ValueError("No se encuentra una nota con este id.")
            finally:
                session.close()
    
    def delete(self, id: int):
        with self.session() as session:
            try:
                nota = session.query(Model).filter_by(id=id).first()
                session.delete(nota)
                session.commit()
            except:
                raise ValueError("No se encuentra una nota con este id.")
            finally:
                session.close()
