from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
from ..models import Representante as Model

class Representante:
    def __init__(self, engine: Engine) -> None:
        self.session = sessionmaker(engine)
    
    def create(self, nombres: str, apellidos: str, cedula: str, telefono: str, profesion: str = None):
        with self.session() as session:
            if session.query(Model).filter_by(cedula=cedula).first() is not None:
                raise ValueError("Un representante con esta cédula ya existe.")
            representante = Model(nombres=nombres,
                                apellidos=apellidos,
                                cedula=cedula,
                                telefono=telefono,
                                profesion=profesion)
            session.add(representante)
            session.commit()

    def update(self, id: int, nombres: str, apellidos: str, cedula: str, telefono: str, profesion: str = None):
        with self.session() as session:
            try:
                session.query(Model).filter_by(id=id).update({
                    Model.nombres: nombres,
                    Model.apellidos: apellidos,
                    Model.cedula: cedula,
                    Model.telefono: telefono,
                    Model.profesion: profesion
                })
                session.commit()
            except:
                raise ValueError("No se encuentra un representante con este id.")
            finally:
                session.close()
    
    def delete(self, id: int):
        with self.session() as session:
            try:
                representante = session.query(Model).filter_by(id=id).first()
                session.delete(representante)
                session.commit()
            except:
                raise ValueError("No se encuentra un representante con este id.")
            finally:
                session.close()