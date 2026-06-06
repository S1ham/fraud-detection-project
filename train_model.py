import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import joblib
import seaborn as sns
import matplotlib.pyplot as plt

# ====================== LOAD DATA ======================
print("Loading dataset...")
data = pd.read_csv('data/creditcard.csv')

# Features and target
X = data.drop('Class', axis=1)
y = data['Class']

# ====================== TRAIN-TEST SPLIT ======================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2, 
    random_state=42,
    stratify=y          # Important for imbalanced fraud data
)

print(f"Training samples: {X_train.shape[0]:,}")
print(f"Testing samples: {X_test.shape[0]:,}")
print(f"Fraud cases in test set: {y_test.sum()}\n")

# ====================== TRAIN MODEL ======================
print("Training the model...")

model = make_pipeline(
    StandardScaler(),
    LogisticRegression(
        max_iter=2000,
        solver='lbfgs',
        class_weight={0: 1.0, 1: 35},   # Best balance we found
        random_state=42
    )
)

model.fit(X_train, y_train)

# ====================== PREDICTIONS & EVALUATION ======================
y_pred = model.predict(X_test)

print("="*60)
print("CLASSIFICATION REPORT")
print("="*60)
print(classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("\nCONFUSION MATRIX")
print(cm)

print("\nInterpretation:")
print(f"True Negatives (Correct Normal) : {cm[0,0]}")
print(f"False Positives (Wrongly flagged as Fraud): {cm[0,1]}")
print(f"False Negatives (Missed Fraud)    : {cm[1,0]}")
print(f"True Positives (Correctly caught Fraud): {cm[1,1]}")

# Plot Confusion Matrix (Nice visual)
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Normal', 'Fraud'],
            yticklabels=['Normal', 'Fraud'])
plt.xlabel('Predicted Label')
plt.ylabel('Actual Label')
plt.title('Confusion Matrix - Fraud Detection Model')
plt.show()

# ====================== SAVE MODEL ======================
joblib.dump(model, 'fraud_model.pkl')
print("\n✅ Model trained and saved successfully as 'fraud_model.pkl'")