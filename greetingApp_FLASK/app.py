from flask import Flask, render_template, request, flash
import pred as p

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"


@app.route("/")
def index():
    flash("Enter product name")
    return render_template("index.html")


@app.route("/greet", methods=['POST', 'GET'])
def greeter():
    product_name = str(request.form['name_input'])
    flash("Results for" + product_name)
    data = p.x()
    amazon_link = data[0]
    flipkart_link = data[1]
    amazon_price = data[2]
    flipkart_price = data[3]
    return render_template("index.html", a=amazon_link, b=amazon_price, c=flipkart_link, d=flipkart_price)


if __name__ == "__main__":
    app.run()
