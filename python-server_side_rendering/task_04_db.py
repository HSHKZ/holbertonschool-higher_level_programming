from flask import Flask, render_template, request, jsonify
import json
import os
import csv
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, 'items.json')
    with open(file_path) as f:
        data = json.load(f)
    items_list = data.get('items', [])
    return render_template('items.html', items=items_list)

def read_json(file_name):
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, file_name)
    with open(file_path, 'r') as f:
        return json.load(f)

def read_csv(file_name):
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, file_name)
    products = []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []
    print(product_id)

    if source == 'json':
        try:
            products = read_json('products.json')
            print(products)
        except FileNotFoundError:
            return render_template('product_display.html', error='File not found')
    elif source == 'csv':
        try:
            products = read_csv('products.csv')
            print(products)
        except FileNotFoundError:
            return render_template('product_display.html', error='File not found')
    elif source in ['db', 'sql']:
        try:
            conn = sqlite3.connect('products.db')
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            print(cursor)
            if product_id:
                cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
            else:
                cursor.execute('SELECT * FROM Products')
            products = cursor.fetchall()
            conn.close()
            products = [dict(product) for product in products]
        except sqlite3.Error:
            return render_template('product_display.html', error='Database error')
    else:
        return render_template('product_display.html', error='Wrong source')

    if product_id:
        products = [product for product in products if product['id'] == product_id]

    if not products:
        return render_template('product_display.html', error='Product not found')

    return render_template('product_display.html', products=products)

def create_database():
    base_dir = os.path.dirname(__file__)
    db_path = os.path.join(base_dir, 'products.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT OR IGNORE INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=5000)
