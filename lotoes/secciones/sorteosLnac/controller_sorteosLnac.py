
from flask import url_for, redirect, Blueprint, render_template, request
from .model_sorteoLnac import SorteoLnac
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.exceptions import NotFound

BP_NM = 'sorteosLnac'

sorteosLnac = Blueprint(BP_NM, __name__, template_folder='templates')


@sorteosLnac.route('/')
@login_required
def sorteosLnac_func():
    sorteosLnac = SorteoLnac.get_all()
    return render_template('sorteosLnac.html', sorteosLnac=sorteosLnac, seccion="sorteos")

@sorteosLnac.route('/sorteoLnac/<int:sorteo_id>')
@login_required
def sorteoLnac(sorteo_id):
    sorteo = SorteoLnac.get_by_id(sorteo_id)
    if sorteo is None:
        raise NotFound(sorteo_id)
    return render_template('sorteoLnac.html', sorteo=sorteo, seccion="sorteos")
