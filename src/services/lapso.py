from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
from ..models import Lapso as Model

class Lapso:
    def __init__(self, engine: Engine) -> None:
        self.session = sessionmaker(engine)
    
    def create(self, inicio: datetime, nota_id: int):
        with self.session() as session:
            lapso = Model(inicio=inicio,
                          nota_id=nota_id)
            session.add(lapso)
            session.commit()

    def update(self, id: int, inicio: datetime, fin: datetime, nota_id: int):
        with self.session() as session:
            try:
                session.query(Model).filter_by(id=id).update({
                    Model.inicio: inicio,
                    Model.fin: fin,
                    Model.nota_id: nota_id
                })
                session.commit()
            except:
                raise ValueError("No se encuentra un lapso con este id.")
            finally:
                session.close()
    
    def delete(self, id: int):
        with self.session() as session:
            try:
                lapso = session.query(Model).filter_by(id=id).first()
                session.delete(lapso)
                session.commit()
            except:
                raise ValueError("No se encuentra un lapso con este id.")
            finally:
                session.close()