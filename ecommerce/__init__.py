from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_admin import Admin
from .config import Config
from ecommerce.invadmin import MyAdminView

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
migrate = Migrate(compare_type=True)
admin = Admin()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app, index_view=MyAdminView())

    with app.app_context():
        from .General import routes
        app.register_blueprint(routes.general_bp)

        from .Inventory import routes
        app.register_blueprint(routes.inventory_bp)

        from .Products import routes
        app.register_blueprint(routes.products_bp)

        from .Users import routes
        app.register_blueprint(routes.users_bp)

        from .Orders import routes
        app.register_blueprint(routes.orders_bp)

        from .Cart import routes
        app.register_blueprint(routes.cart_bp)


    return app
