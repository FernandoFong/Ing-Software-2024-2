from alchemyClasses.Alumno import Alumno
from alchemyClasses import db

def borra_alumno(num_cta):
    alumno = Alumno.query.filter(Alumno.num_cta).first()
    db.session.delete(alumno)
    db.session.commit()


