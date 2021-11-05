
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
    return render_template('clientes.html', clientes=clientes, seccion='clientes')

@clientes.route('/form', methods=['GET', 'POST'], defaults={'cliente_id': None})
@clientes.route('/form/<int:cliente_id>', methods=['GET', 'POST'])
@login_required
def clientes_form(cliente_id=None):
    form = ClienteForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        tipo_cliente = form.tipo_cliente.data
        es_empresa = form.es_empresa.data
        persona_contacto = form.persona_contacto.data
        tipo_documento = form.tipo_documento.data
        documento = form.documento.data
        telefono = form.telefono.data
        movil = form.movil.data
        email = form.email.data
        direccion = form.direccion.data
        municipio = form.municipio.data
        provincia = form.provincia.data
        cp = form.cp.data
        pais = form.pais.data
        tiene_credito = form.tiene_credito.data
        credito = form.credito.data
        notas = form.notas.data
        cliente = Cliente(nombre=nombre, tipo_cliente=tipo_cliente, es_empresa=es_empresa, persona_contacto=persona_contacto, tipo_documento=tipo_documento, documento=documento, telefono=telefono, movil=movil, email=email, direccion=direccion, municipio=municipio, provincia=provincia, cp=cp, pais=pais, tiene_credito=tiene_credito, credito=credito, notas=notas )
        cliente.save()
        return redirect(url_for('clientes'))
    return render_template('form_cliente.html', form=form, seccion='clientes')

@clientes.route('/cliente/<int:id>')
@login_required
def cliente(id):
    return render_template('cliente.html', id=escape(id),seccion='clientes')