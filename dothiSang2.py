import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
data = pd.read_csv('cars.csv')
# Thiết lập màu sắc cho từng loại xe
scatter_colors = {'unacc': 'red', 'acc': 'blue', 'good': 'green', 'vgood': 'purple'}

# Tạo biểu đồ scatter plot
plt.figure(figsize=(8, 6))
for category, color in scatter_colors.items():
    subset = data[data['class'] == category]
    plt.scatter(subset['buying'], subset['maint'], label=category, alpha=0.6, color=color)
# Thiết lập tiêu đề và nhãn trục
plt.title("Scatter Plot of Buying vs Maint by Car Class")
plt.xlabel("Buying Cost")
plt.ylabel("Maintenance Cost")
plt.legend(title='Car Class', loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True)
plt.show()
