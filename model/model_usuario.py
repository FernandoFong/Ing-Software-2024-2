from alchemyClasses.Usuario import Usuario
from alchemyClasses import db


#/////////////////////////////////////////1)Ver los registros de una tabla
def muestra_todos_usuarios():
    for usuario in Usuario.query.all():
        print(usuario)
        print("--------------------------------")


#///////////////////////////////////////////2)Filtrar los registros por id
def filtrar_por_id_usuario(id):
    for usuario in Usuario.query.filter(Usuario.idUsuario== id):
        print(usuario)



#////////////////////////////////////////////3) Actualizar la columna nombre de un registro

def actualizar_nombre_usuario(id,nombre):
    usuario = Usuario.query.filter(Usuario.idUsuario==id).first()
    usuario.nombre= nombre
    db.session.commit()
    print("Actualizacion realizada con exito")


#//////////////////////////////////////////4) Borrar registro por id o todos los registros
def borra_usuario(id):
    usuario = Usuario.query.filter(Usuario.idUsuario == id).first()
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        print(f"Usuario con el ID {id} ha sido eliminado.")
    else:
        print(f"No se encontró ningún usuario con el ID {id}.")


def borra_todos_usuarios():
    usuarios = Usuario.query.all()
    for usuario in usuarios:
        db.session.delete(usuario)
    db.session.commit()
    print("Todos los registros de usuarios han sido eliminados.")





