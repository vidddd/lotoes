from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, StringField, SubmitField, TextField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
from lotoes.lotoes_config import tipo_documento, tipo_cliente

class ClienteForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=255)])
    tipo_cliente = SelectField('Tipo Cliente', choices=tipo_cliente)
    es_empresa = BooleanField('Es Empresa ?')
    persona_contacto = StringField('Persona Contacto', validators=[Length(max=255)])
    tipo_documento = SelectField('Tipo Documento', choices=tipo_documento, validators=[DataRequired()])
    documento = StringField('Documento', validators=[DataRequired(), Length(max=15)])
    telefono = StringField('Telefono', validators=[DataRequired(), Length(max=15)])
    movil = StringField('Movil', validators=[Length(max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    direccion = StringField('Direccion', validators=[Length(max=250)])
    municipio = StringField('Municipio', validators=[Length(max=250)])
    provincia = IntegerField('Provincia')
    cp = IntegerField('Codigo Postal')
    pais = IntegerField('Pais')
    tiene_credito = BooleanField('Tiene Credito ?')
    credito = FloatField('Credito')
    notas = TextAreaField('Notas')
    submit = SubmitField('Guardar')