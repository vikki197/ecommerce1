from flask import Blueprint, render_template, redirect, url_for, request
from ecommerce.models import cart, products
from flask_login import current_user, login_required
from ecommerce.Cart.forms import removeForm
from ecommerce import db
import base64

cart_bp = Blueprint('cart', __name__, template_folder="templates")


@cart_bp.route('/viewcart', methods=['GET', 'POST'])
@login_required
def viewcart():
    rform = removeForm()
    user_cart = {}
    c1 = cart.query.filter_by(user_id=current_user.user_id).all()
    print(type(c1))
    for row in c1:
        print(row, type(row))
        prod = products.query.filter_by(product_id=row.product_id).first()
        product_pics = []
        for pic in prod.pics:
            b64data = base64.b64encode(pic).decode('utf-8')
            product_pics.append(b64data)
        user_cart[row.id] = [row.product_name, product_pics, row.quantity]

    if rform.validate_on_submit():
        if rform.remove.data:
            product_desc = request.form.get('remove')
            product = cart.query.filter_by(product_name=product_desc).delete()
            db.session.commit()
            return redirect(url_for('cart.viewcart'))

        if rform.buyall.data:
            return redirect(url_for('orders.checkout'))
        return redirect(url_for('general.home'))


    return render_template('viewcart.html', cart=user_cart, form=rform)


@cart_bp.route('/addtocart')
def addtocart():
    return render_template('addtocart.html')
