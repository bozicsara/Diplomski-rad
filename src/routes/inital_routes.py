from src import app
from flask import render_template

@app.route("/video-call-test")
def video_call_test_view():
    return render_template("index_lib.html")

@app.route("/admin")
def admin_page():
    return render_template("admin.html")

@app.route("/")
@app.route("/home")
def home_view():
    return render_template("home.html")

@app.route("/order")
def order_view():
    return render_template("order.html")

@app.route("/cart")
def cart_view():
    return render_template("cart.html")