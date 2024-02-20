from sqlalchemy import Column, Integer, String

from alchemyClasses import db


class Usuario(db.Model):

    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key=True)
    nombre = Column(String(200),nullable=False)
    apPat = Column(String(200),nullable=False)
    apMat = Column(String(200), nullable=True)
    password = Column(String(64),nullable=False)
    email = Column(String(500))
    profilePicture = Column(String(50))
    superUser = Column(Integer)

    def __init__(self, nombre, apPat, apMat, password, email, profilePicture, superUser):
        self.nombre = nombre
        self.ap_pat = apPat
        self.ap_mat = apMat
        self.password = password
        self.email = email
        self.profilePicture= profilePicture
        self.superUser= superUser

    def __str__(self):
        return f'ID:{self.idUsuario}\nNombre:{self.nombre} {self.apPat}\nEmail:{self.email}\nPassword:{self.password}'