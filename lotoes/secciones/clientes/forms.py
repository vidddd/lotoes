from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, StringField, SubmitField, TextField, BooleanField
from wtforms.validators import DataRequired, Email, Length


class ClienteForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=255)])
    tipo_cliente = BooleanField('tipo_cliente')
    es_empresa = BooleanField('es_empresa')
    persona_contacto = StringField('Persona Contacto', validators=[Length(max=255)])
    nif = StringField('Nif / DNI / NIE', validators=[DataRequired(), Length(max=15)])
    telefono = StringField('Telefono', validators=[DataRequired(), Length(max=15)])
    movil = StringField('Movil', validators=[Length(max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    direccion = StringField('Direccion', validators=[Length(max=250)])
    tiene_credito = BooleanField('tiene_credito')
    credito = FloatField('credito')
    tipo_cliente = IntegerField('tipo_cliente')
    notas = TextField('notas')
    submit = SubmitField('Guardar')