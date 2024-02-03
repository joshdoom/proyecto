from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
from ..models import Nota as Model

class Nota:
    def __init__(self, engine: Engine) -> None:
        self.session = sessionmaker(engine)
    
    def create(self, nota: float, id_unidad: int, id_lapso: int, id_estudiante: int, id_materia: int):
        with self.session() as session:
            nota_obj = session.query(Model).filter_by(id_estudiante=id_estudiante, id_materia=id_materia, unidad=id_unidad, id_lapso=id_lapso).first()
            if not nota_obj:
                nota_obj = Model(nota1=nota, id_estudiante=id_estudiante, id_materia=id_materia, unidad=id_unidad, id_lapso=id_lapso)
                session.add(nota_obj)
            else:
                if nota_obj.nota1 == 0:
                    nota_obj.nota1 = nota
                elif nota_obj.nota2 == 0:
                    nota_obj.nota2 = nota
                elif nota_obj.nota3 == 0:
                    nota_obj.nota3 = nota
                elif nota_obj.nota4 == 0:
                    nota_obj.nota4 = nota
                else:
                    nota_obj.valor_neto = (nota_obj.nota1 + nota_obj.nota2 + nota_obj.nota3 + nota_obj.nota4) / 4
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
