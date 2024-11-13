import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Đọc dữ liệu từ file CSV
data = pd.read_csv(r'D:/PRJPython/DoAnCuoiKiPy/cars.csv')

# Kiểm tra cấu trúc dữ liệu
print(data.head())

# Tính độ tương quan giữa các đặc trưng và biến mục tiêu
correlations = {}
target = 'class'

# Lấy danh sách các cột, trừ cột mục tiêu
features = [col for col in data.columns if col != target]

for feature in features:
    correlation = data[feature].astype('category').cat.codes.corr(data[target].astype('category').cat.codes)
    correlations[feature] = abs(correlation)

# Sắp xếp độ tương quan từ cao đến thấp
sorted_features = sorted(correlations, key=correlations.get, reverse=True)
importance_values = [correlations[feature] for feature in sorted_features]

# Vẽ biểu đồ
plt.figure(figsize=(10, 6))
plt.bar(sorted_features, importance_values, color=['red', 'blue', 'green', 'purple', 'orange', 'yellow'])
plt.title('Feature Importance based on Correlation')
plt.xlabel('Features')
plt.ylabel('Importance')
plt.show()