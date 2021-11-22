from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, StringField, SubmitField, TextField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
from wtforms.fields.html5 import DateField
from lotoes.lotoes_config import tipo_documento, tipo_cliente, clasificacion_interna
from .model_cliente import Provincia, getProvincia
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class ClienteForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=255)])
    tipo_cliente = SelectField('Tipo Cliente', choices=tipo_cliente)
    clasificacion_interna = SelectField('Clasificacion Interna', choices=clasificacion_interna)
    es_empresa = BooleanField('Es Empresa ?')
    persona_contacto = StringField('Persona Contacto', validators=[Length(max=255)])
    tipo_documento = SelectField('Tipo Documento', choices=tipo_documento)
    documento = StringField('Documento', validators=[DataRequired(), Length(max=15)])
    telefono = StringField('Telefono', validators=[Length(max=15)])
    movil = StringField('Movil', validators=[Length(max=15)])
    email = StringField('Email', validators=[Length(max=100), Email()])
    web = StringField('Web', validators=[Length(max=150)])
    direccion = StringField('Direccion', validators=[Length(max=250)])
    municipio = StringField('Municipio', validators=[Length(max=250)])
    provincia = QuerySelectField(u'Provincia', query_factory=getProvincia, get_label='nombre', allow_blank=True,blank_text=(u"-- Seleccione --"), )
    cp = IntegerField('Codigo Postal')
    pais = StringField('Pais', validators=[Length(max=100)])
    tiene_credito = BooleanField('Tiene Credito ?')
    credito = FloatField('Credito')
    visible = BooleanField('Visible ?')
    saldo = FloatField('Saldo')
    deuda = FloatField('Deuda')
    fecha_nacimiento = DateField('Fecha Nacimiento')
    notas = TextAreaField('Notas')
    submit = SubmitField('Guardar')