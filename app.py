from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

# Load ML model
# MODEL_PATH = os.path.join("ml", "model.pkl")
# with open(MODEL_PATH, "rb") as f:
#     model = pickle.load(f)

# with open(MODEL_PATH, "rb") as f:
#     model = pickle.load(f)
import pickle
import os

MODEL_PATH = "ml/model.pkl"

if not os.path.exists(MODEL_PATH) or os.path.getsize(MODEL_PATH) == 0:
    raise RuntimeError("❌ model.pkl is missing or empty. Run train_model.py first.")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return "Final Capstone Flask App is running"

@app.route("/health")
def health():
    return jsonify({"status": "OK"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    if not data or "features" not in data:
        return jsonify({"error": "Invalid input"}), 400

    features = data["features"]
    prediction = model.predict([features])

    return jsonify({"prediction": prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)
