from flask import Blueprint, render_template, url_for, redirect, request, session
from .forms import ProductSearch
from flask_login import current_user

general_bp = Blueprint('general', __name__, template_folder="templates")


@general_bp.route('/home', methods=['GET', 'POST'])
def home():
    # print(request.args)
    # print(session.get('_id'))
    # print(session.get('_user_id'))
    print('loading home', session)
    if hasattr(current_user, 'permission'):
        print('cannot access inventory this page need admin access')
        return redirect(url_for('inventory.inventorylogin'))
    psform = ProductSearch()
    if psform.validate_on_submit():
        return redirect(url_for('products.viewproducts', name=psform.search.data))
    return render_template('home.html', form=psform)
