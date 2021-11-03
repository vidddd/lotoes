
from flask import url_for, redirect, Blueprint, render_template, request
from .model_usuario import Usuario
from .forms import UsuarioForm, LoginForm
from werkzeug.urls import url_parse
from flask_login import login_required, login_user, logout_user, current_user

BP_NM = 'usuarios'

usuarios = Blueprint(BP_NM, __name__, template_folder='templates')


@usuarios.route('/')
@login_required
def usuarios_func():
    usuarios = Usuario.get_all()
    return render_template('usuarios.html', usuarios=usuarios, seccion="usuarios")

@usuarios.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('inicio'))
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.get_by_email(form.email.data)
        if usuario is not None and usuario.check_password(form.password.data):
            login_user(usuario, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('inicio.inicio_func')
            return redirect(next_page)
        
    return render_template('login.html', form=form, seccion="usuarios")

@usuarios.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('usuarios.login'))

@usuarios.route('/usuarios/&lt;username&gt;')
@login_required
def user(username):
    return render_template('clientes.html', cliente=cliente, seccion="usuarios")