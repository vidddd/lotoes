from flask import url_for, redirect, Blueprint, render_template, request, current_app
from .model_consignacion import Consignacion
from .form_Consignacion import ConsignacionForm
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.exceptions import NotFound

BP_NM = 'consignaciones'

consignaciones = Blueprint(BP_NM, __name__, template_folder='templates')

@consignaciones.route('/')
@login_required
def consignaciones_index():
    Consignaciones = Consignacion.get_all()
    return render_template('consignaciones.html', consignaciones=consignaciones, seccion="consignaciones")

@consignaciones.route('/new', methods=['GET', 'POST'], defaults={'usuario_id': None})
@login_required
def Consignaciones_form(usuario_id=None):
    form = ConsignacionForm()
    if form.validate_on_submit():
        Consignacion = Consignacion(
            nombre=form.nombre.data)
        Consignacion.save()
        return redirect(url_for('consignaciones.consignaciones_index'))
    return render_template('form_consignacion.html', form=form, seccion='Consignaciones')

'''
@consignaciones.route('/consignacion/<int:consignacion_id>')
@login_required
def Consignacion(consignacion_id):
    Consignacion = Consignacion.get_by_id(Consignacion_id)
    if consignacion is None:
        raise NotFound(consignacion_id)
    return render_template('consignacion.html', consignacion=consignacion, seccion='consignaciones')
    

@consignaciones.route('/<int:consignacion_id>/edit', methods=['GET', 'POST'])
@login_required
def consignacion_edit(consignacion_id=None):
    consignacion = Consignacion.get_by_id(consignacion_id)
    if consignacion is None:
        raise NotFound(consignacion_id)
    form = ConsignacionForm()
    if form.validate_on_submit():
        consignacion.nombre=form.nombre.data
        consignacion.save()
        return redirect(url_for('consignaciones.consignaciones_index'))
    
    form.nombre.data=consignacion.nombre
    
    return render_template('form_consignacion.html', form=form, seccion='consignaciones')
'''