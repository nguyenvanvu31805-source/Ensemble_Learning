import os
import joblib
import pandas as pd

from app.data_preprocessing import (
    load_data,
    prepare_data
)

from app.models import get_models

from app.evaluate import evaluate_model


def train_models():

    # Load dataset
    df = load_data(
        "data/iris.csv"
    )

    print("Dataset:")
    print(df.head())

    print()
    print("Kích thước:", df.shape)

    # Prepare data
    (
        X_train,
        X_test,
        y_train,
        y_test,
        scaler
    ) = prepare_data(df)

    # Get models
    models = get_models()

    os.makedirs(
        "models",
        exist_ok=True
    )

    results = []

    # Train từng model
    for name, model in models.items():

        print()
        print("==============================")
        print("Đang huấn luyện:", name)
        print("==============================")

        model.fit(
            X_train,
            y_train
        )

        metrics = evaluate_model(
            model,
            X_test,
            y_test
        )

        print(
            "Accuracy :",
            round(metrics["Accuracy"], 4)
        )

        print(
            "Precision:",
            round(metrics["Precision"], 4)
        )

        print(
            "Recall   :",
            round(metrics["Recall"], 4)
        )

        print(
            "F1-Score :",
            round(metrics["F1-Score"], 4)
        )

        results.append({
            "Model": name,
            "Accuracy": metrics["Accuracy"],
            "Precision": metrics["Precision"],
            "Recall": metrics["Recall"],
            "F1-Score": metrics["F1-Score"]
        })

        file_name = (
            name.lower()
            .replace(" ", "_")
            + ".pkl"
        )

        joblib.dump(
            model,
            f"models/{file_name}"
        )

    # Save scaler
    joblib.dump(
        scaler,
        "models/scaler.pkl"
    )

    # Save results
    os.makedirs(
        "results",
        exist_ok=True
    )

    result_df = pd.DataFrame(
        results
    )

    result_df.to_csv(
        "results/comparison.csv",
        index=False
    )

    print()
    print("================================")
    print("HOÀN THÀNH HUẤN LUYỆN")
    print("================================")

    print(result_df)


if __name__ == "__main__":
    train_models()