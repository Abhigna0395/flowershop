from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret123'  

products = [
    {'id': 1, 'name': 'Red Rose Bouquet', 'price': 1000, 'image': 'redrosebouquet.webp'},
    {'id': 2, 'name': 'Sunflower Bouquet', 'price': 2000, 'image': 'sunflowerbouquet.webp'},
    {'id': 3, 'name': 'Lone Rose', 'price': 100, 'image': 'lonerose.webp'},
    {'id': 4, 'name': 'Tulip Bunch', 'price': 1200, 'image': 'tulipbunch.webp'},
    {'id': 5, 'name': 'Orchid Basket', 'price': 2500, 'image': 'orchidbasket.webp'},
    {'id': 6, 'name': 'Mixed Flower Bouquet', 'price': 1800, 'image': 'mixedflowerbouquet.webp'},
    {'id': 7, 'name': 'Lily Arrangement', 'price': 2200, 'image': 'lilyarrangement.jpg'},
    {'id': 8, 'name': 'Daisy Charm Pack', 'price': 900, 'image': 'daisycharmpack.jpg'},
    {'id': 9, 'name': 'mixed rose bouquet', 'price': 600, 'image': 'mixedrosebouquet.jpeg'},
    {'id': 10, 'name': 'Jasmine Bouquet', 'price': 850, 'image': 'jasminebouquet.jpeg'},
    {'id': 11, 'name': 'Carnation Box', 'price': 1500, 'image': 'carnationbox.jpg'},
    {'id': 12, 'name': 'Exotic Bloom Combo', 'price': 3000, 'image': 'exoticflowerbloom.jpg'}
]

TAX_RATE = 0.18  

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(product_id)
    session.modified = True
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    cart_items = []
    total = 0
    if 'cart' in session:
        for pid in session['cart']:
            for product in products:
                if product['id'] == pid:
                    cart_items.append(product)
                    total += product['price']
    return render_template('cart.html', cart=cart_items, total=total)

@app.route('/checkout')
def checkout():
    cart_items = []
    total = 0
    if 'cart' in session:
        for pid in session['cart']:
            for product in products:
                if product['id'] == pid:
                    cart_items.append(product)
                    total += product['price']
        session.pop('cart', None)  

    tax = round(total * TAX_RATE, 2)
    grand_total = round(total + tax, 2)
    return render_template(
        'checkout.html',
        cart=cart_items,
        total=total,
        tax=tax,
        grand_total=grand_total
    )

if __name__ == '__main__':
    app.run(debug=True, port=5500)
