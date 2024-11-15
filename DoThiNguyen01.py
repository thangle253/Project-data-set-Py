import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

# Đọc dữ liệu từ file CSV
data = pd.read_csv(r'D:/PRJPython/DoAnCuoiKiPy/cars.csv')

def cramers_v(x, y):
    """Hàm tính độ tương quan Cramér's V giữa hai cột phân loại"""
    contingency_table = pd.crosstab(x, y)
    
# Mục đích: Tạo bảng phân phối chéo (contingency table) cho hai biến x và y.
# Bảng phân phối chéo: Là bảng hiển thị tần suất xuất hiện của các cặp giá trị từ hai biến x và y.
# Ví dụ: Nếu x là safety và y là class, bảng này sẽ cho biết có bao nhiêu mẫu thuộc từng cặp (safety, class).
    chi2 = chi2_contingency(contingency_table)[0]
    
#Chi-squared test (chi2_contingency): Là phép kiểm định giả thuyết để xác định xem hai biến phân loại có phụ thuộc vào nhau hay không.
# Giá trị chi2 lớn cho thấy có sự phụ thuộc giữa hai biến, ngược lại giá trị nhỏ cho thấy hai biến độc lập.
# [0]: Lấy giá trị chi2 từ kết quả trả về của hàm chi2_contingency.
    n = contingency_table.sum().sum()
#contingency_table.sum().sum(): Tính tổng tất cả các phần tử trong bảng phân phối chéo, tương đương với tổng số mẫu trong tập dữ liệu.
    r, k = contingency_table.shape
    return np.sqrt(chi2 / (n * (min(r, k) - 1)))
# Công thức Cramér's V: sqrt(chi2 / (n * (min(r, k) - 1)))
# chi2: Giá trị chi-squared đã tính trước đó.
# n: Tổng số mẫu.
# min(r, k) - 1: Điều chỉnh để đảm bảo giá trị Cramér's V nằm trong khoảng từ 0 đến 1.
# Kết quả:
# V = 0: Không có tương quan giữa x và y.
# V = 1: Tương quan hoàn hảo giữa x và y.
# Giá trị V càng gần 1, mối quan hệ giữa hai biến càng mạnh.

# Tính Cramér's V cho tất cả các đặc trưng với biến mục tiêu
target = 'class'
features = [col for col in data.columns if col != target]
correlations = {}

for feature in features:
    correlations[feature] = cramers_v(data[feature], data[target])

# Sắp xếp các đặc trưng theo mức độ tương quan giảm dần
sorted_features = sorted(correlations, key=correlations.get, reverse=True)
importance_values = [correlations[feature] for feature in sorted_features]

# Vẽ biểu đồ
plt.figure(figsize=(12, 8))
colors = plt.cm.viridis(np.linspace(0, 1, len(sorted_features)))
plt.bar(sorted_features, importance_values, color=colors)
plt.title('Feature Importance based on Cramér\'s V')
plt.xlabel('Features')
plt.ylabel('Importance')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
