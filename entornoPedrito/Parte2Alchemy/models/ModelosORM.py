from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'usuarios'

    idUsuario = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    password = Column(String(64), nullable=False)
    email = Column(String(500))
    profilePicture = Column(String)
    superUser = Column(Integer)

class Peliculas(Base):
    __tablename__ = 'peliculas'

    idPelicula = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    genero = Column(String(45))
    duracion = Column(Integer)
    inventario = Column(Integer, default=1)

class Rentar(Base):
    __tablename__ = 'rentar'

    idRentar = Column(Integer, primary_key=True)
    idUsuario = Column(Integer, ForeignKey('usuarios.idUsuario'))
    idPelicula = Column(Integer, ForeignKey('peliculas.idPelicula'))
    fecha_renta = Column(DateTime)
    dias_de_renta = Column(Integer, default=5)
    estatus = Column(Integer, default=0)