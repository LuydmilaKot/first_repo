from flask import Flask, render_template
from db.orders_DZ16 import get_orders

app = Flask(__name__)


@app.route('/', methods=['GET'])
def template():
    spisok_orders = get_orders()
    return render_template('index.html', orders=spisok_orders)


if __name__ == '__main__':
    app.run()
