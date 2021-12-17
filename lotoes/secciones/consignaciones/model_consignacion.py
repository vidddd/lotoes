from sqlalchemy.exc import IntegrityError
from lotoes import db
from datetime import datetime

class Consignacion(db.Model):
    __tablename__ = 'administraciones'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime())

    def __repr__(self):
        return f'<Consignacion {self.nombre}>'

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
        return Consignacion.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Consignacion.query.get(id)