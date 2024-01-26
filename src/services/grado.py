from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
from ..models import Grado as Model

class Grado:
    def __init__(self, engine: Engine) -> None:
        self.session = sessionmaker(engine)
    
    def create(self, inscrito: datetime, id_estudiante: int):
        with self.session() as session:
            if session.query(Model).filter_by(id_estudiante=id_estudiante, inscrito=inscrito).first() is not None:
                raise ValueError("Un grado con este estudiante e inscripción ya existe.")
            grado = Model(inscrito=inscrito,
                          id_estudiante=id_estudiante)
            session.add(grado)
            session.commit()

    def update(self, id: int, inscrito: datetime, id_estudiante: int):
        with self.session() as session:
            try:
                session.query(Model).filter_by(id=id).update({
                    Model.inscrito: inscrito,
                    Model.id_estudiante: id_estudiante
                })
                session.commit()
            except:
                raise ValueError("No se encuentra un grado con este id.")
            finally:
                session.close()
    
    def delete(self, id: int):
        with self.session() as session:
            try:
                grado = session.query(Model).filter_by(id=id).first()
                session.delete(grado)
                session.commit()
            except:
                raise ValueError("No se encuentra un grado con este id.")
            finally:
                session.close()
