# from .representante import Representante
# from .estudiante import Estudiante
# from .anioescolar import AnioEscolar
# from .grado import Grado
# from .seccion import Seccion
# from .materias import Materias
# from .profesor import Profesor
# from .evaluacion import Evaluacion
# from .nota import Nota
# from .lapso import Lapso

# from ..engine import engine

# services_classes = {
#     'representantes': Representante,
#     'estudiantes': Estudiante,
#     'anio_escolar': AnioEscolar,
#     'grados': Grado,
#     'secciones': Seccion,
#     'materias': Materias,
#     'profesores': Profesor,
#     'evaluaciones': Evaluacion,
#     'notas': Nota,
#     'lapsos': Lapso
# }

# def Gestor(table: str):
#     session = services_classes.get(table)
#     if session is not None:
#         return session(engine)
#     else:
#         raise ValueError("Engine not found")