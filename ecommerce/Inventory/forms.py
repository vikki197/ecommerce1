from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, IntegerField, SubmitField, MultipleFileField, EmailField, PasswordField
from wtforms.validators import Length, DataRequired, Email, Regexp, EqualTo


class ProductForm(FlaskForm):
    pid = StringField('product_id', [DataRequired()])
    pname = StringField('product_name', [Length(min=2, max=300), DataRequired()])
    manufacturer = StringField('manufacturer', [Length(min=5, max=300), DataRequired()])
    manufacturer_address = StringField('manufacturer_address', [Length(min=5, max=300), DataRequired()])
    description = StringField('description', [Length(min=5, max=300)])
    quantity = IntegerField('quantity')
    pics = MultipleFileField('images', [FileAllowed(['png', 'jpg'])])
    submit = SubmitField('submit')


class SignupForm(FlaskForm):
    admin_name = StringField('adminname', [DataRequired(), Length(min=3, max=16)])
    mail = EmailField('adminmail', [DataRequired(), Email()])
    password = PasswordField('password', [DataRequired(), Length(min=6, max=16), Regexp("^(?=.*[A-Za-z])(?=.*\\d)(?=.*[$@$!%*#?&])[A-Za-z\\d$@$!%*#?&]{6,16}$")])
    confirm_password = PasswordField('confirmpassword', [DataRequired(), Length(min=6, max=16), EqualTo('password')])
    submit = SubmitField('submit')


class LoginForm(FlaskForm):
    mail = EmailField('adminmail', [DataRequired(), Email()])
    password = PasswordField('password', [DataRequired(), Length(min=6, max=16)])
    submit = SubmitField('submit')