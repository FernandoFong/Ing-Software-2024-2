from flask import Flask
import os
from sqlalchemy import and_, or_

from alchemyClasses import db
from alchemyClasses.Pelicula import Pelicula
from alchemyClasses.Renta import Renta
from alchemyClasses.Usuario import Usuario
from cryptoUtils.CryptoUtils import cipher
from hashlib import sha256

from model.model_pelicula import *
from model.model_usuario import *
from model.model_renta import *

#mysql+pymysql://ferfong:Developer123!@localhost:3306/ing_soft
#<dialecto>+<driver>://<usuario>:<passwd>@localhost:3306/<db>
#mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_soft
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)


def dejar_espacios():
    for i in range(5):
        print("\n")

if __name__ == '__main__':
    with app.app_context():
        while True:
            print("----------|| GESTOR DE OPCIONES ||----------")
            print("1) Ver registros")
            print("2) Filtrar registro por ID")
            print("3) Actualizar nombre o fecha de renta")
            print("4) Eliminar registro")
            print("5) Eliminar todos los registros")
            print("6) Salir")

            opcion = input("Ingrese el número de la opción que desea ejecutar: ")

            if opcion == "1":
                print("-----|| VER REGISTROS ||-----")
                dejar_espacios()
                tabla = input("Ingrese la tabla que desea manipular\n1)Usuario\n2)Pelicula\n3)Renta\n ")
                if tabla == "1":
                    muestra_todos_usuarios()
                elif tabla == "2":
                    muestra_todas_peliculas()

                elif tabla == "3":
                    muestra_todas_rentas()

                else:
                    print("Opcion inválida.")

            elif opcion == "2":
                print("-----|| FILTRAR POR ID ||-----")
                dejar_espacios()
                tabla = input("Ingrese la tabla que desea manipular\n1)Usuario\n2)Pelicula\n3)Renta\n ")
                if tabla == "1":
                    entrada= input("Ingrese el ID del usuario que desea filtrar: ")
                    print("===================================================================")
                    filtrar_por_id_usuario(entrada)
                    print("===================================================================")

                elif tabla == "2":
                    entrada = input("Ingrese el ID de la pelicula que desea filtrar: ")
                    print("===================================================================")
                    filtrar_por_id_pelicula(entrada)
                    print("===================================================================")


                elif tabla == "3":
                    entrada = input("Ingrese el ID de la renta que desea filtrar: ")
                    print("===================================================================")
                    filtrar_por_id_renta(entrada)
                    print("===================================================================")

                else:
                    print("Opcion inválida.")

            elif opcion == "3":
                print("-----|| ACTUALIZAR NOMBRE ||-----")
                dejar_espacios()
                tabla = input("Ingrese la tabla que desea manipular\n1)Usuario\n2)Pelicula\n3)Renta\n ")
                if tabla == "1":
                    id_usuario = input("Ingrese el ID del usuario que desea actualizar: ")
                    nuevo_nombre = input("Ingrese el nuevo nombre del usuario: ")
                    actualizar_nombre_usuario(id_usuario, nuevo_nombre)
                elif tabla == "2":
                    id_pelicula = input("Ingrese el ID de la pelicula que desea actualizar: ")
                    nuevo_nombre = input("Ingrese el nuevo nombre de la pelicula: ")
                    actualizar_nombre_pelicula(id_pelicula, nuevo_nombre)

                elif tabla == "3":
                    id_rentar = input("Ingrese el ID de la renta que desea actualizar: ")
                    nueva_fecha = input("Ingrese la nueva fecha de la renta(formato: YYYY-MM--DD): ")
                    actualizar_fecha_renta(id_rentar, nueva_fecha)
                else:
                    print("Tabla inválida.")

            elif opcion == "4":
                print("-----|| ELIMINAR REGISTRO ||-----")
                dejar_espacios()

                tabla = input("Ingrese la tabla que desea manipular\n1)Usuario\n2)Pelicula\n3)Renta\n ")
                if tabla == "1":
                    id_usuario = input("Ingrese el ID del usuario que desea eliminar: ")
                    borra_usuario(id_usuario)
                elif tabla == "2":
                    id_pelicula = input("Ingrese el ID de la pelicula que desea eliminar:")
                    borra_pelicula(id_pelicula)
                elif tabla == "3":
                    id_renta= input("Ingrese el ID de la renta que desea elimnar:")
                    borra_renta(id_renta)
                else:
                    print("Tabla inválida.")

            elif opcion == "5":
                print("-----|| ELIMINAR TODOS LOS REGISTROS ||-----")
                dejar_espacios()

                tabla = input("Ingrese la tabla que desea manipular\n1)Usuario\n2)Pelicula\n3)Renta\n ")
                if tabla == "1":
                    borra_todos_usuarios()
                elif tabla == "2":
                    borra_todas_peliculas()
                elif tabla == "3":
                    borra_todas_rentas()
                else:
                    print("Tabla inválida.")

            elif opcion == "6":
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Por favor ingrese un número válido del 1 al 6.")


