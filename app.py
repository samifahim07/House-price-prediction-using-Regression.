from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__, template_folder="template")

model = pickle.load(open("model_rf.pkl", "rb"))

# Dataset averages for the 9 features not entered by the user
DEFAULTS = {
    'NOX':      0.5547,
    'RM':       6.2846,
    'AGE':     68.5185,
    'DIS':      3.7950,
    'RAD':      9.5494,
    'TAX':    408.2372,
    'PTRATIO': 18.4555,
    'B':       356.6740,
    'LSTAT':   12.7154,
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    CRIM  = float(request.form.get("CRIM"))
    ZN    = float(request.form.get("ZN"))
    INDUS = float(request.form.get("INDUS"))
    CHAS  = float(request.form.get("CHAS"))

    features = [[
        CRIM, ZN, INDUS, CHAS,
        DEFAULTS['NOX'], DEFAULTS['RM'],  DEFAULTS['AGE'],
        DEFAULTS['DIS'], DEFAULTS['RAD'], DEFAULTS['TAX'],
        DEFAULTS['PTRATIO'], DEFAULTS['B'], DEFAULTS['LSTAT']
    ]]

    predicted_data = round(float(model.predict(features)[0]), 2)

    return render_template("index.html", predicted_data=predicted_data)

if __name__ == "__main__":
    app.run(debug=True)