from flask import Blueprint, render_template, url_for, redirect, request,session
from flask_login import login_user, current_user, login_required, logout_user
from ecommerce.Users.forms import SignupForm, LoginForm, ProfileForm, AddressForm
from ecommerce.models import users, address
from ecommerce import db, bcrypt, login_manager

users_bp = Blueprint('user', __name__, template_folder="templates")


@users_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    sform = SignupForm()
    users_count = len(users.query.all())
    if sform.validate_on_submit():
        existing_usr = users.query.filter_by(user_mail=sform.mail.data).first()
        if existing_usr is None:
            u1 = users(user_id=users_count + 1, user_name=sform.user_name.data, user_mail=sform.mail.data,
                       password=bcrypt.generate_password_hash(sform.password.data).decode('utf-8'))
            u1.name = None
            u1.age = 0
            u1.gender = None
            db.session.add(u1)
            db.session.commit()
            login_user(u1)
            return redirect(url_for('general.home'))
        else:
            pass
    return render_template('signup.html', supform=sform)


@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    print(current_user, session)
    if current_user.is_authenticated:
        return redirect(url_for('general.home'))
    lform = LoginForm()
    if lform.validate_on_submit():
        u1 = users.query.filter_by(user_mail=lform.mail.data).first()
        if u1 is not None and bcrypt.check_password_hash(u1.password, lform.password.data):
            print('logging you in')
            login_user(u1)
            print('logged in')
            nxt = request.args.get('next')
            # print(nxt)
            if nxt:
                nxt = nxt[1:]
                return redirect(url_for(nxt))
            return redirect(url_for('general.home'))
        else:
            return redirect(url_for('user.login'))

    return render_template('login.html', linform=lform)


@users_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    print('profile page', current_user.user_mail)
    current_values = [current_user.user_mail, current_user.name, current_user.age, current_user.gender]
    pform = ProfileForm()
    if pform.validate_on_submit():
        if pform.mail.data is not None and pform.mail.data != current_user.user_mail:
            usr = users.query.filter_by(user_mail=pform.mail.data)
            if usr is None:
                print('data changed')
                current_user.user_mail = pform.mail.data
            else:
                print('mail already exists in db try another mail id')

        if pform.name.data is not None and pform.name.data != current_user.name:
            print('data changed name')
            current_user.name = pform.name.data

        if pform.age.data is not None and pform.age.data != current_user.age:
            print('data changed age')
            current_user.age = pform.age.data

        if pform.gender.data is not None and pform.gender.data != current_user.gender:
            print('data changed ')
            current_user.gender = pform.gender.data

        db.session.commit()

    return render_template('profile.html', form=pform, current_values=current_values)


@users_bp.route('/addresses', methods=['GET', 'POST'])
@login_required
def addresses():
    aform = AddressForm()
    address_count = len(address.query.all())
    complete_address = ''
    if aform.validate_on_submit():
        a1 = address(id=address_count + 1, address_name=aform.name.data, building=aform.building.data,
                     number=aform.number.data,
                     street=aform.street.data, landmark=aform.landmark.data, code=aform.code.data,
                     city=aform.city.data, district=aform.district.data, state=aform.state.data,
                     country=aform.country.data)

        for name, val in aform.data.items():
            if val is not '' and name != 'submit' and name != 'csrf_token' and val is not None:
                val += ' '
                complete_address += val

        # a1.complete_address = a1.building+' '+a1.number+' '+a1.street+' '+a1.landmark+' '+a1.code+' '+a1.city+' '+a1.state+' '+a1.country
        a1.complete_address = complete_address
        a1.user_id = current_user.user_id
        db.session.add(a1)
        db.session.commit()
    return render_template('addresses.html', form=aform)


@users_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.login'))


@login_manager.unauthorized_handler  # In unauthorized_handler we have a callback URL
def unauthorized_callback():  # In call back url we can specify where we want to
    return redirect(url_for('user.login'))
