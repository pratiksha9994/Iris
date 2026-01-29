from flask import Flask, render_template, request
import pickle
import numpy as np

# Load model and encoder
with open("iris_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    le = pickle.load(f)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction_text = None

    if request.method == "POST":
        sepal_length = float(request.form["sepal_length"])
        sepal_width = float(request.form["sepal_width"])
        petal_length = float(request.form["petal_length"])
        petal_width = float(request.form["petal_width"])

        new_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        prediction = model.predict(new_data)
        species = le.inverse_transform(prediction)

        prediction_text = f"Predicted Species: {species[0]}"

    return render_template("index.html", prediction=prediction_text)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
