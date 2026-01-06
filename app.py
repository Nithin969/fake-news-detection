from flask import Flask, render_template, request, jsonify
Create data folder


app = Flask(__name__)
# Load ML model and vectorizer
model = pickle.load(open("model/fake_news_model.pkl", "rb"))
vectorizer = pickle.load(open("model/tfidf_vectorizer.pkl", "rb"))


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
@app.route("/predict", methods=["POST"])
def predict():
    news_text = request.form.get("news_text")

    if not news_text:
        return jsonify({"error": "No text provided"})

    # Vectorize input text
    transformed_text = vectorizer.transform([news_text])

    # Predict
    prediction = model.predict(transformed_text)[0]

    result = "Real News" if prediction == 1 else "Fake News"

    return jsonify({"prediction": result})



# --------------------
# Run app
# --------------------
if __name__ == "__main__":
    app.run(debug=True)

    return render_template("project.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)
