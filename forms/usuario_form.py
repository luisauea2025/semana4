from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from models import Usuario

class RegistroForm(FlaskForm):
    usuario = StringField('Nombre de Usuario', validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirmar Contraseña', validators=[
        DataRequired(), 
        EqualTo('password', message='Las contraseñas deben coincidir')
    ])
    submit = SubmitField('Registrar Usuario')

    def validate_usuario(self, usuario):
        user = Usuario.get_by_username(usuario.data)
        if user:
            raise ValidationError('El nombre de usuario ya existe.')