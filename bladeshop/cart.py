from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort
from bladeshop.auth import login_required
from bladeshop.db import get_db

bp = Blueprint('cart', __name__)

#whenever the user clicks add to cart, it sends a post request to this function to handle the record creation
@bp.route('/cart/add/<int:prd_id>/<int:prd_qty>', methods=['POST'])
@login_required
def addToCart(prd_id, prd_qty):
    db = get_db()
    db.execute('INSERT INTO cart (usr_id, prd_id, prd_amount) VALUES ('+g.user['id']+', '+prd_id+','+prd_qty+');')
    db.commit()
    return