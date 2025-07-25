from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/book-table')
def book_table():
    return render_template('book_table.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/order-online')
def order_online():
    return render_template('order_online.html')

@app.route('/order-now')
def order_now():
    return redirect(url_for('order_online'))

if __name__ == '__main__':
    app.run(debug=True)