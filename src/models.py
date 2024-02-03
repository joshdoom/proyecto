from sqlalchemy import Column
from sqlalchemy import Integer, String, Numeric, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase 

class Base(DeclarativeBase):
    pass

class usuarios(Base):
    __tablename__= 'usuarios'
    id=Column(Integer, primary_key=True)
    nombre=Column(String(60), nullable=True)
    rol= Column (String(60), nullable=False)
    contrasena = Column(String(60), nullable=True)
    pregunta_seguridad= Column(String(100), nullable=True)
    respuesta_seguridad= Column(String(100), nullable=True)

class Representante(Base):
    __tablename__ = 'representantes'

    id = Column(Integer, primary_key=True)
    nombres = Column(String(60), nullable=False)
    apellidos = Column(String(60), nullable=True)
    cedula = Column(String(12), nullable=False)
    telefono = Column(String(60), nullable=False)
    profesion = Column(String, nullable=True)

class Estudiante(Base):
    __tablename__ = 'estudiantes'

    id = Column(Integer, primary_key=True)
    nombres = Column(String(60), nullable=False)
    apellidos = Column(String(60), nullable=True)
    cedula = Column(String(60), nullable=False)
    telefono = Column(String(60), nullable=True)
    fecha_nacimiento = Column(DateTime, nullable=False)
    id_representante = Column(Integer)
    
class AnioEscolar(Base):
    __tablename__ = 'anio_escolar'

    id = Column(Integer, primary_key=True)
    inicio = Column(DateTime, nullable=False)
    fin = Column(DateTime, nullable=True)
    id_estudiante = Column(Integer, ForeignKey('estudiantes.id'))

class Grado(Base):
    __tablename__ = 'grados'

    id = Column(Integer, primary_key=True)
    inscrito = Column(String, nullable=False)
    id_estudiante = Column(Integer, ForeignKey('estudiantes.id'))

class Seccion(Base):
    __tablename__ = 'secciones'

    id = Column(Integer, primary_key=True)
    seccion = Column(String, default="U")
    id_grado = Column(Integer, ForeignKey('grados.id'))

class Materias(Base):
    __tablename__ = 'materias'

    id = Column(Integer, primary_key=True)
    codigo = Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    id_grado = Column(Integer)

class Profesor(Base):
    __tablename__ = 'profesores'

    id = Column(Integer, primary_key=True)
    nombres = Column(String(60), nullable=False)
    apellidos = Column(String(60), nullable=True)
    cedula = Column(String(12), nullable=False)
    telefono = Column(String(60), nullable=False)
    titulo = Column(String, nullable=False)
    id_materia = Column(Integer)

class Evaluacion(Base):
    __tablename__ = 'evaluaciones'

    id = Column(Integer, primary_key=True)
    unidad = Column(Integer)
    contenido = Column(String, nullable=True)
    metodo = Column(String, nullable=True)
    fecha = Column(DateTime, nullable=True)
    id_profesor = Column(Integer, nullable=True)

class Nota(Base):
    __tablename__ = 'notas'

    id = Column(Integer, primary_key=True)
    nota1 = Column(Integer, nullable=True, default=0)
    nota2 = Column(Integer, nullable=True, default=0)
    nota3 = Column(Integer, nullable=True, default=0)
    nota4 = Column(Integer, nullable=True, default=0)
    valor_neto = Column(Numeric, nullable=True)
    unidad = Column(Integer)
    id_lapso = Column(Integer)
    id_estudiante = Column(Integer, ForeignKey('estudiantes.id'))
    id_materia = Column(Integer, ForeignKey('materias.id'))

class Lapso(Base):
    __tablename__ = 'lapsos'

    id = Column (Integer, primary_key=True)
    inicio = Column (Integer, nullable=False)
    nota_id = Column(Integer, ForeignKey('notas.id'))