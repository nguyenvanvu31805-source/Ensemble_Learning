from app.data_preprocessing import load_data, prepare_data
from app.models import get_models


def test_project_defines_expected_models():
	assert list(get_models()) == [
		"Random Forest",
		"AdaBoost",
		"Gradient Boosting",
		"Voting",
		"Stacking",
	]


def test_iris_preprocessing_has_expected_split():
	data = load_data("data/iris.csv")
	X_train, X_test, y_train, y_test, scaler = prepare_data(data)

	assert data.shape == (150, 5)
	assert X_train.shape == (120, 4)
	assert X_test.shape == (30, 4)
	assert len(y_train) == 120
	assert len(y_test) == 30
	assert scaler.n_features_in_ == 4
