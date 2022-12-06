from flask import request, redirect, url_for, session
from flask_login import current_user
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView


class MyAdminView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('inventory.inventorylogin', next=request.url))


class inventoryController(ModelView):
    def is_accessible(self):
        print(request.args.get('session'))
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('user.login', next=request.url))


class productController(ModelView):
    def is_accessible(self):
        print(request.args.get('session'))
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('user.login', next=request.url))