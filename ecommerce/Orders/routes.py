from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from ecommerce.Orders.forms import OrderForm
from ecommerce.models import products, address, orders, cart
from ecommerce.rmqsender import Sender
from ecommerce import db
from datetime import datetime
from sqlalchemy import and_
import base64

orders_bp = Blueprint('orders', __name__, template_folder="templates")


@orders_bp.route('/details/<pid>/<qty>', methods=['GET', 'POST'])
@login_required
def details(pid, qty):
    if not current_user.is_authenticated:
        return redirect(url_for('users.login'))

    pics = {}
    address_book_usr = {}
    user_address = []
    manufacturer_details = []

    product_price = 0

    prods = products.query.filter_by(product_id=pid).all()
    addrs = address.query.filter_by(user_id=current_user.user_id).all()
    today = datetime.today().strftime('%Y-%m-%d')

    for addr in addrs:
        user_address.append((addr.address_name, addr.complete_address))
        address_book_usr[addr.address_name] = addr.complete_address

    print(current_user.user_id)

    for prod in prods:
        product_pics = []
        product_price = prod.price
        for pic in prod.pics:
            b64data = base64.b64encode(pic).decode('utf-8')
            product_pics.append(b64data)
        pics[prod.product_id] = [prod.product_name, product_pics, prod.description]
        manufacturer_details.append(prod.manufacturer)
        manufacturer_details.append(prod.manufacturer_address)

    orderForm = OrderForm()
    orderForm.delivery_address.choices = [addr for addr in user_address]

    if orderForm.validate_on_submit():
        s = Sender()
        full_addr = address_book_usr[orderForm.delivery_address.data]
        order = orders(user_id=current_user.user_id, product_id=prod.product_id, purchase_date=today,
                       item_name=prod.product_name, sender_address=manufacturer_details[-1],
                       address_name=orderForm.delivery_address.data, delivery_address=full_addr)
        order.order_price = int(qty) * product_price
        order.quantity=int(qty)
        pics[prod.product_id].append(int(qty))
        pics[prod.product_id].append(order.order_price)

        # msg = dict()
        # msg['product_id'] = pid
        # msg['Quantity'] = qty
        # msg['user_id'] = current_user.user_id
        # msg['address'] = orderForm.delivery_address.data
        msg = str(pid)+'-'+str(qty)+'-'+str(current_user.user_id)+'-'+orderForm.delivery_address.data
        # db.session.add(order)
        # db.session.commit()

        # s.publish('product_update', msg)
        return render_template('summary.html', order_details=pics, address=full_addr)

    return render_template('details.html', pictures=pics, form=orderForm, user_address=user_address,
                           manufacturer=manufacturer_details, qty=qty, price=product_price * int(qty))


@orders_bp.route('/summary')
@login_required
def summary():
    return render_template('summary.html')


@orders_bp.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    user_cart = {}
    address_book_usr = {}
    user_address = []
    manufacturer_details = []
    total_amount = 0

    addrs = address.query.filter_by(user_id=current_user.user_id).all()
    c1 = cart.query.filter_by(user_id=current_user.user_id).all()
    today = datetime.today().strftime('%Y-%m-%d')

    for addr in addrs:
        user_address.append((addr.address_name, addr.complete_address))
        address_book_usr[addr.address_name] = addr.complete_address

    for row in c1:
        prod = products.query.filter_by(product_id=row.product_id).first()
        product_pics = []
        for pic in prod.pics:
            b64data = base64.b64encode(pic).decode('utf-8')
            product_pics.append(b64data)

        total_amount += row.quantity * prod.price
        manufacturer_details.append(prod.manufacturer)
        manufacturer_details.append(prod.manufacturer_address)
        user_cart[row.id] = [row.product_name, product_pics, prod.description, row.quantity, prod.price,
                             manufacturer_details, row.product_id]

    orderForm = OrderForm()
    orderForm.delivery_address.choices = [addr for addr in user_address]
    if orderForm.validate_on_submit():
        full_addr = address_book_usr[orderForm.delivery_address.data]
        for key, val in user_cart.items():
            order = orders(user_id=current_user.user_id, product_id=val[6], purchase_date=today,
                           item_name=val[0], sender_address=val[5][-1],
                           address_name=orderForm.delivery_address.data, delivery_address=full_addr)
            order.order_price = val[3] * val[4]
            order.quantity = val[3]
            product = cart.query.filter(and_(cart.user_id == current_user.user_id, cart.product_name == val[0])).delete()
            db.session.add(order)
            db.session.commit()

        return render_template('summary.html', order_details=user_cart, address=full_addr)

    return render_template('checkout.html', user_cart=user_cart, total_amount=total_amount, form=orderForm)


@orders_bp.route('/history')
@login_required
def history():
    order_history = {}
    user_orders = orders.query.filter_by(user_id=current_user.user_id).order_by(orders.purchase_date.desc()).all()

    for val in user_orders:
        prod = products.query.filter_by(product_id=val.product_id).first()
        product_pics = []
        for pic in prod.pics:
            b64data = base64.b64encode(pic).decode('utf-8')
            product_pics.append(b64data)
        order_history[val.id] = [val.item_name, product_pics, val.quantity, val.id]

    return render_template('history.html', order_history=order_history)


@orders_bp.route('/order_info/<ordid>')
def order_info(ordid):
    order_list = list()
    order = orders.query.filter_by(id=ordid).first()
    prod = products.query.filter_by(product_id=order.product_id).first()
    product_pics = []
    for pic in prod.pics:
        b64data = base64.b64encode(pic).decode('utf-8')
        product_pics.append(b64data)
    order_list.append([order.item_name, product_pics, order.order_price, order.quantity, order.purchase_date.date(), order.delivery_address, prod.manufacturer, prod.manufacturer_address])
    return render_template('order_info.html', val=order_list)