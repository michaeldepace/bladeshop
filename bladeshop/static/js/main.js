function addToCart(prd_id, prd_qty){
    //send post request to 
    fetch('/cart/add/' + prd_id + '/'+ prd_qty, {method: 'POST'}); //find a way to improve this with jinja later
}

function removeFromCart(crt_id){
    fetch('/cart/remove/' + crt_id, {method: 'POST'});
    // document.location.reload(true);
}