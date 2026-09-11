from sklearn.ensemble import (
    RandomForestClassifier,
    AdaBoostClassifier,
    GradientBoostingClassifier,
    VotingClassifier,
    StackingClassifier
)

from sklearn.linear_model import LogisticRegression

from sklearn.svm import SVC


def get_models():

    models = {}

    # Random Forest
    models["Random Forest"] = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    # AdaBoost
    models["AdaBoost"] = AdaBoostClassifier(
        n_estimators=100,
        random_state=42
    )

    # Gradient Boosting
    models["Gradient Boosting"] = GradientBoostingClassifier(
        n_estimators=100,
        random_state=42
    )

    # Voting
    models["Voting"] = VotingClassifier(
        estimators=[
            (
                "logistic",
                LogisticRegression(max_iter=1000)
            ),
            (
                "random_forest",
                RandomForestClassifier(
                    n_estimators=100,
                    random_state=42
                )
            ),
            (
                "svm",
                SVC(probability=True)
            )
        ],
        voting="soft"
    )

    # Stacking
    models["Stacking"] = StackingClassifier(
        estimators=[
            (
                "random_forest",
                RandomForestClassifier(
                    n_estimators=100,
                    random_state=42
                )
            ),
            (
                "gradient_boosting",
                GradientBoostingClassifier(
                    n_estimators=100,
                    random_state=42
                )
            )
        ],
        final_estimator=LogisticRegression(
            max_iter=1000
        )
    )

    return models