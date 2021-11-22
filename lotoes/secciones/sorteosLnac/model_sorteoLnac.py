from sqlalchemy.exc import IntegrityError
from lotoes import db
from datetime import datetime

class SorteoLnac(db.Model):
    __tablename__ = 'sorteosLnac'
    id = db.Column(db.Integer, primary_key=True)
    #user_id = db.Column(db.Integer, db.ForeignKey('blog_user.id', ondelete='CASCADE'), nullable=False)
    nombre = db.Column(db.String(256), nullable=False)
    numero_sorteo = db.Column(db.Integer, nullable=False)
    ano_sorteo = db.Column(db.Integer, nullable=False)
    tipo_sorteo = db.Column(db.Integer, nullable=False)
    fecha_sorteo = db.Column(db.DateTime())
    fecha_caducidad = db.Column(db.DateTime())
    fracciones_consignadas = db.Column(db.Integer)
    fracciones_devueltas = db.Column(db.Integer)
    estado_consignacion = db.Column(db.Integer)
    porcentaje_paga_premios = db.Column(db.Integer)
    precio_billete = db.Column(db.Float)
    numero_series = db.Column(db.Integer)
    numero_billetes = db.Column(db.Integer)
    
    def __repr__(self):
        return f'<SorteoLnac {self.nombre}>'

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
        return SorteoLnac.query.all()
    
    @staticmethod
    def get_by_id(id):
        return SorteoLnac.query.get(id)