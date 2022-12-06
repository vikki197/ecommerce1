from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Length, DataRequired


class ProductSearch(FlaskForm):
    search = StringField('search', [DataRequired(), Length(min=2, max=200)], render_kw={"placeholder": "Search for a product"})
    submit = SubmitField('submit')
