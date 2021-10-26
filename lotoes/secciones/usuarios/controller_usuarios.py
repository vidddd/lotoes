
from flask import (
    url_for,
    redirect,
    Blueprint,
    render_template
)

BP_NM = 'clientes'

clientes = Blueprint(BP_NM, __name__, template_folder='templates')



@clientes.route('/')
def clientes_func():
    print(clientes.root_path)
    #return redirect(url_for('blog.index'))
    return render_template('clientes.html')

@clientes.route('/clientes/&lt;username&gt;')
def user(username):
    return render_template('clientes.html', cliente=cliente)