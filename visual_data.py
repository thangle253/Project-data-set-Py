import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('cars.csv')
def BieuDo1():
    """Biểu đồ phân tích sự phân phối các biến trong đánh giá ô tô"""
    categorical_columns = df.columns[:-1] 
    plt.figure(figsize=(12, 8)) 
    for i, column in enumerate(categorical_columns, 1): 
        plt.subplot(3, 2, i) 
        sns.countplot(x=column, data=df, palette='viridis') 
        plt.title(f'Distribution of {column}')
        plt.xticks(rotation=45) 
    plt.tight_layout()
    plt.show()
def BieuDo2():
    """"Biểu đồ phân tích ảnh hưởng của các thuộc tính xe hơi đến đánh giá chất lượng"""
    categorical_columns = df.columns[:-1] 
    plt.figure(figsize=(12,8))
    for i, col in enumerate(categorical_columns): #duyệt qua các cột
        plt.subplot(3, 2, i+1) #vẽ biểu đồ ở hàng 3, cột 2, vị trí
        sns.countplot(data=df,x=col,hue='class') #vẽ biểu đồ bằng seaborn
    plt.tight_layout() #để tránh trùng lắp giữa các biểu đồ
    plt.show()
def BieuDo3():
    """Biểu đồ nhiệt phân tích mối quan hệ giữa giá mua và mức độ an toàn của xe"""
    buying_order = ['low', 'med', 'high', 'vhigh']
    safety_order = ['low', 'med', 'high']
    # Chuyển đổi các cột 'buying' và 'safety' thành kiểu Categorical với thứ tự đã định nghĩa
    df['buying'] = pd.Categorical(df['buying'], categories=buying_order, ordered=True)
    df['safety'] = pd.Categorical(df['safety'], categories=safety_order, ordered=True)
    # Tạo bảng crosstab giữa chi phí mua và độ an toàn, chuẩn hóa theo hàng
    interaction_crosstab = pd.crosstab(df['buying'], df['safety'], normalize='index')
    print(interaction_crosstab)
    # Tạo biểu đồ nhiệt
    plt.figure(figsize=(12, 8))
    sns.heatmap(interaction_crosstab, annot=True, cmap='Blues', fmt='.3f', yticklabels=buying_order[::-1])
    # Thiết lập tiêu đề cho biểu đồ
    plt.title('Buying vs Safety Crosstab Heatmap')
    plt.show()
def BieuDo4():
    """Biểu đồ phân tán thể hiện sự phân bố các lớp xe dựa trên giá mua và chi phí bảo dưỡng"""
    scatter_colors = {'unacc': 'red', 'acc': 'blue', 'good': 'green', 'vgood': 'purple'}
    plt.figure(figsize=(12, 8))
    for category, color in scatter_colors.items():
        subset = df[df['class'] == category]
        plt.scatter(subset['buying'], subset['maint'], label=category, alpha=0.6, color=color)
    plt.title("Scatter Plot of Buying vs Maint by Car Class")
    plt.xlabel("Buying Cost")
    plt.ylabel("Maintenance Cost")
    plt.legend(title='Car Class', loc='upper left', bbox_to_anchor=(1, 1))
    plt.grid(True)
    plt.show()
def BieuDo5():
    """Biểu đồ thể hiện về mối quan hệ giữa các đặc điểm khác nhau của xe và cách chúng phân bố theo các lớp xe"""
    encoded_df = df.copy()
    for column in df.select_dtypes(include=['object']).columns:
        encoded_df[column] = encoded_df[column].astype('category').cat.codes

    # Các mối quan hệ từng cặp (sử dụng dữ liệu đã được mã hóa nhãn)
    class_mapping = dict(enumerate(df['class'].astype('category').cat.categories))
    encoded_df['class'] = encoded_df['class'].map(class_mapping)
    plt.figure(figsize=(12, 8))
    pairplot = sns.pairplot(encoded_df, hue='class', palette="Set1")
    # Thiết lập giá trị cho các trục x và y của mỗi biểu đồ con
    for ax in pairplot.axes.flatten():
        ax.set_xticks([0, 1, 2, 3])  # Các giá trị trục x
        ax.set_yticks([0, 1, 2, 3])  # Các giá trị trục y
    plt.show()
def BieuDo6():
    """ Biểu đồ thống kê số lượng xe dựa trên mức đánh giá"""
    # Mã hóa các biến phân loại thành các giá trị số
    encoded_df = df.copy()
    for column in df.select_dtypes(include=['object']).columns:
        encoded_df[column] = encoded_df[column].astype('category').cat.codes
    # Tính toán số lượng xe theo loại xe
    class_counts = df['class'].value_counts()
    # Vẽ biểu đồ thanh
    plt.figure(figsize=(10, 6))
    sns.barplot(x=class_counts.index, y=class_counts.values, palette='Set2')
    plt.title('Number of Cars by Class')
    plt.xlabel('Car Class')
    plt.ylabel('Number of Cars')
    plt.show()