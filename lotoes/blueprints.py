from config import config

def mount_blueprints(app, config_name):
    if not app:
        return
    
    from lotoes.secciones.inicio import inicio
    from lotoes.secciones.clientes import clientes
    #from yapper.blueprints.user import user
    #from yapper.blueprints.blog import blog
    #from yapper.blueprints.api import api

    app.register_blueprint(inicio, url_prefix='')
    app.register_blueprint(clientes, url_prefix='/clientes')
    
    '''app.register_blueprint(api, url_prefix='/api/v1')'''