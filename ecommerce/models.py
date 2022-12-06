from ecommerce import db, login_manager, admin
from flask_login import UserMixin
from ecommerce.invadmin import inventoryController, productController


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    print('check user logged in on every page')
    if user_id is not None:
        return users.query.get(user_id)
    return None


class products(db.Model):
    product_id = db.Column(db.String(20), primary_key=True)
    product_name = db.Column(db.String(120), nullable=False)
    manufacturer = db.Column(db.String(120), nullable=False)
    manufacturer_address = db.Column(db.String(220), nullable=False)
    quantity = db.Column(db.Integer)
    pics = db.Column(db.ARRAY(db.LargeBinary))
    description = db.Column(db.String(320))
    product_tag = db.Column(db.String(200))
    price = db.Column(db.Integer)
    purchases = db.relationship('orders', backref='products')


class users(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(16), nullable=False)
    user_mail = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    name = db.Column(db.String(200))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(20))
    contact_number = db.Column(db.Integer)
    addresses = db.relationship('address', backref='users', lazy=True)
    purchases = db.relationship('orders', backref='users')

    def get_id(self):
        print('sending id via user get_id')
        return self.user_id


class address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address_name = db.Column(db.String(400))
    building = db.Column(db.String(400))
    number = db.Column(db.String(400))
    street = db.Column(db.String(400))
    landmark = db.Column(db.String(400))
    code = db.Column(db.String(400))
    city = db.Column(db.String(400))
    district = db.Column(db.String(400))
    state = db.Column(db.String(400))
    country = db.Column(db.String(400))
    complete_address = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))


class orders(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    product_id = db.Column(db.String(20), db.ForeignKey('products.product_id'))
    purchase_date = db.Column(db.DateTime)
    item_name = db.Column(db.String(600))
    order_price = db.Column(db.Integer)  # pending
    sender_address = db.Column(db.String(600))
    address_name = db.Column(db.String(400))
    delivery_address = db.Column(db.String(600))
    delivery_date = db.Column(db.DateTime)  # pending
    payment_details = db.Column(db.String(600))  # pending
    quantity = db.Column(db.Integer)


class cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(20), db.ForeignKey('products.product_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    product_name = db.Column(db.String(120), nullable=False)
    quantity = db.Column(db.Integer)


class inventoryuser(db.Model):
    id = db.Column(db.Integer, auto_increment=True, primary_key=True)
    admin_usr_name = db.Column(db.String(16), nullable=False)
    admin_mail = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    permission = db.Column(db.String(20))
    admin_id = db.Column(db.String(20))

    def get_id(self):
        print('sending a user_id from inventory')
        return self.id

    def is_active(self):
        return True

# admin.add_view(inventoryController(inventoryuser, db.session))
# admin.add_view(productController(products, db.session))
