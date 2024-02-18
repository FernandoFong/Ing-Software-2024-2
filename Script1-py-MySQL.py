import pymysql.cursors
import random
import string

# connect to the database
connection = pymysql.connect(
    host="localhost",
    user="lab",
    password="Developer123!",
    db="lab_ing_software",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)


def create(tabla: str, data: dict):
    try:
        with connection.cursor() as cursor:
            if tabla == "usuarios":
                sql = "INSERT INTO usuarios (nombre, apPat, apMat, password, email, profilePicture, superUser) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            elif tabla == "peliculas":
                sql = "INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES (%s, %s, %s, %s)"
            elif tabla == "rentar":
                sql = "INSERT INTO rentar (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, tuple(data.values()))
        connection.commit()
    except Exception as e:
        print("Error:", e)


def read(tabla: str, id: str):
    try:

        if id_existe_en_tabla(id, tabla):
            if tabla == "usuarios":

                with connection.cursor() as cursor:
                    sql = "SELECT idUsuario, nombre FROM usuarios WHERE idUsuario = %s"
                    cursor.execute(sql, (id,))
                    result = cursor.fetchone()  # para mostrar solo un resultado
            elif tabla == "peliculas":
                with connection.cursor() as cursor:
                    sql = "SELECT idPelicula, nombre, genero FROM peliculas WHERE idPelicula = %s"
                    cursor.execute(sql, (id,))
                    result = cursor.fetchone()

            elif tabla == "rentar":
                with connection.cursor() as cursor:
                    sql = "SELECT idRentar, idUsuario, idPelicula,fecha_renta, dias_de_renta, estatus FROM rentar WHERE idRentar = %s"
                    cursor.execute(sql, (id,))
                    result = cursor.fetchone()

            if result is None:
                return "No se encontraron resultados"
            return result
        else:
            print("El ID proporcionado no existe en la tabla: ", tabla)

    except Exception as e:
        print("Error:", e)


def update(tabla: str, id: str, data: dict):
    if id_existe_en_tabla(id, tabla):
        try:
            if tabla == "usuarios":
                with connection.cursor() as cursor:
                    sql = "UPDATE usuarios SET nombre = %s, apPat = %s, apMat = %s, password = %s, email = %s, profilePicture = %s, superUser = %s WHERE idUsuario = %s"
                    cursor.execute(
                        sql,
                        (
                            data["nombre"],
                            data["apPat"],
                            data["apMat"],
                            data["password"],
                            data["email"],
                            data["profilePicture"],
                            data["superUser"],
                            id,
                        ),
                    )
                connection.commit()
            elif tabla == "peliculas":
                with connection.cursor() as cursor:
                    sql = "UPDATE peliculas SET nombre = %s, genero = %s, duracion = %s, inventario = %s WHERE idPelicula = %s"
                    cursor.execute(
                        sql,
                        (
                            data["nombre"],
                            data["genero"],
                            data["duracion"],
                            data["inventario"],
                            id,
                        ),
                    )
                connection.commit()
            elif tabla == "rentar":
                with connection.cursor() as cursor:
                    sql = "UPDATE rentar SET idUsuario = %s, idPelicula = %s, fecha_renta = %s, dias_de_renta = %s, estatus = %s WHERE idRentar = %s"
                    cursor.execute(
                        sql,
                        (
                            data["idUsuario"],
                            data["idPelicula"],
                            data["fecha_renta"],
                            data["dias_de_renta"],
                            data["estatus"],
                            id,
                        ),
                    )
                connection.commit()
        except Exception as e:
            print("Error:", e)
    else:
        print("El ID proporcionado no existe en la tabla: ", tabla)


def delete(tabla: str, id: str):
    if id_existe_en_tabla(id, tabla):
        try:
            with connection.cursor() as cursor:
                if tabla == "usuarios":
                    sql = "DELETE FROM usuarios WHERE idUsuario = %s"
                elif tabla == "peliculas":
                    sql = "DELETE FROM peliculas WHERE idPelicula = %s"
                elif tabla == "rentar":
                    sql = "DELETE FROM rentar WHERE idRentar = %s"
                cursor.execute(sql, (id,))
            connection.commit()
        except Exception as e:
            print("Error:", e)
    else:
        print("El ID proporcionado no existe en la tabla: ", tabla)


# funcion para verificar si un id existe en una tabla
def id_existe_en_tabla(id: str, tabla: str) -> bool:
    try:
        with connection.cursor() as cursor:
            if tabla == "usuarios":
                sql = "SELECT EXISTS(SELECT 1 FROM usuarios WHERE idUsuario = %s)"
            elif tabla == "peliculas":
                sql = "SELECT EXISTS(SELECT 1 FROM peliculas WHERE idPelicula = %s)"
            elif tabla == "rentar":
                sql = "SELECT EXISTS(SELECT 1 FROM rentar WHERE idRentar = %s)"
            cursor.execute(sql, (id,))
            result = cursor.fetchone()
            return result[0] == 1
    except Exception as e:
        print("Error:", e)


# Funcion para generar una cadena aleatoria
def cadena_random(lenght):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(lenght))


# Funcion para generar un email aleatorio
def random_email():
    return cadena_random(10) + "@gmail.com"


# Funcion para generar datos aleatorios
def random_data():
    data = {
        "nombre": cadena_random(6),
        "apPat": cadena_random(6),
        "apMat": cadena_random(6),
        "password": cadena_random(8),
        "email": random_email(),
        "profilePicture": None,
        "superUser": random.choice([0, 1]),
    }
    return data


# Funcion para obtener el ultimo ID insertado en una tabla
def obtener_ultimo_id(tabla: str):
    try:
        with connection.cursor() as cursor:
            if tabla == "usuarios":
                sql = f"SELECT MAX(idUsuario) AS maximo_valor FROM usuarios"  # Cambiar por el campo ID correcto si no es idUsuario
            else:
                sql = f"SELECT MAX(idPelicula) AS maximo_valor FROM peliculas"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result[0]["maximo_valor"]
    except Exception as e:
        print("Error al obtener el último ID:", e)


# ///////////////////////////////////////////////////////////////////////////////// 1) Funcion para insertar datos aleatorios en las 3 tablas
def insertar_en_tablas():
    usuario_data = random_data()  # Para generar datos aleatorios
    create("usuarios", usuario_data)

    pelicula_data = {
        "nombre": cadena_random(14),
        "genero": cadena_random(15),
        "duracion": random.randint(60, 180),
        "inventario": random.randint(1, 50),
    }
    create("peliculas", pelicula_data)

    id_usuario = obtener_ultimo_id("usuarios")  # el ultimo insertado

    id_pelicula = obtener_ultimo_id("peliculas")  # ultima peli insertada

    rentar_data = {
        "idUsuario": id_usuario,
        "idPelicula": id_pelicula,
        "fecha_renta": "2021-06-30",
        "dias_de_renta": random.randint(1, 7),
        "estatus": random.randint(0, 1),
    }

    create("rentar", rentar_data)


# ///////////////////////////////////////////////////////////////////////////////// 2)Funcion que filtra a la tabla Usuario a todos los usuarios cuyo apellido termine en alguna cadena especificada por el usuario
def filtrar_apPat(cadena: str):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM usuarios WHERE apPat LIKE %s"
            cursor.execute(sql, (f"%{cadena}",))
            results = cursor.fetchall()
            formatted_results = []  # pone chulo el resultado
            for user in results:
                formatted_user = f"ID: {user['idUsuario']}, Nombre: {user['nombre']} ApellidoP: {user['apPat']} ApellidoM: {user['apMat']}, Email: {user['email'],}"
                formatted_results.append(formatted_user)
            return formatted_results
    finally:
        connection.close()


# ///////////////////////////////////////////////////////////////////////////////// 3)funcion que dado el nombre de una pelicula(input) y un genero, si dicha pelicula existe, se le cambie el genero a dicha pelicula
def cambiar_genero_pelicula(nombre_pelicula: str, genero: str):
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE peliculas SET genero = %s WHERE nombre = %s"
            cursor.execute(sql, (genero, nombre_pelicula))
        connection.commit()
    finally:
        connection.close()


if __name__ == "__main__":

    insertar_en_tablas()  # Descomentar para insertar datos aleatorios

    # create("usuarios", {"nombre": "Juan", "apPat": "Perez", "apMat": "Gomez
