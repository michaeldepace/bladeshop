function addToCart(prd_id, prd_qty){
    //send post request to 
    fetch('/cart/add/' + prd_id + '/'+ prd_qty, {method: 'POST'}); //find a way to improve this with jinja later
}