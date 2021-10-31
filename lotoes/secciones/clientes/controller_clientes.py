
from flask import url_for, redirect, Blueprint, render_template
from markupsafe import escape
from .forms import ClienteForm
from .model_cliente import Cliente
from flask_login import login_required

BP_NM = 'clientes'

clientes = Blueprint(BP_NM, __name__, template_folder='templates')

@clientes.route('/')
@login_required
def clientes_func():
    clientes = Cliente.get_all()
    return render_template('clientes.html', clientes=clientes)

@clientes.route('/form', methods=['GET', 'POST'], defaults={'cliente_id': None})
@clientes.route('/form/<int:cliente_id>', methods=['GET', 'POST'])
@login_required
def clientes_form(cliente_id=None):
    form = ClienteForm()
    if form.validate_on_submit():
        print('clientes form')
        nombre = form.nombre.data
        es_empresa = form.es_empresa.data
        print(nombre)
    return render_template('form_cliente.html', form=form)

@clientes.route('/cliente/<int:id>')
@login_required
def cliente(id):
    return render_template('cliente.html', id=escape(id))