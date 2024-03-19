from alchemyClasses import db
from sqlalchemy import Column, Integer, String
from datetime import date

class Pelicula(db.Model):

    __tablename__ = 'peliculas'
    idPelicula = Column(Integer, primary_key=True)
    nombre = Column(String(45))
    genero = Column(String(45), nullable=True)
    duracion = Column(Integer, nullable=True)
    inventario = Column(Integer, nullable=True)

    def __init__(self, nombre, genero=None, duracion=None, inventario=None):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.inventario = inventario

    def __str__(self):
        #Que regrese el nombre de la pelicula y su inventario
        return f"Pelicula: {self.nombre} Inventario: {self.inventario}"