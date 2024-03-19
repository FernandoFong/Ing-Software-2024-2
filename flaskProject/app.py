from flask import Flask, render_template
from alchemyClasses import db
from contollers.ControllerPelicula import pelicula_blueprint
from contollers.PrimerControlador import mi_primer_blueprint
from contollers.ControllerAlumno import alumno_blueprint
from contollers.ControllerUsuario import usuario_blueprint
from contollers.ControllerRenta import renta_blueprint
from flask import Flask
from sqlalchemy import and_, or_
from alchemyClasses.Usuario import Usuario
from alchemyClasses.Pelicula import Pelicula
from alchemyClasses.Renta import Renta
from alchemyClasses import db
from cryptoUtils.CryptoUtils import cipher
from hashlib import sha256
from datetime import date
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)
app.register_blueprint(mi_primer_blueprint)
app.register_blueprint(alumno_blueprint)
app.register_blueprint(pelicula_blueprint)
app.register_blueprint(usuario_blueprint)
app.register_blueprint(renta_blueprint)
@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
