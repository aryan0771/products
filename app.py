from flask import Flask, jsonify

app = Flask(__name__)

# Static product array
products = [
    {"id": 1, "name": "Product A", "price": 10.99},
    {"id": 2, "name": "Product B", "price": 15.49},
    {"id": 3, "name": "Product C", "price": 7.99},
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
