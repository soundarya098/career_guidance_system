from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib

# Initialize app
app = Flask(__name__)
CORS(app)  # Enables communication between React (port 3000) and Flask (port 5000)

# Load trained model and label encoder
model = joblib.load("career_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

@app.route("/")
def home():
    return jsonify({"message": "AI Career Guidance Backend Running 🚀"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        age = int(data.get("age", 21))
        math = int(data.get("math", 3))
        programming = int(data.get("programming", 3))
        creativity = int(data.get("creativity", 3))
        communication = int(data.get("communication", 3))
        logic = int(data.get("logic", 3))
        preferred_subject = data.get("preferred_subject", "Computer Science")

        # Encode the subject
        if preferred_subject in label_encoder.classes_:
            subject_encoded = label_encoder.transform([preferred_subject])[0]
        else:
            subject_encoded = 0

        # Create DataFrame for model
        input_data = pd.DataFrame([[age, math, programming, creativity, communication, logic, subject_encoded]],
                                  columns=["age", "math", "programming", "creativity", "communication", "logic", "preferred_subject"])

        # Predict
        prediction = model.predict(input_data)
        predicted_career = label_encoder.inverse_transform(prediction)[0]

        return jsonify({"prediction": predicted_career})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
