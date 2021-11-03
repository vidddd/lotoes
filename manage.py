"""Manger script."""
import os
from lotoes import db, create_app
from initial_data import usuarios
from lotoes.secciones.usuarios.model_usuario import Usuario

env = os.getenv('FLASK_CONFIG')
#if env is None or env not in ["test", "prod"]:
env = "dev"

app = create_app(env)
app.app_context().push()

db.drop_all()


db.create_all()


obj_list = []
for usuario in usuarios:
    data_obj= Usuario(**usuario)
    obj_list.append(data_obj)

db.session.add_all(obj_list)
db.session.commit()