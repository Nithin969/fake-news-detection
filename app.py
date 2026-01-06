from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route("/")
def index():
    return render_template("index.html")

# About page
@app.route("/about")
def about():
    return render_template("about.html")

# Project page
@app.route("/project")
def project():
    return render_template("project.html")

# Contact page
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Login page
@app.route("/login")
def login():
    return render_template("login.html")

# Thank you page
@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

@app.route("/predict", methods=["POST"])
def predict():
    news_text = request.form.get("news")

    # Dummy prediction logic (for now)
    if news_text and len(news_text) > 50:
        result = "Real News"
    else:
        result = "Fake News"

    return render_template("project.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)
