# Ensemble Learning - Phan loai hoa Iris

## Gioi thieu

Project mon Hoc may co ban minh hoa Ensemble Learning cho bai toan phan loai
hoa Iris. Project huan luyen va so sanh nam model tren cung mot tap kiem tra.

## Bai toan va dataset

Iris gom 150 mau, 4 dac trung (`sepal_length`, `sepal_width`, `petal_length`,
`petal_width`) va 3 lop `setosa`, `versicolor`, `virginica`.

Code dung `train_test_split` voi `test_size=0.2`, `random_state=42` va
`stratify=y`, sau do chuan hoa bang `StandardScaler` fit tren tap train.

## Ensemble Learning va cac model

Ensemble Learning ket hop nhieu model de tao du doan chung.

- **Random Forest:** Bagging nhieu cay quyet dinh.
- **AdaBoost:** Boosting tuan tu, tap trung vao mau bi du doan sai.
- **Gradient Boosting:** Boosting bang cach them cay de giam loi dan.
- **Voting:** soft voting giua Logistic Regression, Random Forest va SVM.
- **Stacking:** Random Forest va Gradient Boosting lam model co so, Logistic
	Regression lam meta-model.

Chi tiet ly thuyet nam trong [ML.md](ML.md).

## Cau truc project

```text
app/                  Ma tien xu ly, model, train va danh gia
data/                 Dataset Iris
models/               Model da huan luyen, khong commit file .pkl
results/              Bang ket qua
scripts/              Script chay project
tests/                Test tu dong
training/             Tai lieu training
README.md             Huong dan project
ML.md                 Ly thuyet Machine Learning
project.md            Mo ta project
requirements.txt      Thu vien can cai
run.py                Tao lai dataset Iris
```

## Cai dat

```bash
python -m venv venv
source venv/Scripts/activate
python -m pip install -r requirements.txt
```

Tren PowerShell, kich hoat bang `venv\\Scripts\\Activate.ps1`.

## Cach chay

```bash
python -m app.train
python scripts/run_project.py
```

Ket qua duoc ghi vao `results/comparison.csv`. Co the tao lai dataset bang
`python run.py`.

## Cach test

```bash
pytest -q
```

## Ket qua thuc te

Bang duoi day duoc doc tu `results/comparison.csv` sau lan train hien tai:

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---:|---:|---:|---:|
| Random Forest | 0.9000 | 0.9024 | 0.9000 | 0.8997 |
| AdaBoost | 0.9333 | 0.9333 | 0.9333 | 0.9333 |
| Gradient Boosting | 0.9667 | 0.9697 | 0.9667 | 0.9666 |
| Voting | 0.9667 | 0.9697 | 0.9667 | 0.9666 |
| Stacking | 0.9667 | 0.9697 | 0.9667 | 0.9666 |

Gradient Boosting, Voting va Stacking dat Accuracy cao nhat trong lan chia du
lieu nay.

## Cong nghe

Python, NumPy, Pandas, scikit-learn, Joblib va Pytest.

## GitHub

Repository: https://github.com/nguyenvanvu31805-source/Ensemble_Learning