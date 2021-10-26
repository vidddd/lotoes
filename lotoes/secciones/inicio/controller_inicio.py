
from flask import Blueprint,render_template

BP_NM = 'inicio'

inicio = Blueprint(BP_NM, __name__, template_folder='templates')
 
@inicio.route('/')
def inicio_func():
    return render_template('inicio.html')

@inicio.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')