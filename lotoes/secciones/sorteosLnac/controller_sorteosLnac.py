
from flask import url_for, redirect, Blueprint, render_template, request
from .model_sorteoLnac import SorteoLnac
#from .forms import UsuarioForm
from flask_login import login_required, login_user, logout_user, current_user

BP_NM = 'sorteosLnac'

sorteosLnac = Blueprint(BP_NM, __name__, template_folder='templates')


@sorteosLnac.route('/')
@login_required
def sorteosLnac_func():
    sorteosLnac = SorteoLnac.get_all()
    return render_template('sorteosLnac.html', sorteosLnac=sorteosLnac, seccion="sorteos")

@sorteosLnac.route('/sorteoLnac/&lt;id&gt;')
@login_required
def user(username):
    return render_template('clientes.html', cliente=cliente, seccion="sorteos")