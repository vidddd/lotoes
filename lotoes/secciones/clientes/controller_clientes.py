
from flask import url_for, redirect, Blueprint, render_template
from markupsafe import escape
from .forms_clientes import ClienteForm
from .model_cliente import Cliente
from flask_login import login_required
from werkzeug.exceptions import NotFound

BP_NM = 'clientes'

clientes = Blueprint(BP_NM, __name__, template_folder='templates')

@clientes.route('/')
@login_required
def clientes_index():
    clientes = Cliente.get_all()
    return render_template('clientes.html', clientes=clientes, seccion='clientes')

@clientes.route('/form', methods=['GET', 'POST'], defaults={'cliente_id': None})
@clientes.route('/form/<int:cliente_id>', methods=['GET', 'POST'])
@login_required
def cliente_form(cliente_id=None):
    form = ClienteForm()
    if cliente_id:
        cliente_to_update = Cliente.get_by_id(cliente_id)
    else:
        print ("nuevo")
    if form.validate_on_submit():
        cliente = Cliente(nombre=form.nombre.data, 
                          tipo_cliente=form.tipo_cliente.data,
                          clasificacion_interna= form.clasificacion_interna.data,
                          es_empresa=form.es_empresa.data,
                          persona_contacto=form.persona_contacto.data,
                          tipo_documento=form.tipo_documento.data,
                          documento=form.documento.data,
                          telefono=form.telefono.data,
                          movil=form.movil.data,
                          email=form.email.data,
                          web=form.web.data,
                          direccion=form.direccion.data,
                          municipio=form.municipio.data,
                          provincia=form.provincia.data,
                          cp=form.cp.data,
                          pais=form.pais.data,
                          tiene_credito=form.tiene_credito.data,
                          credito=form.credito.data,
                          visible=form.visible.data,
                          saldo=form.saldo.data,
                          deuda=form.deuda.data,
                          notas=form.notas.data )        
        cliente.save()
        return redirect(url_for('clientes.clientes_index'))
    return render_template('form_cliente.html', form=form, seccion='clientes')

@clientes.route('/cliente/<int:cliente_id>')
@login_required
def cliente(cliente_id):
    cliente = Cliente.get_by_id(cliente_id)
    if cliente is None:
        raise NotFound(cliente_id)
    return render_template('cliente.html', cliente=cliente, seccion='clientes')