from flask import Flask, render_template
from cupcakes import get_cupcakes
app = Flask(__name__)

@app.route("/endpoint")

@app.route("/")
def home():
    cupcakes = get_cupcakes("sample.csv")
    order = get_cupcakes("orders.csv")
    order_total = round(sum([float(x["price"]) for x in order]), 2)
    return render_template("index.html", cupcakes=cupcakes, items_num=len(order), order_total=order_total)

@app.route("/cupcakes")
def all_cupcakes():
    return render_template("individual-cupcake.html")

@app.route("/order")
def order():
    return render_template("order.html")

if __name__ == "__main__":
    app.debug = True
    app.run(debug = True, port = 8080, host = "localhost")
    