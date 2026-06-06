from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

port = int(os.environ.get("PORT", 5000))
#app.run(host='0.0.0.0', port=port)

app = Flask(__name__)

# ====================== LOAD MODEL ======================
# Since app.py and fraud_model.pkl are now both in the root folder
try:
    model = joblib.load('fraud_model.pkl')
    print("✅ Model loaded successfully!")
except FileNotFoundError:
    print("❌ Error: 'fraud_model.pkl' not found in the current folder!")
    print("Make sure you have run train_model.py first.")
    model = None

@app.route('/')
def home():
    return jsonify({
        "message": "Fraud Detection API is running 🚀",
        "status": "active"
    })

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded. Please train the model first."}), 500

    try:
        data = request.get_json()
        
        if not data or 'features' not in data:
            return jsonify({"error": "Please provide 'features' in the request body"}), 400
        
        features = data.get('features')
        
        # Convert to 2D array (1 sample, 30 features)
        features_array = np.array(features).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(features_array)[0]
        probability = model.predict_proba(features_array)[0][1]

        return jsonify({
            "prediction": int(prediction),           # 0 = Normal, 1 = Fraud
            "fraud_probability": round(float(probability), 4),
            "message": "Fraud" if prediction == 1 else "Normal"
        })

    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500


if __name__ == '__main__':
    print("Starting Fraud Detection API...")
    app.run(debug=True, host='0.0.0.0', port=5000)




