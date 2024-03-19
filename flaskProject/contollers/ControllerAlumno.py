from flask import Blueprint, request, render_template, flash, url_for
from random import randint

alumno_blueprint = Blueprint('alumno', __name__, url_prefix='/alumno')

@alumno_blueprint.route('/') #localhost:5000/alumno/
def ver_alumnos():
    return "select * from alumno"

#responde a localhost:5000/alumno/id/1
@alumno_blueprint.route('/id/<int:id_alumno>/<string:nombre>') #<tipo:nombre_variable>
def ver_alumno_id(id_alumno, nombre):
    return f"Se hace el query con el id {id_alumno} y el nombre {nombre}"


@alumno_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_alumno():
    if request.method == 'GET':
        return render_template('add_usuario.html')
    else:
        #Obtengo la información del método post.
        name = request.form['name']
        ap_pat = request.form['ap_pat']
        ap_mat = request.form['ap_mat']
        num_cta = request.form['num_cta']
        passwd = request.form['passwd']
        #Creo mi usuario.
        #alumno = Alumno(name, ap....)
        #Lo guardo en la DB
        #url_for
        #flash
        v = randint(0, 2)
        if v == 1:
            flash("Hello from flash!")
            return url_for('alumno.agregar_alumno')
        # Y regreso al flujo que me hayan especificado.
        return render_template('usuario_added.html', name=name, num_cta=num_cta)