from sqlalchemy import Column, Integer, String
from alchemyClasses import db

class Pelicula(db.Model):

    __tablename__='peliculas'
    idPelicula = Column(Integer, primary_key=True)
    nombre = Column(String(200),nullable=False)
    genero= Column(String(45))
    duracion = Column(Integer)
    inventario= Column(Integer,nullable=False,default=1)

    def __init__(self, nombre, genero, duracion, inventario):
        self.nombre=nombre
        self.genero=genero
        self.duracion=duracion
        self.inventario=inventario

    def __str__(self):
        return f'ID:{self.idPelicula}\nNombre:{self.nombre}\nGenero:{self.genero}\nDuracion:{self.duracion}\nInventario:{self.inventario}'
