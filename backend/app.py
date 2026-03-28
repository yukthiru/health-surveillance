from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

import os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv(os.path.join(BASE, "data", "disease_data.csv"))

def get_risk(cases, avg):
    if cases >= avg * 1.8:
        return "Critical"
    elif cases >= avg * 1.4:
        return "High"
    elif cases >= avg * 1.1:
        return "Medium"
    else:
        return "Low"

@app.route("/api/districts")
def get_districts():
    results = []
    for district in df["district"].unique():
        for disease in df["disease"].unique():
            subset = df[(df["district"] == district) &
                       (df["disease"] == disease)]
            avg = subset["cases"].mean()
            latest = subset.iloc[-1]["cases"]
            risk = get_risk(latest, avg)
            results.append({
                "district": district,
                "disease": disease,
                "latest_cases": int(latest),
                "average_cases": round(float(avg), 1),
                "risk": risk
            })
    return jsonify(results)

@app.route("/api/district/<name>")
def get_district(name):
    subset = df[df["district"] == name]
    data = subset.to_dict(orient="records")
    return jsonify(data)

@app.route("/")
def home():
    return jsonify({"message": "Health Surveillance API is running!"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
