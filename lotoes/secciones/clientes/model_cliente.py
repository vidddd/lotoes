from sqlalchemy.exc import IntegrityError
from lotoes import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #user_id = db.Column(db.Integer, db.ForeignKey('blog_user.id', ondelete='CASCADE'), nullable=False)
    nombre = db.Column(db.String(256), nullable=False)
    tipo_cliente = db.Column(db.Integer())
    es_empresa = db.Column(db.Boolean)
    persona_contacto = db.Column(db.String(256), nullable=False)
    nif = db.Column(db.String(15), nullable=False)
    telefono = db.Column(db.String(15), nullable=False)
    movil = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(256), nullable=False)
    municipio = db.Column(db.String(256), nullable=False)
    provincia = db.Column(db.Integer(), nullable=False)
    cp = db.Column(db.Integer(), nullable=False)
    pais = db.Column(db.Integer(), nullable=False)
    notas = db.Column(db.Text, nullable=False)

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