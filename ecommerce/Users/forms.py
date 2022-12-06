from flask_wtf import FlaskForm
from wtforms.fields import StringField, EmailField, PasswordField, SubmitField, IntegerField
from wtforms.validators import Length, DataRequired, Email, EqualTo, Regexp


class SignupForm(FlaskForm):
    user_name = StringField('username', [DataRequired(), Length(min=3, max=16)])
    mail = EmailField('usermail', [DataRequired(), Email()])
    password = PasswordField('password', [DataRequired(), Length(min=6, max=16), Regexp("^(?=.*[A-Za-z])(?=.*\\d)(?=.*[$@$!%*#?&])[A-Za-z\\d$@$!%*#?&]{6,16}$")])
    confirm_password = PasswordField('confirmpassword', [DataRequired(), Length(min=6, max=16), EqualTo('password')])
    submit = SubmitField('submit')


class LoginForm(FlaskForm):
    mail = EmailField('usermail', [DataRequired(), Email()])
    password = PasswordField('password', [DataRequired(), Length(min=6, max=16)])
    submit = SubmitField('submit')


class ProfileForm(FlaskForm):
    name = StringField('name', [Length(min=3, max=16)])
    age = IntegerField('age')
    gender = StringField('gender', [Length(min=4, max=20)])
    mail = EmailField('usermail', [Email()])
    submit = SubmitField('submit')


class AddressForm(FlaskForm):
    name = StringField('name')
    building = StringField('building')
    number = StringField('number')
    street = StringField('street')
    landmark = StringField('landmark')
    code = StringField('code')
    city = StringField('city')
    district = StringField('district')
    state = StringField('state')
    country = StringField('country')
    submit = SubmitField('submit')