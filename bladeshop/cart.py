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
    count = db.execute('SELECT COUNT(*) FROM cart WHERE usr_id='+str(g.user['usr_id'])+' AND prd_id='+str(prd_id)+'').fetchall()[0][0]
    if count > 0:
        db.execute('UPDATE cart SET prd_amount = prd_amount + '+str(prd_qty)+' WHERE usr_id='+str(g.user['usr_id'])+' AND prd_id='+str(prd_id)+'')    
    else:
        db.execute('INSERT INTO cart (usr_id, prd_id, prd_amount) VALUES ('+str(g.user['usr_id'])+', '+str(prd_id)+','+str(prd_qty)+');')    
    db.commit()
    return "Success", 200

@bp.route('/cart/remove/<int:crt_id>', methods=['POST'])
@login_required
def removeFromCart(crt_id):
    db=get_db()
    db.execute('DELETE FROM cart WHERE crt_id=' + str(crt_id))
    db.commit()
    return render_template('cart/cart.html')

@bp.route('/cart/itemqty/<int:prd_id>/<int:prd_qty>', methods=['POST'])
@login_required
def setCartQuantity(prd_id, prd_qty):
    db = get_db()
    db.execute('UPDATE cart SET prd_amount = '+str(prd_qty)+' WHERE usr_id='+str(g.user['usr_id'])+' AND prd_id='+str(prd_id)+'')
    db.commit()
    return "Success", 200

@bp.route('/cart')
@login_required
def cart():
    db = get_db()
    cart_total = db.execute('select SUM(c.prd_amount * p.prd_price) FROM CART c JOIN PRODUCT p on c.prd_id=p.prd_id WHERE c.usr_id = 1').fetchone()[0]
    cart_items = db.execute('SELECT * FROM cart c JOIN product p on c.prd_id = p.prd_id WHERE c.usr_id='+str(g.user['usr_id'])+'').fetchall()
    return render_template('cart/cart.html', items=cart_items, cartTotal=cart_total)
    