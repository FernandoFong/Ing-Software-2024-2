from alchemyClasses.Renta import Renta
from alchemyClasses import db


#/////////////////////////////////////////1)Ver los registros de una tabla
def muestra_todas_rentas():
    for renta in Renta.query.all():
        print(renta)
        print("--------------------------------")


#///////////////////////////////////////////2)Filtrar los registros por id
def filtrar_por_id_renta(id):
    for renta in Renta.query.filter(Renta.idRentar== id):
        print(renta)

#////////////////////////////////////////////3) Actualizar la columna nombre de un registro

def actualizar_fecha_renta(id,fecha):
    renta = Renta.query.filter(Renta.idRentar==id).first()
    renta.fecha_renta= fecha
    db.session.commit()
    print("Actualizacion realizada con exito")


#//////////////////////////////////////////4) Borrar registro por id o todos los registros
def borra_renta(id):
    renta = Renta.query.filter(Renta.idRentar == id).first()
    if renta:
        db.session.delete(renta)
        db.session.commit()
        print(f"Renta con el ID {id} ha sido eliminado.")
    else:
        print(f"No se encontró ningúna renta con el ID {id}.")


def borra_todas_rentas():
    rentas = Renta.query.all()
    for renta in rentas:
        db.session.delete(renta)
    db.session.commit()
    print("Todos los registros de rentas han sido eliminadas.")





