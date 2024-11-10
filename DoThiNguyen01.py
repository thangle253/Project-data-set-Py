import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Load dữ liệu và tiền xử lý (thay thế 'path_to_file' bằng đường dẫn file của bạn)
df = pd.read_csv(r'D:/PRJPython/DoAnCuoiKiPy/cars.csv')
df.head()
df.describe()
df.isnull().sum()
df.info()
# Mã hóa các biến phân loại
label_encoder = LabelEncoder()
encoded_df = df.apply(label_encoder.fit_transform)

X = encoded_df.drop('class', axis=1)
y = encoded_df['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)
print(f'Accuracy:  {accuracy_score(y_test, y_pred):.4f}')
print(f'Precision: {precision_score(y_test, y_pred, average="weighted"):.4f}')

# Tính accuracy và precision cho từng điểm trong tập kiểm thử
accuracy_list = []
precision_list = []
for i in range(1, len(y_test) + 1):
    accuracy = accuracy_score(y_test[:i], y_pred[:i])
    precision = precision_score(y_test[:i], y_pred[:i], average='weighted', zero_division=0)
    accuracy_list.append(accuracy)
    precision_list.append(precision)

# Hàm tính moving average
def moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

# Tính moving averages cho accuracy và precision
window_size = 10
smoothed_accuracy = moving_average(accuracy_list, window_size)
smoothed_precision = moving_average(precision_list, window_size)

# Vẽ biểu đồ
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(smoothed_accuracy) + 1), smoothed_accuracy, label='Average Accuracy', color='blue')
plt.plot(range(1, len(smoothed_precision) + 1), smoothed_precision, label='Average Precision', color='orange')
plt.title(f'Moving Average ({window_size}) of Model Accuracy and Precision Over Test Dataset')
plt.ylabel('Score')
plt.legend()
plt.grid()
plt.ylim(0.7, 1)
plt.show()