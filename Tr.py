import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
# Đọc dữ liệu từ file CSV
df = pd.read_csv('cars.csv')

# Kiểm tra một số thông tin cơ bản của dữ liệu
df.head()
df.describe()
df.isnull().sum()
df.info()
# Mã hóa
encoded_df = df.copy()
encoded_df['class'] = encoded_df['class'].astype('category').cat.codes

# Phân tích sự cân bằng các lớp xe 
plt.figure(figsize=(8, 6))
class_counts = encoded_df['class'].value_counts()
sns.barplot(x=class_counts.index, y=class_counts.values, palette='Set2')
plt.title('Phân tích sự cân bằng các lớp xe')
plt.ylabel('Số lượng')
plt.xlabel('Lớp xe')
plt.show()