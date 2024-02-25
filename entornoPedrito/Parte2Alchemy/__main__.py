from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate
from models.ModelosORM import Usuarios, Peliculas, Rentar

# Crear el engine de SQLAlchemy para conectarse a la base de datos
engine = create_engine('mysql+pymysql://lab:Developer123!@localhost/lab_ing_software')

# Crear una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

# Imprimir las tablas
def ver_registros(tabla):
    registros = session.query(tabla).all()
    headers = [column.key for column in tabla.__table__.columns if column.key != '_sa_instance_state']
    rows = [[getattr(registro, column) for column in headers] for registro in registros]
    print(tabulate(rows, headers=headers, tablefmt='grid'))


class InvalidRequestError:
    pass

# Filtrar las tablas
def filtrar_por_id_Usuario(tabla, id):
    try:
        resultado = session.query(tabla).filter_by(idUsuario=id).all()
        return resultado
    except InvalidRequestError as e:
        print(f"Error: {e}")
        return None

def filtrar_por_id_Pelicula(tabla, id):
    try:
        resultado = session.query(tabla).filter_by(idPelicula=id).all()
        return resultado
    except InvalidRequestError as e:
        print(f"Error: {e}")
        return None

def filtrar_por_id_Renta(tabla, id):
    try:
        resultado = session.query(tabla).filter_by(idRentar=id).all()
        return resultado
    except InvalidRequestError as e:
        print(f"Error: {e}")
        return None

# Actualizar nombre en los registros
def actualizar_nombre_registro_usuario(tabla, id, nuevo_nombre):
    registro = session.query(tabla).filter_by(idUsuario=id).first()
    if registro:
        registro.nombre = nuevo_nombre
        session.commit()
        print("Nombre actualizado correctamente.")
    else:
        print("No se encontró ningún registro con ese ID.")

def actualizar_nombre_registro_pelicula(tabla, id, nuevo_nombre):
    registro = session.query(tabla).filter_by(idPelicula=id).first()
    if registro:
        registro.nombre = nuevo_nombre
        session.commit()
        print("Nombre actualizado correctamente.")
    else:
        print("No se encontró ningún registro con ese ID.")

def actualizar_nombre_registro_renta(tabla, id, nueva_fecha):
    registro = session.query(tabla).filter_by(idRentar=id).first()
    if registro:
        try:
            nueva_fecha = datetime.strptime(nueva_fecha, "%Y-%m-%d").date()
            registro.fecha_renta = nueva_fecha
            session.commit()
            print("Fecha de renta actualizada correctamente.")
        except ValueError:
            print("Formato de fecha incorrecto. Debe ser YYYY-MM-DD.")
    else:
        print("No se encontró ningún registro con ese ID.")

# Eliminando por id señores
def eliminar_registro_por_idUsuario(tabla, id):
    registro = session.query(tabla).filter_by(idUsuario=id).first()
    if registro:
        session.delete(registro)
        session.commit()
        print("Registro eliminado correctamente.")
    else:
        print("No se encontró ningún registro con ese ID.")

def eliminar_registro_por_idPelicula(tabla, id):
    registro = session.query(tabla).filter_by(idPelicula=id).first()
    if registro:
        session.delete(registro)
        session.commit()
        print("Registro eliminado correctamente.")
    else:
        print("No se encontró ningún registro con ese ID.")

def eliminar_registro_por_idRentar(tabla, id):
    registro = session.query(tabla).filter_by(idRentar=id).first()
    if registro:
        session.delete(registro)
        session.commit()
        print("Registro eliminado correctamente.")
    else:
        print("No se encontró ningún registro con ese ID.")

# Madres que hay que hacer esto :0
def eliminar_todos_los_registros(tabla):
    print("No lo hagas gonzalo, no gonzalo, te estan viendo tus hijos :c \n")
    confirmacion = input("¿Estás seguro que deseas eliminar todos los registros de esta tabla? (s/n): ")
    if confirmacion.lower() == 's':
        session.query(tabla).delete()
        session.commit()
        print("Todos los registros han sido eliminados correctamente.")
    else:
        print("No lo hagas gonzalo, no gonzalo, te estan viendo tus hijos :c")

def mostrar_menu():
    print("Menú:")
    print("1. Ver los registros de una tabla.")
    print("2. Filtrar los registros de una tabla por ID.")
    print("3. Actualizar la columna nombre de un registro.")
    print("4. Eliminar un registro por ID.")
    print("5. Eliminar todos los registros de una tabla.")
    print("0. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción que desea ejecutar: ")

        if opcion == '1':
            tabla = input("Ingrese el nombre de la tabla que desea ver (usuarios, peliculas, rentar): ").lower()
            if tabla == 'usuarios':
                ver_registros(Usuarios)
            elif tabla == 'peliculas':
                ver_registros(Peliculas)
            elif tabla == 'rentar':
                ver_registros(Rentar)
            else:
                print("Tabla no válida.")

        elif opcion == '2':
            tabla = input("Ingrese el nombre de la tabla que desea filtrar (usuarios, peliculas, rentar): ").lower()

            if tabla == 'usuarios':
                id = input("Ingrese el ID por el que desea filtrar: ")
                registros = filtrar_por_id_Usuario(Usuarios, id)
            elif tabla == 'peliculas':
                id = input("Ingrese el ID por el que desea filtrar: ")
                registros = filtrar_por_id_Pelicula(Peliculas, id)
            elif tabla == 'rentar':
                id = input("Ingrese el ID por el que desea filtrar: ")
                registros = filtrar_por_id_Renta(Rentar, id)
            else:
                print("Tabla no válida.")
                continue

            if registros:
                print("Registros encontrados:")
                headers = [column.key for column in registros[0].__table__.columns if
                           column.key != '_sa_instance_state']
                rows = [[getattr(registro, column) for column in headers] for registro in registros]
                print(tabulate(rows, headers=headers, tablefmt='pretty'))
            else:
                print("No se encontraron registros.")
                continue

        elif opcion == '3':
            tabla = input("Ingrese el nombre de la tabla en la que desea actualizar el nombre (usuarios, peliculas, rentar): ").lower()

            if tabla == 'usuarios':
                id = input("Ingrese el ID del registro que desea actualizar: ")
                nuevo_nombre = input("Ingrese el nuevo nombre de usuario(Recuerde poner el apellido, si no lo pone sirve pero pues se ve feo :3 ): ")
                actualizar_nombre_registro_usuario(Usuarios, id, nuevo_nombre)
            elif tabla == 'peliculas':
                id = input("Ingrese el ID del registro que desea actualizar: ")
                nuevo_nombre = input("Ingrese el nuevo nombre de la pelicula: ")
                actualizar_nombre_registro_pelicula(Peliculas, id, nuevo_nombre)
            elif tabla == 'rentar':
                id = input("Ingrese el ID del registro que desea actualizar: ")
                nueva_fecha = input("Ingrese la nueva fecha (YYYY-MM-DD): ")
                actualizar_nombre_registro_renta(Rentar, id, nueva_fecha)
            else:
                print("Tabla no válida.")

        elif opcion == '4':
            tabla = input("Ingrese el nombre de la tabla en la que desea eliminar un registro (usuarios, peliculas, rentar): ").lower()

            if tabla == 'usuarios':
                id = input("Ingrese el ID del registro que desea eliminar: ")
                eliminar_registro_por_idUsuario(Usuarios, id)
            elif tabla == 'peliculas':
                id = input("Ingrese el ID del registro que desea eliminar: ")
                eliminar_registro_por_idPelicula(Peliculas, id)
            elif tabla == 'rentar':
                id = input("Ingrese el ID del registro que desea eliminar: ")
                eliminar_registro_por_idRentar(Rentar, id)
            else:
                print("Tabla no válida.")

        elif opcion == '5':
            tabla = input("Ingrese el nombre de la tabla de la que desea eliminar todos los registros (usuarios, peliculas, rentar): ").lower()
            if tabla == 'usuarios':
                eliminar_todos_los_registros(Usuarios)
            elif tabla == 'peliculas':
                eliminar_todos_los_registros(Peliculas)
            elif tabla == 'rentar':
                eliminar_todos_los_registros(Rentar)
            else:
                print("Tabla no válida.")

        elif opcion == '0':
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, ingrese un número del 0 al 5.")

if __name__ == "__main__":
    main()
