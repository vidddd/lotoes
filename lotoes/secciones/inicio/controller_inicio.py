
from flask import Blueprint,render_template
from flask_login import login_required

BP_NM = 'inicio'

inicio = Blueprint(BP_NM, __name__, template_folder='templates')
 
@inicio.route('/')
@login_required
def inicio_func():
    return render_template('inicio.html', seccion="inicio")

@inicio.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')