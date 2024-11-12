import pandas as pd  
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt # type: ignore

df = pd.read_csv('cars.csv')
#biểu đồ phân phối của các biến phân loại
categorical_columns = df.columns[:-1]  #các cột không phải là cột target
plt.figure(figsize=(12, 8)) #kích thước biểu đồ: 12x8
for i, column in enumerate(categorical_columns, 1): #duyệt qua các cột
    plt.subplot(3, 2, i) #vẽ biểu đồ ở hàng 3, cột 2, vị trí
    sns.countplot(x=column, data=df, palette='viridis') # vẽ biểu đồ bằng seaborn
    plt.title(f'Distribution of {column}') #tiêu đề của từng biểu đồ biểu đồ 
    plt.xticks(rotation=45) #xoay nhãn trục x 45 độ
plt.tight_layout() #để tránh trùng lắp giữa các biểu đồ
plt.show()

#biểu đồ phân phối của các biến phân loại theo biến target
plt.figure(figsize=(12,8))
for i, col in enumerate(categorical_columns): #duyệt qua các cột
    plt.subplot(3, 2, i+1) #vẽ biểu đồ ở hàng 3, cột 2, vị trí
    sns.countplot(data=df,x=col,hue='class') #vẽ biểu đồ bằng seaborn
plt.tight_layout() #để tránh trùng lắp giữa các biểu đồ
plt.show()

df = pd.read_csv("cars.csv")
interaction_crosstab = pd.crosstab(df['buying'], df['safety'], normalize='index')
plt.figure(figsize=(8, 6))
sns.heatmap(interaction_crosstab, annot=True, cmap='Blues', fmt='.2f')
plt.title('Buying vs Safety Crosstab Heatmap')
plt.show()
