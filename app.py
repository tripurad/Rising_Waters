from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open("flood_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = [
            float(request.form["Temp"]),
            float(request.form["Humidity"]),
            float(request.form["Cloud_Cover"]),
            float(request.form["ANNUAL"]),
            float(request.form["Jan_Feb"]),
            float(request.form["Mar_May"]),
            float(request.form["Jun_Sep"]),
            float(request.form["Oct_Dec"]),
            float(request.form["avgjune"]),
            float(request.form["sub"])
        ]

        prediction = model.predict([features])[0]

        if prediction == 1:
            return render_template("chance.html")
        else:
            return render_template("no_chance.html")

    except Exception as e:
        return render_template("index.html", prediction=str(e))

if __name__ == "__main__":
    app.run(debug=True)