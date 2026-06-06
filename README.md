# 💖 PinkGuard AI – Fraud Detection System

## 📌 Overview
PinkGuard AI is an end-to-end machine learning system designed to detect fraudulent credit card transactions in real time.

This project combines:
- Machine Learning (Fraud Detection Model)
- Backend API (Flask)
- Interactive Dashboard (Streamlit)

---

## 🎯 Features
- Detect fraudulent transactions instantly
- High recall model (optimized to catch fraud)
- REST API for real-time predictions
- Interactive UI dashboard
- Sample transaction testing

---

## 🧠 Machine Learning
- Model: Logistic Regression
- Dataset: Credit Card Fraud Detection Dataset
- Techniques used:
  - Data scaling (StandardScaler)
  - Class imbalance handling (class weights)
  - Stratified train-test split

---

## 🏗️ Project Structure

fraud-detection-project/
│
├── app.py
├── streamlit_app.py
├── fraud_model.pkl
├── requirements.txt
└── README.md

---

## 🚀 How to Run Locally

### 1. Clone the repo
```bash
git clone <your-repo-link>
cd fraud-detection-project

2. Install dependencies
pip install -r requirements.txt
3. Run the API
python app.py
4. Run the UI
streamlit run streamlit_app.py


🌐 API Endpoint

POST /predict

Example request:

{
  "features": [0.0, -1.2, ..., 50.0]
}


📊 Results
Fraud Recall: ~88%
Precision: ~51%
Focus: Maximize fraud detection


💼 Why This Project Matters

This project demonstrates:

End-to-end ML system design
API development
Frontend integration
Real-world problem solving

💡 Future Improvements
Deploy to cloud (Render)
Add authentication
Improve model with XGBoost

✨ Author

Siham Ali