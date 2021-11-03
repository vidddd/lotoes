from sqlalchemy.exc import IntegrityError
from lotoes import db
from datetime import datetime

class SorteoLnac(db.Model):
    __tablename__ = 'sorteosLnac'
    id = db.Column(db.Integer, primary_key=True)
    #user_id = db.Column(db.Integer, db.ForeignKey('blog_user.id', ondelete='CASCADE'), nullable=False)
    nombre = db.Column(db.String(256), nullable=False)
    codigo = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.Integer, nullable=False)
    ano = db.Column(db.Integer, nullable=False)


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