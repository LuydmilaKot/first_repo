from flask import Flask, render_template, request, make_response, redirect
from db20.Orders import get_orders, create_orders, delete_orders

app = Flask(__name__)


@app.route("/", methods=["GET"])
def tabl():
    list_orders = get_orders()
    return render_template("index.html", orders=list_orders)


@app.route("/order", methods=["GET", "POST"])
def new_order():
    if request.method == "POST":
        name = request.form.get("name")
        cost = request.form.get("cost")
        client_id = request.form.get("client_id")
        if not name or not cost or not client_id:
            return make_response("Name, cost, and client ID required", 400)
        create_orders(name, cost, client_id)
        return make_response("Order added", 201)

    orders = get_orders()
    return render_template("orders.html", orders=orders)


@app.route("/order/<client_id>", methods=["DELETE"])
def delete_order(client_id):
    delete_orders(client_id)
    return make_response("Deleted", 201)


if __name__ == "__main__":
    app.run()