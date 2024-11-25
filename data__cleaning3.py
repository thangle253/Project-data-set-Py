import pandas as pd

file_path = 'cars (2).csv'

# Hàm tải dữ liệu từ tệp CSV
def load_data(file_path):
    return pd.read_csv(file_path)

# Hàm đếm số lượng hàng trùng lặp
def count_duplicate_rows(data):
    duplicate_count = data.duplicated(keep=False).sum()
    print(f"\nSố lượng các hàng trùng lặp: {duplicate_count}")

    if duplicate_count > 0:
        duplicate_rows = data[data.duplicated(keep=False)]
        print("Các hàng trùng lặp:")
        print(duplicate_rows)
    else:
        print("Không có hàng trùng lặp nào.")

# Hàm loại bỏ các hàng trùng lặp hoàn toàn
def remove_duplicate_rows(data):
    modified_data = data.drop_duplicates(keep='first')
    print("\nDữ liệu sau khi loại bỏ các hàng trùng lặp:")
    print(modified_data)
    return modified_data

# Hàm đếm số lượng giá trị NULL trong mỗi cột
def count_null_values(data):
    print("\nĐếm số lượng giá trị NULL trong mỗi cột:")
    for column in data.columns:  
        null_count = data[column].isnull().sum() 
        print(f"Cột '{column}': {null_count} giá trị NULL")

    # Chỉ ra các hàng có giá trị NULL
    print("\nDanh sách các hàng có giá trị NULL:")
    null_rows = data[data.isnull().any(axis=1)] 
    print(null_rows)

# Hàm loại bỏ các hàng chứa giá trị NULL (NaN)
def remove_null_values(data):
    data_cleaned = data.dropna()
    print("Đã loại bỏ các hàng chứa giá trị NULL (NaN).")
    return data_cleaned


def main():
    file_path = 'cars (2).csv'
    output_file_path = 'data_cleaning.csv'

    data = load_data(file_path)

    # Đếm số lượng giá trị trùng lặp
    count_duplicate_rows(data)

    # Loại bỏ giá trị trùng lặp
    modified_data = remove_duplicate_rows(data)

    # Đếm số lượng giá trị NULL
    count_null_values(modified_data)

    # Loại bỏ các hàng chứa giá trị NULL
    data_cleaned = remove_null_values(modified_data)

    # Lưu dữ liệu đã xử lý vào tệp mới
    data_cleaned.to_csv(output_file_path, index=False)
    print(f"\nDữ liệu đã được lưu vào tệp '{output_file_path}'.")

# Chạy hàm main
if __name__ == "__main__":
    main()
