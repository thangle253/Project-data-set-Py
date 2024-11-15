import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu từ file CSV
df = pd.read_csv('cars.csv')

# Kiểm tra thông tin cơ bản của dữ liệu
print(df.head())
print(df.describe())
print(df.isnull().sum())
print(df.info())

# Mã hóa các biến phân loại thành các giá trị số
encoded_df = df.copy()
for column in df.select_dtypes(include=['object']).columns:
    encoded_df[column] = encoded_df[column].astype('category').cat.codes

# Xem dữ liệu sau khi mã hóa
print(encoded_df.head())

# 1. Heatmap của ma trận tương quan
plt.figure(figsize=(10, 8))
correlation_matrix = encoded_df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Ma trận tương quan giữa các biến đã mã hóa')
plt.show()

# 2. Countplot cho biến đã mã hóa (ví dụ: buying)
plt.figure(figsize=(8, 6))
sns.countplot(x='buying', data=encoded_df, palette='viridis')
plt.title('Phân phối các mức giá mua xe (đã mã hóa)')
plt.xlabel('Mã hóa mức giá mua')
plt.ylabel('Số lượng')
plt.show()

# 3. Box Plot để so sánh phân phối của các nhóm mã hóa
plt.figure(figsize=(8, 6))
sns.boxplot(x='class', y='safety', data=encoded_df, palette='Set3')
plt.title('Phân phối mức độ an toàn theo loại xe (mã hóa)')
plt.xlabel('Loại xe (mã hóa)')
plt.ylabel('Mức độ an toàn (mã hóa)')
plt.show()

# 4. Scatter Plot giữa các biến đã mã hóa
plt.figure(figsize=(8, 6))
sns.scatterplot(x='buying', y='maint', hue='class', data=encoded_df, palette='deep')
plt.title('Mối quan hệ giữa chi phí mua và bảo trì theo loại xe')
plt.xlabel('Chi phí mua (mã hóa)')
plt.ylabel('Chi phí bảo trì (mã hóa)')
plt.show()
