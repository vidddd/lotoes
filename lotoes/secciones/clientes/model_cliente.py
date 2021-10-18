
from lotoes import db
from lotoes.lib.base_model import BaseModel
from sqlalchemy.dialects.postgresql import SMALLINT

class Cliente(BaseModel):
    __tablename__ = 'clientes'
    author_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    nombre = db.Column(db.String(256))
    es_empresa = db.Column(db.Boolean, default=False)
    observaciones = db.Column(db.Text, default='')