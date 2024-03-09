from flask import Blueprint, render_template

mi_primer_blueprint = Blueprint('mpb', __name__, url_prefix='/mpb')

@mi_primer_blueprint.route('/')
def fun():
    return "Hello from Blueprint"


@mi_primer_blueprint.route("/html")
def html_controller():
    return render_template('html_bueno_ahorasi.html')