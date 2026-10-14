from flask import Flask, render_template, request
from numpy.ma.core import product

import dao

app = Flask(__name__)


@app.route("/")
def index():
    q = request.args.get("q", "").strip()

    cates = dao.load_categories()
    prods = dao.load_products(q)

    return render_template(
        "index.html",
        cates=cates,
        prods=prods,
        q=q
    )

@app.route("/products/<int:id>")
def detaild(id):
    return render_template("product_detail.html", product=product)

if __name__ == "__main__":
    app.run(debug=True)