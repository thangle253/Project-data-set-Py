import pandas as pd
file_path = 'car (2).csv'
def load_data(file_path):
    return pd.read_csv(file_path)

# Hàm đếm các giá trị trùng lặp theo hàng
def count_duplicate_values(data):
    print("Đếm số lượng các giá trị trùng lặp theo từng hàng:")
    for index, row in data.iterrows():
        # Đếm số lần xuất hiện của mỗi giá trị trong hàng
        value_counts = row.value_counts()
        # Lọc ra các giá trị trùng lặp (xuất hiện nhiều hơn một lần)
        duplicates = value_counts[value_counts > 1]
        
        # In kết quả cho hàng hiện tại
        if not duplicates.empty:
            print(f"\nCác giá trị trùng lặp trong hàng {index}:")
            print(duplicates)
        else:
            print(f"\nKhông có giá trị trùng lặp trong hàng {index}")

# Hàm loại bỏ các giá trị trùng lặp theo hàng
def remove_duplicate_values(data):
    modified_data = data.copy()  # Tạo bản sao để tránh thay đổi trực tiếp DataFrame gốc
    
    for index, row in modified_data.iterrows():
        # Đếm số lần xuất hiện của mỗi giá trị trong hàng
        value_counts = row.value_counts()
        # Tìm các giá trị trùng lặp (xuất hiện nhiều hơn một lần)
        duplicate_values = value_counts[value_counts > 1].index
        # Thay thế các giá trị trùng lặp bằng NaN
        modified_data.loc[index] = row.apply(lambda x: x if x not in duplicate_values else pd.NA)
        print(f"\nĐã loại bỏ các giá trị trùng lặp trong hàng {index}")
    
    # In kết quả sau khi loại bỏ các giá trị trùng lặp
    print("\nDữ liệu sau khi loại bỏ các giá trị trùng lặp theo từng hàng:")
    print(modified_data)
    return modified_data


# Hàm  Đếm số lượng giá trị NULL trong mỗi cột
def count_null_values(data):
    print("\nĐếm số lượng giá trị NULL trong mỗi cột:")
    for column in data.columns:
        null_count = data[column].isnull().sum()
        print(f"Cột '{column}': {null_count} giá trị NULL")


# Hàm để loại bỏ các hàng chứa giá trị NULL (NaN)
def remove_null_values(data):
    # Loại bỏ tất cả các hàng có chứa giá trị NULL (NaN)
    data_cleaned = data.dropna()
    print("Đã loại bỏ các hàng chứa giá trị NULL (NaN).")
    return data_cleaned

# Hàm để sắp xếp dữ liệu theo cột cụ thể
def sort_data(data, sort_columns, ascending_order=True):
    # Sắp xếp dữ liệu theo các cột đã chỉ định
    sorted_data = data.sort_values(by=sort_columns, ascending=ascending_order)
    return sorted_data

# Hàm main để chạy tất cả các bước
def main():
    file_path = 'cars (2).csv'
    output_file_path = 'cleaned_cars.csv'

   
    data = load_data(file_path)

    #Đếm số lượng giá trị trùng lập
    count_duplicate_values(data)

    #Loại bỏ giá trị trung lập
    data = remove_duplicate_values(data)

    #Đếm giá trị NULL
    count_null_values(data)

    #Loại bỏ các hàng chứa giá trị NULL
    data_cleaned = remove_null_values(data)

    #Sắp xếp dữ liệu theo cột 'buying' và 'class'
    sort_columns = ['buying', 'class']
    sorted_data = sort_data(data_cleaned, sort_columns)

    print("Dữ liệu sau khi sắp xếp:")
    print(sorted_data)

    #Lưu dữ liệu đã xử lý vào tệp mới
    sorted_data.to_csv(output_file_path, index=False)
    print(f"\nDữ liệu đã được lưu vào tệp '{output_file_path}'.")

# Chạy hàm main
if __name__ == "__main__":
    main()
