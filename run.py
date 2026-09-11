from sklearn.datasets import load_iris
import pandas as pd
import os


def create_dataset():

    iris = load_iris()

    df = pd.DataFrame(
        iris.data,
        columns=[
            "sepal_length",
            "sepal_width",
            "petal_length",
            "petal_width"
        ]
    )

    df["target"] = [
        iris.target_names[i]
        for i in iris.target
    ]

    os.makedirs("data", exist_ok=True)

    df.to_csv(
        "data/iris.csv",
        index=False
    )

    print("================================")
    print("ĐÃ TẠO DATASET IRIS")
    print("================================")

    print(df.head())

    print()
    print("Số dòng:", len(df))
    print("Số cột:", len(df.columns))


if __name__ == "__main__":
    create_dataset()