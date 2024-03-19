from flask import Blueprint, request, render_template, flash, url_for, Flask
from random import randint
from alchemyClasses import db
from alchemyClasses.Usuario import Usuario
from flask_sqlalchemy import SQLAlchemy
from flask import redirect
from sqlalchemy.exc import IntegrityError
from hashlib import sha256

usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuario')
@usuario_blueprint.route('/')
def ver_usuarios():
    usuarios = Usuario.query.all()
    return render_template('ver_usuarios.html', usuarios=usuarios)
@usuario_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'GET':
        return render_template('add_usuario.html')
    else:
        nuevo_usuario = Usuario(
            nombre=request.form['name'],
            apPat=request.form['ap_pat'],
            apMat=request.form['ap_mat'],
            password=sha256(request.form['passwd'].encode()).hexdigest(),
            email=request.form['email']
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash('Usuario agregado con éxito!')
        return render_template('usuario_added.html', name=nuevo_usuario.nombre, ap_pat=nuevo_usuario.apPat, ap_mat=nuevo_usuario.apMat, passwd=nuevo_usuario.password, email=nuevo_usuario.email)

@usuario_blueprint.route('/eliminar/<int:id_usuario>', methods=['POST'])
def eliminar_usuario(id_usuario):
    try:
        usuario_a_eliminar = Usuario.query.get_or_404(id_usuario)
        db.session.delete(usuario_a_eliminar)
        db.session.commit()
        flash('Usuario eliminado con éxito.')
    except IntegrityError:
        db.session.rollback()  # Es importante hacer rollback para resetear el estado de la sesión.
        flash('Este Usuario no puede ser eliminado porque actualmente está rentando algo.')
    return redirect(url_for('usuario.ver_usuarios'))

@usuario_blueprint.route('/editar/<int:id_usuario>', methods=['GET', 'POST'])
def editar_usuario(id_usuario):
    if request.method == 'GET':
        usuario = Usuario.query.get_or_404(id_usuario)
        return render_template('editar_usuario.html', usuario=usuario)
    else:
        usuario = Usuario.query.get_or_404(id_usuario)
        usuario.nombre = request.form['name'],
        usuario.apPat = request.form['ap_pat'],
        usuario.apMat = request.form['ap_mat'],
        usuario.password = sha256(request.form['passwd'].encode()).hexdigest(),
        usuario.email = request.form['email']
        db.session.commit()
        flash('Usuario actualizado con éxito.')
        return redirect(url_for('usuario.ver_usuarios'))