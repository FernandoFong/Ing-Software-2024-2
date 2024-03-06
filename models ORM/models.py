from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    idUsuario = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    apPat = Column(String(200), nullable=False)
    apMat = Column(String(200))
    password = Column(String(64), nullable=False)
    email = Column(String(500), unique=True)
    profilePicture = Column(String)
    superUser = Column(Integer)

class Pelicula(Base):
    __tablename__ = 'peliculas'

    idPelicula = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    genero = Column(String(45))
    duracion = Column(Integer)
    inventario = Column(Integer, nullable=False, default=1)

class Rentar(Base):
    __tablename__ = 'rentar'

    idRentar = Column(Integer, primary_key=True)
    idUsuario = Column(Integer, ForeignKey('usuarios.idUsuario'))
    idPelicula = Column(Integer, ForeignKey('peliculas.idPelicula'))
    fecha_renta = Column(DateTime, nullable=False, default=datetime.now)
    dias_de_renta = Column(Integer, default=5)
    estatus = Column(Integer, default=0)

    usuario = relationship("Usuario", back_populates="rentas")
    pelicula = relationship("Pelicula", back_populates="rentas")

Usuario.rentas = relationship("Rentar", order_by=Rentar.idRentar, back_populates="usuario")
Pelicula.rentas = relationship("Rentar", order_by=Rentar.idRentar, back_populates="pelicula")