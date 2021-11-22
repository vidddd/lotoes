from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, StringField, SubmitField, TextField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
from wtforms.fields.html5 import DateField
from lotoes.lotoes_config import tipo_sorteo_lnac

class SorteoLnacForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=255)])
    tipo_sorteo = SelectField('Tipo Sorteo', choices=tipo_sorteo_lnac)
    submit = SubmitField('Guardar')