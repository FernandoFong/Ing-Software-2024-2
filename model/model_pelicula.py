from alchemyClasses.Pelicula import Pelicula
from alchemyClasses import db


#/////////////////////////////////////////1)Ver los registros de una tabla
def muestra_todas_peliculas():
    for pelicula in Pelicula.query.all():
        print(pelicula)
        print("--------------------------------")


#///////////////////////////////////////////2)Filtrar los registros por id
def filtrar_por_id_pelicula(id):
    for pelicula in Pelicula.query.filter(Pelicula.idPelicula== id):
        print(pelicula)

#////////////////////////////////////////////3) Actualizar la columna nombre de un registro

def actualizar_nombre_pelicula(id,nombre):
    pelicula = Pelicula.query.filter(Pelicula.idPelicula==id).first()
    pelicula.nombre= nombre
    db.session.commit()
    print("Actualizacion realizada con exito")


#//////////////////////////////////////////4) Borrar registro por id o todos los registros
def borra_pelicula(id):
    pelicula = Pelicula.query.filter(Pelicula.idPelicula == id).first()
    if pelicula:
        db.session.delete(pelicula)
        db.session.commit()
        print(f"Pelicula con el ID {id} ha sido eliminado.")
    else:
        print(f"No se encontró ningúna pelicula con el ID {id}.")


def borra_todas_peliculas():
    peliculas = Pelicula.query.all()
    for pelicula in peliculas:
        db.session.delete(pelicula)
    db.session.commit()
    print("Todos los registros de peliculas han sido eliminadas.")





