import pandas as pd

file_path = 'cars.csv'

# Hàm tải dữ liệu từ tệp CSV
def load_data(file_path):
    return pd.read_csv(file_path)

# Hàm sắp xếp dữ liệu theo cột cụ thể
def sort_data(data, sort_columns, ascending_order=True):
    # Sắp xếp dữ liệu theo các cột đã chỉ định
    sorted_data = data.sort_values(by=sort_columns, ascending=ascending_order)
    return sorted_data

# Hàm lọc dữ liệu theo điều kiện cụ thể
def filter_data(data, filter_conditions):
    # Lọc dữ liệu theo điều kiện
    filtered_data = data
    for column, condition in filter_conditions.items():
        filtered_data = filtered_data[filtered_data[column].apply(condition)]
    return filtered_data

def main():
    file_path = 'cars.csv'  # Đảm bảo tên tệp chính xác
    output_file_path = 'car_new.csv'
    
    # Tải dữ liệu từ tệp CSV
    data = load_data(file_path)
    
    # Sắp xếp dữ liệu theo cột 'buying' và 'class'
    sort_columns = ['buying', 'class']
    sorted_data = sort_data(data, sort_columns)

    # In dữ liệu đã sắp xếp
    print("Dữ liệu sau khi sắp xếp theo cột 'buying' và 'class':")
    print(sorted_data)

    # Lọc dữ liệu theo một số điều kiện
    filter_conditions = {
        'buying': lambda x: x == 'low',  # Lọc những xe có giá 'low'
        'class': lambda x: x == 'unacc'  # Lọc những xe thuộc lớp 'unacc'
    }
    filtered_data = filter_data(sorted_data, filter_conditions)

    # In dữ liệu đã lọc
    print("\nDữ liệu sau khi lọc:")
    print(filtered_data)

    # Lưu dữ liệu đã xử lý vào tệp mới
    filtered_data.to_csv(output_file_path, index=False)
    print(f"\nDữ liệu đã được lưu vào tệp '{output_file_path}'.")

# Chạy hàm main
if __name__ == "__main__":
    main()
