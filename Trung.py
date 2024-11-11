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

# Mã hóa các biến phân loại thành các giá trị số
# Sử dụng pandas để mã hóa cột phân loại
encoded_df = df.copy()
for column in df.select_dtypes(include=['object']).columns:
    encoded_df[column] = encoded_df[column].astype('category').cat.codes

# Các mối quan hệ từng cặp (sử dụng dữ liệu đã được mã hóa nhãn)
class_mapping = dict(enumerate(df['class'].astype('category').cat.categories))
print(class_mapping)    
plt.figure(figsize=(4, 3))
sns.pairplot(encoded_df, hue='class', palette="plasma")
plt.show()

# Phân tích sự cân bằng các lớp xe 
plt.figure(figsize=(8, 6))
class_counts = df['class'].value_counts()
sns.barplot(x=class_counts.index, y=class_counts.values, palette='Set2')
plt.title('Phân tích sự cân bằng các lớp xe')
plt.ylabel('Số lượng')
plt.xlabel('Lớp xe')
plt.show()