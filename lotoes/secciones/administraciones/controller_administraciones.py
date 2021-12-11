
from flask import url_for, redirect, Blueprint, render_template, request, current_app
from .model_administracion import Administracion
from .form_administracion import AdministracionForm
from flask_login import login_required, login_user, logout_user, current_user
from .model_administracion import Administracion
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
            notas=form.notas.data)
        administracion.save()
        return redirect(url_for('administraciones.administraciones_index'))
    return render_template('form_administracion.html', form=form, seccion='administraciones')

@administraciones.route('/administracion/<int:administracion_id>')
@login_required
def administracion(administracion_id):
    administracion = Administracion.get_by_id(administracion_id)
    #raise NotFound(administracion_id)
    if administracion is None:
        raise NotFound(administracion_id)
    return render_template('administracion.html', administracion=administracion, seccion='administraciones')
    

@administraciones.route('/<int:administracion_id>/edit', methods=['GET', 'POST'])
@login_required
def administraciones_edit(_id=None):
    usuario = Usuario.get_by_id(usuario_id)
    if usuario is None:
        raise NotFound(usuario_id)
    form = UsuarioForm()
    if form.validate_on_submit():
        usuario.name = form.name.data
        usuario.password = form.password.data
        usuario.email = form.email.data
        usuario.is_admin = form.is_admin.data
        usuario.save()
        return redirect(url_for('administraciones.administraciones_index'))
    
    form.name.data = usuario.name
    form.password.data = usuario.password
    form.email.data = usuario.email
    form.is_admin = form.is_admin
    
    return render_template('form_usuario.html', form=form, seccion='administraciones')
