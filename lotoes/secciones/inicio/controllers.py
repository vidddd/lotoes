import os

from flask import (
    url_for,
    send_from_directory,
    redirect,
    Blueprint
)

from ..usuarios.models import Permission
from config import basedir
from flask import render_template

BP_NM = 'inicio'

inicio = Blueprint(BP_NM, __name__, template_folder='views')

TEMPLATE_DIR = os.path.join(basedir, 'templates')
STATIC_DIR = os.path.join(TEMPLATE_DIR, 'static')


@inicio.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)


@inicio.route('/')
def index():
    #return redirect(url_for('inicio.index'))
    return render_template('inicio/index.html')


@inicio.route('/favicon.ico')
def favicon():
    return send_from_directory(
        STATIC_DIR,
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )
