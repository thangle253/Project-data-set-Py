import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu từ file CSV
df = pd.read_csv("cars.csv")
print(df)

# Định nghĩa thứ tự cho các giá trị trong cột 'buying' và 'safety'
buying_order = ['low', 'med', 'high', 'vhigh']
safety_order = ['low', 'med', 'high']

# Chuyển đổi các cột 'buying' và 'safety' thành kiểu Categorical với thứ tự đã định nghĩa
df['buying'] = pd.Categorical(df['buying'], categories=buying_order, ordered=True)
df['safety'] = pd.Categorical(df['safety'], categories=safety_order, ordered=True)

# Tạo bảng crosstab giữa chi phí mua và độ an toàn, chuẩn hóa theo hàng
interaction_crosstab = pd.crosstab(df['buying'], df['safety'], normalize='index')
print(interaction_crosstab)
# Tạo biểu đồ nhiệt
plt.figure(figsize=(8, 6))
sns.heatmap(interaction_crosstab, annot=True, cmap='Oranges', fmt='.4f', yticklabels=buying_order[::-1])

# Thiết lập tiêu đề cho biểu đồ
plt.title('Buying vs Safety Crosstab Heatmap')
plt.show()