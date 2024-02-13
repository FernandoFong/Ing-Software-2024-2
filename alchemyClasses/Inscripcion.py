from alchemyClasses import db
from flask import Column, Integer, ForeignKey, DateTime
from datetime import date

class Inscripcion(db.Model):

    __tablename__ = 'inscripcion'
    id_inscripcion = Column(Integer, primary_key=True)
    id_alumno = Column(Integer, ForeignKey('alumno.id_alumno'))
    id_clase = Column(Integer, ForeignKey('clase.id_clase'))
    fecha = Column(DateTime, nullable=True)

    def __init__(self, id_alumno, id_clase, fecha=date.today()):
        self.id_alumno = id_alumno
        self.id_clase = id_clase
        self.fecha = fecha

    def __str__(self):
        #Que regrese el nombre del alumno y que regrese el nombre de la clase.
        return f"Alumno: {}\nClase: {}\nFecha: {self.fecha}"