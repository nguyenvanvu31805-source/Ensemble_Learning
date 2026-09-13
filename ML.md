# Machine Learning va Ensemble Learning

## Ensemble Learning

Ensemble Learning ket hop nhieu model de tao du doan chung. Cac model co the
bo tro diem yeu cua nhau, giup ket qua on dinh hon.

## Bagging va Random Forest

Bagging huan luyen nhieu model tren cac mau du lieu khac nhau roi tong hop du
doan. Random Forest la Bagging dung nhieu cay quyet dinh va chon ngau nhien
mot phan dac trung khi xay cay. No giam phuong sai va thuong manh, nhung kho
giai thich hon mot cay don va ton tai nguyen hon.

## Boosting

Boosting xay dung model theo thu tu. Model sau tap trung sua loi cua model
truoc, thuong giam bias va tang do chinh xac. Nhuoc diem la nhay voi nhieu va
co the overfit neu cau hinh khong phu hop.

### AdaBoost

AdaBoost tang trong so cho cac mau bi du doan sai de model sau chu y hon. No
de hieu va thuong hieu qua, nhung nhay voi outlier va nhieu.

### Gradient Boosting

Gradient Boosting them cac cay moi de giam dan ham loi. No phu hop du lieu bang
nhu Iris va co the dat ket qua tot, nhung huan luyen tuan tu va can chinh tham
so de tranh overfit.

## Voting

Voting ket hop nhieu model doc lap. Hard voting chon nhan duoc nhieu phieu
nhat; soft voting dung xac suat du doan. Project dung soft voting voi Logistic
Regression, Random Forest va SVM. Uu diem la ket hop nhieu cach hoc, nhung phu
thuoc vao chat luong cac model thanh phan.

## Stacking

Stacking dung cac model co so tao du doan, sau do dua cac du doan nay cho
meta-model. Project dung Random Forest va Gradient Boosting lam model co so,
Logistic Regression lam meta-model. Cach nay linh hoat nhung phuc tap va ton
thoi gian hon.

## Iris trong project

Dataset co 150 mau, 4 dac trung va 3 lop Setosa, Versicolor, Virginica. Code
dung 80% de train va 20% de test, co stratify de giu ty le lop. StandardScaler
fit tren train roi transform train va test. Metric gom Accuracy, Precision,
Recall va F1-Score theo weighted average.