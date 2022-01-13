
from flask import url_for, redirect, Blueprint, render_template, request, current_app
from .model_usuario import Usuario
from .form_usuario import UsuarioForm, LoginForm
from werkzeug.urls import url_parse
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.exceptions import NotFound

BP_NM = 'usuarios'

usuarios = Blueprint(BP_NM, __name__, template_folder='templates')


@usuarios.route('/')
@login_required
def usuarios_index():
    current_app.logger.info('Mostrando los usuaruis del blog')
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

@usuarios.route('/form', methods=['GET', 'POST'], defaults={'usuario_id': None})
@login_required
def usuarios_form(usuario_id=None):
    form = UsuarioForm()
    print(form)
    if form.validate_on_submit():
        usuario = Usuario(name=form.name.data, email=form.email.data, password=form.password.data, is_admin=form.is_admin.data, rol_id=form.roles.data.id)
        usuario.save()
        return redirect(url_for('usuarios.usuarios_index'))
    return render_template('form_usuario.html', form=form, seccion='usuarios')

@usuarios.route('/<int:usuario_id>/edit', methods=['GET', 'POST'])
@login_required
def usuario_edit(usuario_id=None):
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
        return redirect(url_for('usuarios.usuarios_index'))
    
    form.name.data = usuario.name
    form.password.data = usuario.password
    form.email.data = usuario.email
    form.is_admin = usuario.is_admin
    form.roles = usuario.roles
    
    return render_template('form_usuario.html', form=form, seccion='usuarios')

@usuarios.route('/usuario/<int:usuario_id>')
@login_required
def usuario(usuario_id):
    usuario = Usuario.get_by_id(usuario_id)
    if usuario is None:
        raise NotFound(usuario_id)
    return render_template('usuario.html', usuario=usuario, seccion='usuarios')