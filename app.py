"""
MLOps Assignment 6: Prediction Application
Loads model.joblib and accepts Iris flower measurements to predict species.
Input Features: Sepal Length, Sepal Width, Petal Length, Petal Width
"""

import os
import sys
import warnings
import numpy as np
import joblib

# Suppress serialization version mismatch warnings when model is loaded across environments
warnings.filterwarnings("ignore", category=UserWarning)

FEATURE_NAMES = [
    "Sepal Length (cm)",
    "Sepal Width (cm)",
    "Petal Length (cm)",
    "Petal Width (cm)",
]

CLASS_NAMES = ["setosa", "versicolor", "virginica"]
MODEL_FILENAME = "model.joblib"


def load_model(filepath: str = MODEL_FILENAME):
    """
    Loads the serialized model artifact with error handling.
    Exits gracefully if file is missing or corrupted.
    """
    if not os.path.exists(filepath):
        print(f"[ERROR] Model file '{filepath}' was not found in directory: {os.getcwd()}", file=sys.stderr)
        print("Please train the model first by executing: python train_model.py", file=sys.stderr)
        sys.exit(1)
    try:
        model = joblib.load(filepath)
        return model
    except Exception as exc:
        print(f"[ERROR] Failed to load model artifact '{filepath}': {exc}", file=sys.stderr)
        sys.exit(1)


def parse_and_validate_input(user_string: str):
    """
    Parses comma- or space-separated input into four positive float values.
    Validates token count and data types.
    """
    cleaned = user_string.strip()
    if not cleaned:
        raise ValueError("Empty input received. Exactly 4 numeric values are required.")

    # Accept both comma-separated ("5.1, 3.5, 1.4, 0.2") and space-separated ("5.1 3.5 1.4 0.2")
    if "," in cleaned:
        tokens = [t.strip() for t in cleaned.split(",") if t.strip()]
    else:
        tokens = cleaned.split()

    if len(tokens) != 4:
        raise ValueError(
            f"Expected exactly 4 feature values, but received {len(tokens)}: {tokens}"
        )

    try:
        float_values = [float(t) for t in tokens]
    except ValueError as conv_err:
        raise ValueError(f"All values must be valid decimal numbers. Error: {conv_err}")

    # Validate physical plausibility (biological measurements must be strictly positive)
    for name, val in zip(FEATURE_NAMES, float_values):
        if val <= 0:
            raise ValueError(f"Measurement '{name}' must be positive. Received: {val}")

    return float_values


def predict(model, measurements):
    """
    Converts measurement list into a 2D NumPy array of shape (1, 4),
    passes to model.predict(), and returns class index and species name.
    """
    features_array = np.array(measurements, dtype=float).reshape(1, 4)
    pred_class_idx = int(model.predict(features_array)[0])
    species_name = CLASS_NAMES[pred_class_idx]
    return pred_class_idx, species_name, features_array


def main():
    print("=" * 65)
    print("       Iris Flower Species - Model Inference Application")
    print("=" * 65)

    # 1. Load model artifact
    model = load_model(MODEL_FILENAME)
    print(f"[INFO] Model artifact '{MODEL_FILENAME}' successfully loaded.")

    # 2. Display expected features
    print("\nRequired Features:")
    for idx, feature in enumerate(FEATURE_NAMES, 1):
        print(f"  {idx}. {feature}")

    # 3. Read input from CLI arguments or standard interactive input
    if len(sys.argv) > 1:
        raw_text = " ".join(sys.argv[1:])
        print(f"\n[INPUT] Read from command-line arguments: {raw_text}")
    else:
        print("\nEnter 4 values separated by commas (e.g. 5.1, 3.5, 1.4, 0.2):")
        try:
            raw_text = input("Measurements > ")
        except (EOFError, KeyboardInterrupt):
            print("\nInput operation cancelled. Exiting.")
            sys.exit(0)

    # 4. Validate input
    try:
        measurements = parse_and_validate_input(raw_text)
    except ValueError as validation_error:
        print(f"\n[ERROR] Input validation failed: {validation_error}", file=sys.stderr)
        print("Example of valid input format: 5.1, 3.5, 1.4, 0.2", file=sys.stderr)
        sys.exit(1)

    # 5. Display formatted features
    print("\nReceived Measurements:")
    for name, val in zip(FEATURE_NAMES, measurements):
        print(f"  - {name}: {val}")

    # 6. Execute model prediction
    class_idx, species, input_matrix = predict(model, measurements)

    # 7. Display prediction result clearly
    print("\n" + "=" * 65)
    print(f"  Input Vector:      {input_matrix.tolist()[0]}")
    print(f"  Predicted Class:   {class_idx}")
    print(f"  PREDICTED SPECIES: {species}")
    print("=" * 65)


if __name__ == "__main__":
    main()
