from config import config

def mount_blueprints(app, config_name):
    if not app:
        return
    
    from lotoes.secciones.inicio import inicio
    from lotoes.secciones.clientes import clientes
    from lotoes.secciones.usuarios import usuarios
    from lotoes.secciones.sorteosLnac import sorteosLnac
    from lotoes.secciones.api import api

    app.register_blueprint(inicio, url_prefix='')
    app.register_blueprint(clientes, url_prefix='/clientes')
    app.register_blueprint(usuarios, url_prefix='/usuarios')
    app.register_blueprint(sorteosLnac, url_prefix='/sorteosLnac')
    app.register_blueprint(api, url_prefix='/api/v1')