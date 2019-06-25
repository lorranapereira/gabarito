from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,RadioField,PasswordField,TextAreaField,IntegerField
from wtforms.validators import DataRequired,Optional,NumberRange, Length
from wtforms_components import EmailField
from wtforms.widgets.html5 import NumberInput
class formulario(FlaskForm):
    login = StringField('Login',validators=[DataRequired()])
    idade = IntegerField('Idade',widget=NumberInput(step=1,max=99),validators=[DataRequired()])
    codigo = IntegerField('Codigo',validators=[DataRequired()])
    enviar = SubmitField('Enviar')