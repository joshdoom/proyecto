import sqlalchemy
from sqlalchemy import column
from sqlalchemy import DateTime
from sqlalchemy import Integer, String, Numeric, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import proyecto_db

Base= proyecto_db

class profesor:

    __tablename__= "Profesores"

    id= column (Integer, Primary_key=True)
    nombre1= column(String(30), nullable=False )
    nombre2= column(String(30), nullable=False)
    apellido= column(String(30), nullable=False)
    apellido2= column(String(20), nullable= True)
    telefono= column(Integer, nullable= True)
    create_at= column(DateTime, default=DateTime.now())
    update_at= column(DateTime, default=DateTime.now())

class evaluacion:

    __tablename__= "Evaluaciones"

    Unidad=column(Integer, primary_key= True)
    contenido= column (String(60), nullable=False )
    metodo= column (String(60), nullable=False )
    fecha=column (DateTime, nullable=True)
    id_profesor= column(Integer, ForeignKey("Profesores.id"))
    create_at= column(DateTime, default=DateTime.now())
    update_at= column(DateTime, default=DateTime.now())

class Nota:

    __tablename__= "Notas"

    id_estudiante=column (Integer, primary_key=True)
    Valor =column (Numeric, nullable= False)
    porcentaje=column(Integer, nullable= True)
    promedio=column(Numeric, )
    unidad_evaluacion= column (Integer, ForeignKey("Evaluaciones.unidad") )
    create_at= column(DateTime, default=DateTime.now())
    update_at= column(DateTime, default=DateTime.now())
    
class Lapso:

    __tablename__= "lapso"

    id= column (Integer, primary_key=True)
    inicio=column (DateTime, nullable=False)
    fin=column (DateTime, nullable=False)
    nota_id_estudiante= column (Integer, ForeignKey("Notas.id_estudiante"))
    create_at= column(DateTime, default=DateTime.now())
    update_at= column(DateTime, default=DateTime.now())

    