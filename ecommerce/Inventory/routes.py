from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from .forms import ProductForm, SignupForm, LoginForm
from ecommerce import db, bcrypt
from ecommerce.models import products, inventoryuser
import base64

inventory_bp = Blueprint('inventory', __name__, template_folder="templates")

""" 
@inventory_bp.route('/inventorysignup', methods=['GET', 'POST'])
def inventorysignup():
    sform = SignupForm()
    if sform.validate_on_submit():
        existing_usr = inventoryuser.query.filter_by(admin_mail=sform.mail.data).first()
        if existing_usr is None:
            u1 = inventoryuser(admin_usr_name=sform.admin_name.data, admin_mail=sform.mail.data,
                               password=bcrypt.generate_password_hash(sform.password.data).decode('utf-8'))
            u1.name = None
            u1.age = 0
            u1.gender = None
            db.session.add(u1)
            db.session.commit()
            login_user(u1)
            return redirect(url_for('inventory.inventory'))
        else:
            pass
    return render_template('inventorysignup.html', supform=sform)


@inventory_bp.route('/inventorylogin', methods=['GET', 'POST'])
def inventorylogin():
    lform = LoginForm()
    if lform.validate_on_submit():
        u1 = inventoryuser.query.filter_by(admin_mail=lform.mail.data).first()
        print(u1.admin_usr_name)
        if u1 is not None and bcrypt.check_password_hash(u1.password, lform.password.data):
            if u1.permission == 'admin':
                print('admin logged in')
                login_user(u1)
                return redirect(url_for('admin.index'))
            else:
                return redirect(url_for('inventory.inventorylogin'))
        else:
            return redirect(url_for('inventory.inventorylogin'))

    return render_template('inventorylogin.html', linform=lform)


@inventory_bp.route('/inventorylogout')
@login_required
def inventorylogout():
    logout_user()
    return redirect(url_for('inventory.inventorylogin'))


@inventory_bp.route('/inventory')
def inventory():
    # query(Model).filter(something).limit(5).all()
    print(current_user.__dict__)
    if not hasattr(current_user, 'permission'):
        print('cannot access inventory this page need admin access')
        return redirect(url_for('inventory.inventorylogin'))
    productList = products.query.limit(5).all()
    pics = {}
    for prods in productList:
        inventory_pics = []
        for prod in prods.pics:
            b64data = base64.b64encode(prod).decode('utf-8')
            inventory_pics.append(b64data)
        pics[prods.product_id] = [prods.product_name, inventory_pics, prods.description]

    return render_template('inventory.html', pictures=pics)


@inventory_bp.route('/addproducts', methods=['GET', 'POST'])
def add_products():
    if not hasattr(current_user, 'permission'):
        print('cannot access add products this page need admin access')
        return redirect(url_for('inventory.inventorylogin'))
    pform = ProductForm()
    if pform.validate_on_submit():
        product_pics = []
        pics = request.files.getlist(pform.pics.name)
        for picture_upload in pics:
            # product_pics.append(secure_filename(picture_upload.filename))
            product_pics.append(picture_upload.stream.read())
        p1 = products(product_id=pform.pid.data, product_name=pform.pname.data,
                      manufacturer=pform.manufacturer.data, manufacturer_address=pform.manufacturer_address.data,
                      pics=product_pics, description=pform.description.data, quantity=pform.quantity.data)

        db.session.add(p1)
        db.session.commit()
        return render_template('addproducts.html', form=pform)

    return render_template('addproducts.html', form=pform)"""
