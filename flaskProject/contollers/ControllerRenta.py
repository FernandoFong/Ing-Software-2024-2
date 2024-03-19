from flask import Blueprint, request, render_template, flash, url_for, Flask
from random import randint
from alchemyClasses import db
from alchemyClasses.Renta import Renta
from flask_sqlalchemy import SQLAlchemy
from flask import redirect
from sqlalchemy.exc import IntegrityError
from datetime import date

renta_blueprint = Blueprint('renta', __name__, url_prefix='/renta')
@renta_blueprint.route('/')
def ver_rentas():
    rentas = Renta.query.all()
    return render_template('ver_rentas.html', rentas=rentas)
@renta_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_renta():
    if request.method == 'GET':
        return render_template('add_renta.html')
    else:
        nueva_renta = Renta(
            idPelicula=request.form['id_pelicula'],
            idUsuario=request.form['id_usuario'],
            fecha_renta=date.today(),
            dias_de_renta=5,
            estatus=0
        )
        db.session.add(nueva_renta)
        db.session.commit()
        flash('Renta agregada con éxito!')
        return render_template('renta_added.html', idPelicula=nueva_renta.idPelicula, idUsuario=nueva_renta.idUsuario, fecha_renta=nueva_renta.fecha_renta,
                               dias_de_renta=nueva_renta.dias_de_renta, estatus=nueva_renta.estatus)

@renta_blueprint.route('/editar/<int:id_renta>', methods=['GET', 'POST'])
def editar_renta(id_renta):
    if request.method == 'GET':
        renta = Renta.query.get_or_404(id_renta)
        return render_template('editar_renta.html', renta=renta)
    else:
        renta = Renta.query.get_or_404(id_renta)
        renta.estatus = request.form['estatus']
        db.session.commit()
        flash('Renta actualizada con éxito.')
        return redirect(url_for('renta.ver_rentas'))