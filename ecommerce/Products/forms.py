from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, IntegerField
from wtforms.validators import DataRequired


class buyForm(FlaskForm):
    qty = IntegerField('qty', [DataRequired()], default=1)
    cart = SubmitField('cart')
    buy = SubmitField('buy')
