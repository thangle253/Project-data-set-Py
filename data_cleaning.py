import pandas as pd
# Đọc dữ liệu từ tệp
file_path = 'cars (2).csv'
data = pd.read_csv(file_path)

# Hàm 1: Đếm số lượng các giá trị duy nhất trong mỗi cột
def count_unique_values(data):
    print("Đếm số lượng các giá trị duy nhất trong mỗi cột:")
    for column in data.columns:
        unique_counts = data[column].value_counts()
        print(f"\nSố lượng các giá trị trong cột '{column}':")
        print(unique_counts)

# Sử dụng hàm đếm giá trị duy nhất
count_unique_values(data)

# Hàm 2: Loại bỏ các hàng có giá trị phổ biến nhất (giá trị trung lập) trong mỗi cột
def remove_neutral_values(data):
    for column in data.columns:
        # Tìm giá trị trung lập (phổ biến nhất) trong cột
        neutral_value = data[column].mode()[0]
        # Loại bỏ các hàng có giá trị trung lập này trong cột
        data = data[data[column] != neutral_value]
        print(f"\nĐã loại bỏ giá trị trung lập '{neutral_value}' trong cột '{column}'")
    
    # In kết quả sau khi loại bỏ các giá trị trung lập
    print("\nDữ liệu sau khi loại bỏ các giá trị trung lập:")
    print(data)
    return data

# Sử dụng hàm loại bỏ giá trị trung lập
data = remove_neutral_values(data)

# Hàm 4: Đếm số lượng giá trị NULL trong mỗi cột
def count_null_values(data):
    print("\nĐếm số lượng giá trị NULL trong mỗi cột:")
    for column in data.columns:
        null_count = data[column].isnull().sum()
        print(f"Cột '{column}': {null_count} giá trị NULL")

# Sử dụng hàm đếm giá trị NULL
count_null_values(data)
# Hàm để loại bỏ các hàng chứa giá trị NULL (NaN)
def remove_null_values(data):
    # Loại bỏ tất cả các hàng có chứa giá trị NULL (NaN)
    data_cleaned = data.dropna()
    print("Đã loại bỏ các hàng chứa giá trị NULL (NaN).")
    
    # Trả về DataFrame đã được loại bỏ giá trị NULL
    return data_cleaned

data_cleaned = remove_null_values(data)


print(data_cleaned)

# Hàm để sắp xếp dữ liệu theo cột cụ thể
def sort_data(data, sort_columns, ascending_order=True):
    # Sắp xếp dữ liệu theo các cột đã chỉ định
    sorted_data = data.sort_values(by=sort_columns, ascending=ascending_order)
    return sorted_data


# Ví dụ sắp xếp theo cột 'buying' và 'class'
sort_columns = ['buying', 'class']
sorted_data = sort_data(data, sort_columns)

# In kết quả sau khi sắp xếp
print("Dữ liệu sau khi sắp xếp:")
print(sorted_data)
# Lưu dữ liệu đã xử lý vào tệp mới

output_file_path = 'cleaned_cars.csv'
data.to_csv(output_file_path, index=False)
print(f"\nDữ liệu đã được lưu vào tệp '{output_file_path}'.")
