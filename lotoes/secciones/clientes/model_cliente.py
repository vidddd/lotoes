from sqlalchemy.exc import IntegrityError
from lotoes import db
from datetime import datetime

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    #user_id = db.Column(db.Integer, db.ForeignKey('blog_user.id', ondelete='CASCADE'), nullable=False)
    nombre = db.Column(db.String(256), nullable=False)
    tipo_cliente = db.Column(db.Integer())
    es_empresa = db.Column(db.Boolean)
    persona_contacto = db.Column(db.String(256))
    nif = db.Column(db.String(15), nullable=False)
    telefono = db.Column(db.String(15))
    movil = db.Column(db.String(15))
    email = db.Column(db.String(100))
    direccion = db.Column(db.String(256))
    municipio = db.Column(db.String(256))
    provincia = db.Column(db.Integer())
    cp = db.Column(db.Integer())
    pais = db.Column(db.Integer())
    tiene_credito = db.Column(db.Boolean)
    credito = db.Column(db.Float)
    notas = db.Column(db.Text)
    creado = db.Column(db.DateTime(), default=datetime.utcnow)
    actualizado = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Cliente {self.nombre}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        saved = False
        count = 0
        while not saved:
            try:
                db.session.commit()
                saved = True
            except IntegrityError:
                count += 1
    @staticmethod
    def get_all():
        return Cliente.query.all()