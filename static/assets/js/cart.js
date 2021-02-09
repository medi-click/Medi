var updateBtns = document.getElementsByClassName('update-cart')
var wishlistBtns = document.getElementsByClassName('wishlist-cart')


for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {

        var productId = this.dataset.product;
        var action = this.dataset.action;

        console.log('productId:', productId, 'Action: ', action);

        console.log('User:', user);

        if (user == 'AnonymousUser') {
            console.log('not login..');
        } else {
            updateUserOrder(productId, action)

        }
    })
}

function updateUserOrder(productId, action) {
    console.log('User is authenticated,sending data.....');

    var url = '/update_item/'

    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({ 'productId': productId, 'action': action })

        })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log(data)
            location.reload()
        });
}


for (j = 0; j < wishlistBtns.length; j++) {
    wishlistBtns[j].addEventListener('click', function() {

        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('productId:', productId, 'Action: ', action);

        console.log('User:', user);

        if (user == 'AnonymousUser') {
            console.log('not login..');
        } else {
            wishlistUserOrder(productId, action)

        }
    })
}

function wishlistUserOrder(productId, action) {
    console.log('User is authenticated,sending data.....');

    var url = '/wish_item/'

    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({ 'productId': productId, 'action': action })

        })
        .then((response) => {
            //console.log(response)
            return response.json();

        })
        .then((data) => {
            console.log(data)
            location.reload()
        });
}