from flask import Flask, render_template

app = Flask(__name__)

@app.route("/endpoint")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cupcakes")
def all_cupcakes():
    return render_template("individual-cupcake.html")

@app.route("/order")
def order():
    return render_template("order.html")

if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 5000, host = "localhost")
    