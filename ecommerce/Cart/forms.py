from flask_wtf import FlaskForm
from wtforms.fields import SubmitField


class removeForm(FlaskForm):
    remove = SubmitField('remove')
    buyall = SubmitField('buyall')
