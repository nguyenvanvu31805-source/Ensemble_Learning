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

| Model             | Accuracy | Precision | Recall | F1-Score |
| ----------------- | -------: | --------: | -----: | -------: |
| Random Forest     |   0.9000 |    0.9024 | 0.9000 |   0.8997 |
| AdaBoost          |   0.9333 |    0.9333 | 0.9333 |   0.9333 |
| Gradient Boosting |   0.9667 |    0.9697 | 0.9667 |   0.9666 |
| Voting            |   0.9667 |    0.9697 | 0.9667 |   0.9666 |
| Stacking          |   0.9667 |    0.9697 | 0.9667 |   0.9666 |

Gradient Boosting, Voting va Stacking dat Accuracy cao nhat trong lan chia du
lieu nay.

## Cong nghe

Python, NumPy, Pandas, scikit-learn, Joblib va Pytest.

## GitHub

Repository: https://github.com/nguyenvanvu31805-source/Ensemble_Learning

## HUONG DAN CHO NGUOI KHAC

Phan nay huong dan chay project tren mot may Windows moi. Khong can copy thu
muc `venv/`; moi may tu tao mot moi truong rieng tu `requirements.txt`.

### 1. Clone project

Can cai Git truoc, sau do mo PowerShell:

```powershell
git clone https://github.com/nguyenvanvu31805-source/Ensemble_Learning.git
cd Ensemble_Learning
```

Git Bash dung cung cac lenh:

```bash
git clone https://github.com/nguyenvanvu31805-source/Ensemble_Learning.git
cd Ensemble_Learning
```

### 2. Cai Python

Nen dung Python 3.11.x, giong phien ban trong Dockerfile. Kiem tra:

```powershell
python --version
```

Neu may dung lenh `py` thay cho `python`:

```powershell
py -3.11 --version
```

### 3. Tao va activate virtual environment

PowerShell:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

Neu PowerShell chan script activate, chi can mo PowerShell voi quyen phu hop
hoac dung lenh sau cho tai khoan hien tai:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Git Bash:

```bash
python -m venv venv
source venv/Scripts/activate
```

Khi activate thanh cong, dau nhac lenh thuong hien `(venv)`.

### 4. Cai thu vien

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

`requirements.txt` la danh sach thu vien va giup may moi cai lai moi truong
tuong ung. No thay the viec mang `venv` di, nhung khong chua du lieu huan
luyen hay ket qua.

Kiem tra nhanh:

```powershell
python --version
python -m pip list
```

### 5. Chay project

Chay truc tiep module train:

```powershell
python -m app.train
```

Hoac dung script:

```powershell
python scripts/run_project.py
```

Hai lenh tren doc `data/iris.csv`, huan luyen 5 model va ghi ket qua vao
`results/comparison.csv`. Cac file model `.pkl` duoc tao trong `models/` tren
may local nhung khong commit len GitHub.

Git Bash dung nguyen hai lenh `python` o tren.

### 6. Chay test

```powershell
python -m pytest -q
```

Dung `python -m pytest` de chac chan pytest duoc goi tu virtual environment
dang activate.

### 7. Chay bang Docker

Docker la lua chon thay the. Can cai Docker Desktop va dam bao Docker Engine
dang chay, sau do kiem tra:

```powershell
docker --version
docker info
```

Build image:

```powershell
docker build -t iris-ensemble .
```

Chay training trong container:

```powershell
docker run --rm iris-ensemble
```

Lenh tren dung Python 3.11 trong image va cai thu vien tu
`requirements.txt`; khong can cai Python hoac thu vien ML tren may host.

De luu `models/` va `results/` ra thu muc project tren Windows PowerShell:

```powershell
docker run --rm -v "${PWD}/models:/app/models" -v "${PWD}/results:/app/results" iris-ensemble
```

Tren Git Bash:

```bash
docker run --rm -v "$PWD/models:/app/models" -v "$PWD/results:/app/results" iris-ensemble
```

Dockerfile khong copy `venv/` hoac cac file `.pkl` cu. Container tu huan luyen
va tao model moi, vi vay co the chay ngay sau khi clone repository sach.

### 8. Kiem tra tren may hoan toan moi

Thuc hien theo thu tu:

```powershell
git clone https://github.com/nguyenvanvu31805-source/Ensemble_Learning.git
cd Ensemble_Learning
python --version
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m app.train
python -m pytest -q
type results\comparison.csv
```

Neu dung Git Bash, thay dong cuoi bang:

```bash
cat results/comparison.csv
```

### 9. Neu ket qua khac

Kiem tra cac diem sau:

- Python va cac phien ban thu vien co giong nhau khong.
- Lenh co duoc chay tu thu muc goc project khong.
- `data/iris.csv` co dung file va dung 150 dong khong.
- Code co dung cung `test_size=0.2`, `random_state=42` va `stratify=y` khong.
- Ket qua dang so sanh la file `results/comparison.csv` cua lan train moi.
- May co dang dung file model `.pkl` cu thay vi train lai khong.

Ket qua co the khac nho neu khac phien ban Python, scikit-learn, NumPy hoac
he dieu hanh. Docker giup co moi truong Python va thu vien gan dong nhat, nhung
ket qua van nen duoc kiem tra tu file CSV thuc te.

### 10. File nen va khong nen push

Nen push: `app/`, `data/iris.csv`, `scripts/`, `tests/`, `training/`,
`README.md`, `ML.md`, `project.md`, `requirements.txt`, `Dockerfile` va
`.dockerignore`.

Khong nen push: `venv/`, `__pycache__/`, `*.pyc`, `.pytest_cache/`, file
`.env` va model `.pkl` sinh ra local. Cac quy tac nay da duoc dat trong
`.gitignore`.
