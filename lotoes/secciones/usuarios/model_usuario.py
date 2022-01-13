from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError

from lotoes import db
from lotoes import login_manager


class Usuario(db.Model, UserMixin):

    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    #def __init__(self, name, email):
    #    self.name = name
    #    self.email = email
    '''
    @property
    def password(self):
        """
        Prevent password from being accessed
        """
        raise AttributeError('password is not a readable attribute.')
    '''
    def __repr__(self):
        return f'<Usuario {self.email}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

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
                print(IntegrityError)
                count += 1

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Usuario.query.get(id)

    @staticmethod
    def get_by_email(email):
        return Usuario.query.filter_by(email=email).first()

    @staticmethod
    def get_all():
        return Usuario.query.all()


@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

class Rol(db.Model):
    """
    Create a Role table
    """

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(60), unique=True)
    descripcion = db.Column(db.String(200))
    usuarios = db.relationship('Usuario', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Rol: {}>'.format(self.nombre)
    
    @staticmethod
    def get_all():
        return Rol.query.all()

def roles_all():
    return Rol.get_all()