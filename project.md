# Project Description

## 1. Tên đề tài

Phân loại hoa Iris bằng phương pháp Ensemble Learning.

## 2. Bài toán

Xây dựng các mô hình học máy kết hợp để phân loại hoa Iris
thành ba lớp:

- Iris Setosa
- Iris Versicolor
- Iris Virginica

## 3. Mục tiêu

- Tìm hiểu Ensemble Learning.
- Tìm hiểu các phương pháp Bagging, Boosting, Voting và Stacking.
- Xây dựng các mô hình Ensemble trên tập dữ liệu Iris.
- So sánh hiệu quả của các mô hình.

## 4. Các mô hình

- Random Forest
- AdaBoost
- Gradient Boosting
- Voting Classifier
- Stacking Classifier

## 5. Dataset

Iris Dataset gồm 150 mẫu và 4 đặc trưng:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

## 6. Kết quả

Các mô hình được đánh giá bằng:

- Accuracy
# Mo ta project

## Ten de tai

Ensemble Learning - Phan loai hoa Iris.

## Bai toan va muc tieu

Du doan mot mau hoa thuoc Setosa, Versicolor hay Virginica tu bon so do cua
dai hoa va canh hoa. Muc tieu la thuc hanh tien xu ly, huan luyen nhieu model
Ensemble va so sanh ket qua.

## Dataset va tien xu ly

Iris co 150 mau, 4 dac trung (`sepal_length`, `sepal_width`, `petal_length`,
`petal_width`) va 3 lop. Code chia train/test theo ty le 80/20 voi
`random_state=42`, `stratify=y`, sau do dung `StandardScaler` fit tren train.

## Cac model

- Random Forest: Bagging nhieu cay quyet dinh.
- AdaBoost: Boosting tuan tu, tap trung vao mau du doan sai.
- Gradient Boosting: Boosting bang cach giam dan loi.
- Voting: soft voting giua Logistic Regression, Random Forest va SVM.
- Stacking: Random Forest va Gradient Boosting ket hop qua Logistic Regression.

## Danh gia va ket qua

Project tinh Accuracy, Precision, Recall va F1-Score theo weighted average.
Ket qua luu tai `results/comparison.csv`; model da huan luyen va scaler luu tai
`models/` nhung file `.pkl` duoc loai khoi Git.

## Cong nghe

Python, NumPy, Pandas, scikit-learn, Joblib va Pytest.