from alchemyClasses import db
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import date

class Renta(db.Model):

    __tablename__ = 'rentar'
    idRentar = Column(Integer, primary_key=True)
    idUsuario = Column(Integer, ForeignKey(column='usuarios.idUsuario', ondelete='CASCADE'))
    idPelicula = Column(Integer, ForeignKey(column='peliculas.idPelicula', ondelete='CASCADE'))
    fecha_renta = Column(DateTime, default=date.today())
    dias_de_renta = Column(Integer, default=5)
    estatus = Column(Integer, default=0)    

    def __init__(self, idUsuario, idPelicula, fecha_renta=date.today(), dias_de_renta=5, estatus=0):
        self.idUsuario = idUsuario
        self.idPelicula = idPelicula
        self.fecha_renta = fecha_renta
        self.dias_de_renta = dias_de_renta
        self.estatus = estatus


    def __str__(self):
        return f"Renta: {self.idRentar} Usuario: {self.idUsuario} Pelicula: {self.idPelicula} Fecha: {self.fecha_renta} Dias: {self.dias_de_renta} Estatus: {self.estatus}"