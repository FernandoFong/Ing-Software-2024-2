import pymysql
from datetime import datetime, timedelta

connection = pymysql.connect(
    host='localhost',
    user='lab',
    password='Developer123!',
    database='lab_ing_software'
)

# Función para insertar un usuario
def insertar_usuario():
    nombre = input("Ingrese el nombre del usuario(Nombre Apellido en ese orden): ")
    password = input("Ingrese la contraseña del usuario: ")
    email = input("Ingrese el email del usuario: ")
    super_user = int(input("¿Es super usuario? (0: No, 1: Sí): "))

    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (nombre, password, email, superUser) VALUES (%s, %s, %s, %s)", (nombre, password, email, super_user))
        connection.commit()
        print("Usuario insertado correctamente.")
    except pymysql.Error as e:
        print("Error al insertar usuario:", e)
    finally:
        cursor.close()

# Función para insertar una película
def insertar_pelicula():
    nombre = input("Ingrese el nombre de la película: ")
    genero = input("Ingrese el género de la película: ")
    duracion = int(input("Ingrese la duración de la película en minutos: "))
    inventario = int(input("Ingrese la cantidad en inventario: "))

    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES (%s, %s, %s, %s)", (nombre, genero, duracion, inventario))
        connection.commit()
        print("Película insertada correctamente.")
    except pymysql.Error as e:
        print("Error al insertar película:", e)
    finally:
        cursor.close()

# Función para insertar un registro de renta
def insertar_renta():
    id_usuario = int(input("Ingrese el ID del usuario: "))
    id_pelicula = int(input("Ingrese el ID de la película: "))
    fecha_renta_str = input("Ingrese la fecha de renta (formato YYYY-MM-DD): ")
    fecha_renta = datetime.strptime(fecha_renta_str, "%Y-%m-%d").date()
    dias_de_renta = int(input("Ingrese la cantidad de días de renta: "))
    estatus = int(input("Ingrese el estatus de la renta (0: Pendiente, 1: Finalizada): "))

    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO rentar (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus) VALUES (%s, %s, %s, %s, %s)", (id_usuario, id_pelicula, fecha_renta, dias_de_renta, estatus))
        connection.commit()
        print("Registro de renta insertado correctamente.")
    except pymysql.Error as e:
        print("Error al insertar registro de renta:", e)
    finally:
        cursor.close()

# Función para filtrar usuarios por apellido
def filtrar_usuarios_por_apellido(apellido):
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM usuarios WHERE nombre LIKE %s", ('%' + apellido,))
        usuarios = cursor.fetchall()
        if usuarios:
            print("Usuarios encontrados cuyo apellido termina en '{}'".format(apellido))
            for usuario in usuarios:
                print(usuario)
        else:
            print("No se encontraron usuarios cuyo apellido termine en '{}'".format(apellido))
    except pymysql.Error as e:
        print("Error al filtrar usuarios por apellido:", e)
    finally:
        cursor.close()

# Función para cambiar el género de una película por su nombre
def cambiar_genero_pelicula_por_nombre(nombre_pelicula, nuevo_genero):
    cursor = connection.cursor()
    try:
        # Verificar si la película existe
        cursor.execute("SELECT * FROM peliculas WHERE nombre = %s", (nombre_pelicula,))
        pelicula = cursor.fetchone()
        if pelicula:
            # Si la película existe, actualizar su género
            cursor.execute("UPDATE peliculas SET genero = %s WHERE nombre = %s", (nuevo_genero, nombre_pelicula))
            connection.commit()
            print("Se ha cambiado el género de la película '{}' a '{}'.".format(nombre_pelicula, nuevo_genero))
        else:
            print("No se encontró ninguna película con el nombre '{}'.".format(nombre_pelicula))
    except pymysql.Error as e:
        print("Error al cambiar el género de la película:", e)
    finally:
        cursor.close()

# Función para eliminar rentas anteriores a 3 días de la fecha actual
def eliminar_rentas_antiguas():
    cursor = connection.cursor()
    try:
        fecha_actual = datetime.now().date()
        fecha_limite = fecha_actual - timedelta(days=3)
        cursor.execute("DELETE FROM rentar WHERE fecha_renta <= %s", (fecha_limite,))
        connection.commit()
        num_filas_afectadas = cursor.rowcount
        print("Se eliminaron {} rentas antiguas anteriores al {}.".format(num_filas_afectadas, fecha_limite))
    except pymysql.Error as e:
        print("Error al eliminar rentas antiguas:", e)
    finally:
        cursor.close()


#insertar_usuario()
#insertar_pelicula()
#insertar_renta()
#filtrar_usuarios_por_apellido("Morales")
#cambiar_genero_pelicula_por_nombre("Universo","Galaxias")
#eliminar_rentas_antiguas()