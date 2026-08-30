from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ClienteForm(FlaskForm):
    nombre = StringField('Nombre Completo', validators=[
        DataRequired(message="El nombre es obligatorio."),
        Length(min=2, max=50)
    ])
    email = StringField('Correo Electrónico', validators=[
        DataRequired(message="El correo es obligatorio."),
        Email(message="Ingrese un correo electrónico válido.")
    ])
    telefono = StringField('Teléfono', validators=[
        DataRequired(message="El teléfono es obligatorio."),
        Length(min=7, max=15)
    ])
    submit = SubmitField('Guardar Cliente')