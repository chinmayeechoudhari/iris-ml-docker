"""
MLOps Assignment 6: Train an ML Model on the Iris Dataset
Model: RandomForestClassifier (n_estimators=100, random_state=42)
Artifact: model.joblib
"""

import os
import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


def main():
    print("=" * 65)
    print("      Iris Flower Classification - Model Training Pipeline")
    print("=" * 65)

    # 1. Import the Iris dataset from sklearn.datasets
    print("[1/5] Loading Iris dataset from sklearn.datasets...")
    iris = load_iris()
    X = iris.data
    y = iris.target
    feature_names = iris.feature_names
    target_names = iris.target_names

    print(f"      Feature Names: {feature_names}")
    print(f"      Target Classes: {list(target_names)}")
    print(f"      Dataset Shape: {X.shape[0]} samples, {X.shape[1]} features")

    # 2. Split dataset into training and testing sets (80:20 split, random_state=42)
    print("\n[2/5] Splitting dataset into 80% train and 20% test sets (random_state=42)...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42
    )
    print(f"      Training samples: {X_train.shape[0]}")
    print(f"      Testing samples:  {X_test.shape[0]}")

    # 3. Train a RandomForestClassifier with 100 estimators
    print("\n[3/5] Training RandomForestClassifier (n_estimators=100, random_state=42)...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    print("      Training completed successfully.")

    # 4. Generate predictions on testing dataset and calculate metrics
    print("\n[4/5] Evaluating model on testing dataset...")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, target_names=target_names)

    print("-" * 65)
    print(f"Test Accuracy: {accuracy:.4f} ({accuracy * 100:.2f}%)")
    print("-" * 65)
    print("Classification Report:")
    print(report)
    print("-" * 65)

    # 5. Save the trained model using Joblib
    model_filepath = "model.joblib"
    print(f"[5/5] Saving trained model artifact to '{model_filepath}'...")
    joblib.dump(model, model_filepath)

    if os.path.exists(model_filepath):
        file_size_kb = os.path.getsize(model_filepath) / 1024
        print(f"      Model artifact confirmed: '{model_filepath}' ({file_size_kb:.2f} KB)")
        print("      Model saving confirmation: SUCCESS")
    else:
        print("      ERROR: Model artifact could not be verified on disk!")

    print("=" * 65)


if __name__ == "__main__":
    main()
