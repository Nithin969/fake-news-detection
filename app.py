from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --------------------
# Page routes
# --------------------

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/project")
def project():
    return render_template("project.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")


# --------------------
# Fake News Prediction (TEXT)
# --------------------
@app.route("/predict", methods=["POST"])
def predict():
    news_text = request.form.get("news_text")

    # Dummy logic (can be replaced with ML later)
    if news_text and len(news_text) > 50:
        prediction = "Real News"
    else:
        prediction = "Fake News"

    return jsonify({"prediction": prediction})


# --------------------
# Fake News Prediction (IMAGE)
# --------------------
@app.route("/predict_image", methods=["POST"])
def predict_image():
    file = request.files.get("file")

    if not file:
        return jsonify({"error": "No image uploaded"})

    # Dummy response for image input
    prediction = "Fake News"

    return jsonify({"prediction": prediction})


# --------------------
# Run app
# --------------------
if __name__ == "__main__":
    app.run(debug=True)

    return render_template("project.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)
