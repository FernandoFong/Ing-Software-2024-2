from flask import Blueprint, request, render_template, flash, url_for, Flask
from random import randint
from alchemyClasses import db
from alchemyClasses.Pelicula import Pelicula
from flask_sqlalchemy import SQLAlchemy
from flask import redirect
from sqlalchemy.exc import IntegrityError

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')
@pelicula_blueprint.route('/')
def ver_peliculas():
    peliculas = Pelicula.query.all()
    return render_template('ver_peliculas.html', peliculas=peliculas)
@pelicula_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_pelicula():
    if request.method == 'GET':
        return render_template('add_pelicula.html')
    else:
        nueva_pelicula = Pelicula(
            nombre=request.form['name'],
            genero=request.form['genre'],
            duracion=request.form['duration'],
            inventario=request.form['inventory']
        )
        db.session.add(nueva_pelicula)
        db.session.commit()
        flash('Pelicula agregada con éxito!')
        return render_template('pelicula_added.html', name= nueva_pelicula.nombre, genre= nueva_pelicula.genero, duration= nueva_pelicula.duracion, inventory= nueva_pelicula.inventario)

@pelicula_blueprint.route('/eliminar/<int:id_pelicula>', methods=['POST'])
def eliminar_pelicula(id_pelicula):
    try:
        pelicula_a_eliminar = Pelicula.query.get_or_404(id_pelicula)
        db.session.delete(pelicula_a_eliminar)
        db.session.commit()
        flash('Película eliminada con éxito.')
    except IntegrityError:
        db.session.rollback()  # Es importante hacer rollback para resetear el estado de la sesión.
        flash('Esta película no puede ser eliminada porque actualmente está en renta.')
    return redirect(url_for('pelicula.ver_peliculas'))

@pelicula_blueprint.route('/editar/<int:id_pelicula>', methods=['GET', 'POST'])
def editar_pelicula(id_pelicula):
    if request.method == 'GET':
        pelicula = Pelicula.query.get_or_404(id_pelicula)
        return render_template('editar_pelicula.html', pelicula=pelicula)
    else:
        pelicula = Pelicula.query.get_or_404(id_pelicula)
        pelicula.nombre = request.form['name']
        pelicula.genero = request.form['genre']
        pelicula.duracion = request.form.get('duration', type=int)
        pelicula.inventario = request.form.get('inventory', type=int)
        db.session.commit()
        flash('Película actualizada con éxito.')
        return redirect(url_for('pelicula.ver_peliculas'))