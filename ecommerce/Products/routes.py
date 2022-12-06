from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user
from ecommerce.Products.forms import buyForm
from ecommerce.models import products, cart
from ecommerce import db
from sqlalchemy import or_
import base64

products_bp = Blueprint('products', __name__, template_folder="templates")


@products_bp.route('/viewproducts/<name>')
def viewproducts(name):
    pics = {}
    prods = products.query.filter(
        or_(products.product_name.contains(name), products.product_name.contains(name.capitalize())))

    for prod in prods:
        product_pics = []
        for pic in prod.pics:
            b64data = base64.b64encode(pic).decode('utf-8')
            product_pics.append(b64data)
        pics[prod.product_id] = [prod.product_name, product_pics, prod.description, prod.product_id]

    return render_template('viewproducts.html', pictures=pics, name=name)


@products_bp.route('/product/<pid>', methods=['GET', 'POST'])
def product(pid):
    pics = {}
    prods = products.query.filter_by(product_id=pid).all()
    display_msg = ''
    bform = buyForm()
    stock = 0

    for prod in prods:
        product_pics = []
        for pic in prod.pics:
            b64data = base64.b64encode(pic).decode('utf-8')
            product_pics.append(b64data)
        pics[prod.product_id] = [prod.product_name, product_pics, prod.description]
        stock = prod.quantity

    if request.method == 'GET':
        qty = bform.qty.data
        if qty <= stock:
            display_msg = 'In Stock'
        else:
            display_msg = 'Out of Stock'



    if bform.validate_on_submit():
        qty = bform.qty.data
        if bform.cart.data:
            c1 = cart(product_id=pid, user_id=current_user.user_id, product_name=pics[pid][0], quantity=qty)
            db.session.add(c1)
            db.session.commit()
            return redirect(url_for('cart.viewcart'))
        if bform.buy.data:
            if qty < stock:
                return redirect(url_for('orders.details', pid=pid, qty=qty))
            else:
                return render_template('product.html', pictures=pics, form=bform, available='Out of Stock')


    return render_template('product.html', pictures=pics, form=bform, available=display_msg)
