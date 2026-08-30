from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class FacturaForm(FlaskForm):
    cliente = StringField('Cliente', validators=[
        DataRequired(message="El cliente es obligatorio.")
    ])
    monto_total = DecimalField('Monto Total', validators=[
        DataRequired(message="El monto total es obligatorio."),
        NumberRange(min=0.01, message="El monto debe ser mayor a 0.")
    ])
    submit = SubmitField('Generar Factura')