
from flask import url_for, redirect, Blueprint, render_template
from markupsafe import escape

BP_NM = 'clientes'

clientes = Blueprint(BP_NM, __name__, template_folder='templates')



@clientes.route('/')
def clientes_func():
    return render_template('clientes.html')

@clientes.route('/cliente/<int:id>')
def cliente(id):
    return render_template('cliente.html', id=escape(id))