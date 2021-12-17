from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, StringField, SubmitField, TextField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
from lotoes.secciones.clientes.model_cliente import Provincia, getProvincia
from wtforms.ext.sqlalchemy.fields import QuerySelectField

def provincias_all():
    return Provincia.get_all()

class AdministracionForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=256)])
    contacto = StringField('Persona Contacto', validators=[Length(max=256)])
    codigoSelae = IntegerField()
    telefono = StringField('Teléfono', validators=[Length(max=15)])
    movil = StringField('Movil', validators=[Length(max=15)])
    email = StringField('Email', validators=[Length(max=100)])
    web = StringField('Web', validators=[Length(max=100)])
    direccion = StringField('Direccion', validators=[Length(max=256)])
    municipio = StringField('Municipio', validators=[Length(max=2556)])
    cp = IntegerField('Codigo Postal', validators=[DataRequired()])
    provincias = QuerySelectField(query_factory=provincias_all, allow_blank=True, get_label='nombre', validators=[DataRequired()])
    notas = TextAreaField('Notas')
    submit = SubmitField('Guardar')
    
