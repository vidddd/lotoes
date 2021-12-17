from flask import url_for, redirect, Blueprint, render_template, request, current_app
from .model_administracion import Administracion
from .form_administracion import AdministracionForm
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.exceptions import NotFound

BP_NM = 'administraciones'

administraciones = Blueprint(BP_NM, __name__, template_folder='templates')

@administraciones.route('/')
@login_required
def administraciones_index():
    administraciones = Administracion.get_all()
    return render_template('administraciones.html', administraciones=administraciones, seccion="administraciones")

@administraciones.route('/new', methods=['GET', 'POST'], defaults={'usuario_id': None})
@login_required
def administraciones_form(usuario_id=None):
    form = AdministracionForm()
    if form.validate_on_submit():
        administracion = Administracion(
            nombre=form.nombre.data, 
            contacto=form.contacto.data, 
            codigoSelae=form.codigoSelae.data, 
            telefono=form.telefono.data,
            movil=form.movil.data,
            email=form.email.data,
            web=form.web.data,
            direccion=form.direccion.data,
            municipio=form.municipio.data,
            cp=form.cp.data,
            provincia_id=form.provincias.data.id,
            notas=form.notas.data)
        administracion.save()
        return redirect(url_for('administraciones.administraciones_index'))
    return render_template('form_administracion.html', form=form, seccion='administraciones')

@administraciones.route('/administracion/<int:administracion_id>')
@login_required
def administracion(administracion_id):
    administracion = Administracion.get_by_id(administracion_id)
    if administracion is None:
        raise NotFound(administracion_id)
    return render_template('administracion.html', administracion=administracion, seccion='administraciones')
    

@administraciones.route('/<int:administracion_id>/edit', methods=['GET', 'POST'])
@login_required
def administracion_edit(administracion_id=None):
    administracion = Administracion.get_by_id(administracion_id)
    if administracion is None:
        raise NotFound(administracion_id)
    form = AdministracionForm()
    if form.validate_on_submit():
        administracion.nombre=form.nombre.data, 
        administracion.contacto=form.contacto.data, 
        administracion.codigoSelae=form.codigoSelae.data, 
        administracion.telefono=form.telefono.data,
        administracion.movil=form.movil.data,
        administracion.email=form.email.data,
        administracion.web=form.web.data,
        administracion.direccion=form.direccion.data,
        administracion.municipio=form.municipio.data,
        administracion.cp=form.cp.data,
        administracion.provincia_id=form.provincias.data.id,
        administracion.notas=form.notas.data
        administracion.save()
        return redirect(url_for('administraciones.administraciones_index'))
    
    form.nombre.data=administracion.nombre, 
    form.contacto.data=administracion.contacto, 
    form.codigoSelae.data=administracion.codigoSelae, 
    form.telefono.data=administracion.telefono,
    form.movil.data=administracion.movil,
    form.email.data=administracion.email,
    form.web.data=administracion.web,
    form.direccion.data=administracion.direccion,
    form.municipio.data=administracion.municipio,
    form.cp.data=administracion.cp,
    #form.provincias.data.id=administracion.provincia_id,
    form.notas.data=administracion.notas
    
    return render_template('form_administracion.html', form=form, seccion='administraciones')
