from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Usuario, Pelicula, Rentar
from datetime import datetime
import os

# Crear carpeta __pycache__
os.makedirs('__pycache__', exist_ok=True)

# Crear conexión a la base de datos
engine = create_engine('mysql+pymysql://ferfong:Developer123!@localhost/lab_ing_software')
Session = sessionmaker(bind=engine)
session = Session()

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

# Funciones del menú
def ver_registros(tabla):
    registros = session.query(tabla).all()
    print("\n" + "-"*60)
    print(f"{'Registros de la tabla':^60}")
    print("-"*60)
    for registro in registros:
        print("\n" + "-"*60)
        for column in registro.__table__.columns:
            print(f"{column.name}: {getattr(registro, column.name)}")
    print("\n" + "-"*60)

def filtrar_por_id(tabla, id):
    if tabla == Usuario:
        registro = session.query(tabla).filter_by(idUsuario=id).first()
    elif tabla == Pelicula:
        registro = session.query(tabla).filter_by(idPelicula=id).first()
    else:
        registro = None
    
    if registro:
        print("\n" + "-"*60)
        print(f"{'Registro filtrado por ID':^60}")
        print("-"*60)
        for column in registro.__table__.columns:
            print(f"{column.name}: {getattr(registro, column.name)}")
        print("\n" + "-"*60)
    else:
        print("\nNo se encontraron registros con ese ID.")

def actualizar_nombre(tabla, id, nuevo_nombre):
    if tabla == Usuario:
        registro = session.query(tabla).filter_by(idUsuario=id).first()
    elif tabla == Rentar:
        registro = session.query(tabla).filter_by(idRentar=id).first()
    else:
        registro = None

    if registro:
        registro.nombre = nuevo_nombre
        session.commit()
        print("\nNombre actualizado exitosamente.")
    else:
        print("\nNo se encontraron registros con ese ID.")

def actualizar_fecha_renta(id, nueva_fecha):
    registro = session.query(Rentar).filter_by(idRentar=id).first()
    if registro:
        registro.fecha_renta = nueva_fecha
        session.commit()
        print("\nFecha de renta actualizada exitosamente.")
    else:
        print("\nNo se encontraron registros de renta con ese ID.")

def eliminar_registro(tabla, id=None):
    if id:
        if tabla == Usuario:
            registro = session.query(tabla).filter_by(idUsuario=id).first()
        elif tabla == Pelicula:
            registro = session.query(tabla).filter_by(idPelicula=id).first()
        elif tabla == Rentar:
            registro = session.query(tabla).filter_by(idRentar=id).first()
        else:
            registro = None
        
        if registro:
            session.delete(registro)
            session.commit()
            print("\nRegistro eliminado exitosamente.")
        else:
            print("\nNo se encontró ningún registro con ese ID.")
    else:
        confirmacion = input("\n¿Está seguro que desea eliminar todos los registros de esta tabla? (S/N): ")
        if confirmacion.lower() == 's':
            session.query(tabla).delete()
            session.commit()
            print("\nTodos los registros fueron eliminados exitosamente.")
        else:
            print("\nOperación cancelada.")

# Menú principal
while True:
    print("\n" + "-"*60)
    print(f"{'Menú':^60}")
    print("-"*60)
    print("1. Ver registros de una tabla.")
    print("2. Filtrar registros por ID.")
    print("3. Actualizar fecha de renta.")
    print("4. Eliminar registro.")
    print("5. Salir.")

    opcion = input("\nSeleccione una opción: ")

    if opcion == '1':
        tabla = input("\nIngrese el nombre de la tabla (usuarios, peliculas, rentar): ")
        if tabla == 'usuarios':
            ver_registros(Usuario)
        elif tabla == 'peliculas':
            ver_registros(Pelicula)
        elif tabla == 'rentar':
            ver_registros(Rentar)
        else:
            print("\nTabla no válida.")
    
    elif opcion == '2':
        tabla = input("\nIngrese el nombre de la tabla (usuarios, peliculas, rentar): ")
        id = input("\nIngrese el ID a filtrar: ")
        if tabla == 'usuarios':
            filtrar_por_id(Usuario, id)
        elif tabla == 'peliculas':
            filtrar_por_id(Pelicula, id)
        elif tabla == 'rentar':
            filtrar_por_id(Rentar, id)
        else:
            print("\nTabla no válida.")

    elif opcion == '3':
        tabla = input("\nIngrese el nombre de la tabla (usuarios, rentar): ")
        id = input("\nIngrese el ID del registro a actualizar: ")
        if tabla == 'rentar':
            nueva_fecha = input("\nIngrese la nueva fecha de renta (formato YYYY-MM-DD HH:MM:SS): ")
            nueva_fecha = datetime.strptime(nueva_fecha, "%Y-%m-%d %H:%M:%S")
            actualizar_fecha_renta(id, nueva_fecha)
        else:
            print("\nTabla no válida.")

    elif opcion == '4':
        tabla = input("\nIngrese el nombre de la tabla (usuarios, peliculas, rentar): ")
        id = input("\nIngrese el ID del registro a eliminar (dejar en blanco para eliminar todos los registros): ")
        if id:
            id = int(id)
        if tabla == 'usuarios':
            eliminar_registro(Usuario, id)
        elif tabla == 'peliculas':
            eliminar_registro(Pelicula, id)
        elif tabla == 'rentar':
            eliminar_registro(Rentar, id)
        else:
            print("\nTabla no válida.")
    
    elif opcion == '5':
        print("\nSaliendo del programa...")
        break

    else:
        print("\nOpción no válida. Intente de nuevo.")