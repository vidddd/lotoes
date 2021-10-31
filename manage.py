"""Manger script."""
import os
from lotoes import db, create_app
from initial_data import usuarios
from lotoes.model_usuario import Usuario

env = os.getenv('FLASK_CONFIG')
#if env is None or env not in ["test", "prod"]:
env = "dev"

app = create_app(env)
app.app_context().push()


print(usuarios)

#db.drop_all()
#db.create_all()