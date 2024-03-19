from sqlalchemy import Column, Integer, String

from alchemyClasses import db


class Usuario(db.Model):

    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key=True)
    nombre = Column(String(45))
    apPat = Column(String(45))
    apMat = Column(String(45), nullable=True)
    password = Column(String(64), nullable=True)
    email = Column(String(64), nullable=True)

    def __init__(self, nombre, apPat, apMat=None, password=None, email=None):
        self.nombre = nombre
        self.apPat = apPat
        self.apMat = apMat
        self.password = password
        self.email = email

    def __str__(self):
        return f'Nombre:{self.nombre}'