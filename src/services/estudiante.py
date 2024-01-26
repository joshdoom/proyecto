from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
from ..models import Estudiante as Model

class Estudiante:
    def __init__(self, engine: Engine) -> None:
        self.session = sessionmaker(engine)
    
    def create(self, nombres: str, apellidos: str, cedula: str, telefono: str, fecha_nacimiento: datetime, id_representante: int):
        with self.session() as session:
            if session.query(Model).filter_by(cedula=cedula).first() is not None:
                raise ValueError("Un estudiante con esta cédula ya existe.")
            estudiante = Model(nombres=nombres,
                                    apellidos=apellidos,
                                    cedula=cedula,
                                    telefono=telefono,
                                    fecha_nacimiento=fecha_nacimiento,
                                    id_representante=id_representante)
            session.add(estudiante)
            session.commit()

    def update(self, id: int, nombres: str, apellidos: str, cedula: str, telefono: str, fecha_nacimiento: datetime, id_representante: int):
        with self.session() as session:
            try:
                session.query(Model).filter_by(id=id).update({
                    Model.nombres: nombres,
                    Model.apellidos: apellidos,
                    Model.cedula: cedula,
                    Model.telefono: telefono,
                    Model.fecha_nacimiento: fecha_nacimiento,
                    Model.id_representante: id_representante
                })
                session.commit()
            except:
                raise ValueError("No se encuentra un estudiante con este id.")
            finally:
                session.close()
    
    def delete(self, id: int):
        with self.session() as session:
            try:
                estudiante = session.query(Model).filter_by(id=id).first()
                session.delete(estudiante)
                session.commit()
            except:
                raise ValueError("No se encuentra un estudiante con este id.")
            finally:
                session.close()
