from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, SelectField


class OrderForm(FlaskForm):
    delivery_address = SelectField('addrs')
    buy = SubmitField('Submit')

