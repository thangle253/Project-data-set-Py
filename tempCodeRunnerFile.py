import pandas as pd

# Xác định thứ tự các giá trị trong các cột
value_order = {
    'buying': {'v-high': 4, 'high': 3, 'med': 2, 'low': 1},
    'maint': {'v-high': 4, 'high': 3, 'med': 2, 'low': 1},
    'doors': {'5-more': 5, '4': 4, '3': 3, '2': 2},
    'persons': {'more': 3, '4': 2, '2': 1},
    'lug_boot': {'big': 3, 'med': 2, 'small': 1},
    'safety': {'high': 3, 'med': 2, 'low': 1},
    'class': {'vgood': 4, 'good': 3, 'acc': 2, 'unacc': 1}
}

# Hàm chuyển đổi giá trị thành số dựa trên thứ tự đã xác định
def convert_values(data, column):
    return data[column].map(value_order[column])

# Hàm sắp xếp dữ liệu theo cột và thứ tự giá trị
def sort_data(data, sort_column, ascending_order=True):
    # Chuyển đổi giá trị trong cột thành số để sắp xếp
    data[f'{sort_column}_numeric'] = convert_values(data, sort_column)
    
    # Sắp xếp dữ liệu theo cột đã chỉ định
    sorted_data = data.sort_values(by=f'{sort_column}_numeric', ascending=ascending_order)
    
    # Xóa cột 'numeric' sau khi sắp xếp
    sorted_data = sorted_data.drop(columns=[f'{sort_column}_numeric'])
    
    return sorted_data

def main():
    # Tải dữ liệu từ tệp CSV
    file_path = 'cars.csv'  # Đảm bảo bạn có tệp cars.csv đúng định dạng
    data = pd.read_csv(file_path)
    
    # In ra các cột có sẵn trong dữ liệu để người dùng chọn
    print(f"Danh sách các cột có sẵn: {', '.join(data.columns)}")

    # Cho người dùng chọn cột sắp xếp
    sort_column = input(f"\nChọn cột muốn sắp xếp (một trong các cột trên): ")

    # Kiểm tra cột có hợp lệ hay không
    if sort_column not in data.columns:
        print("Cột không hợp lệ!")
        return
    
    # Cho người dùng chọn thứ tự sắp xếp
    order_choice = input("Chọn thứ tự sắp xếp (1: Tăng dần, 2: Giảm dần):")

    if order_choice == '1':
        ascending_order = True
    elif order_choice == '2':
        ascending_order = False
    else:
        print("Lựa chọn không hợp lệ, mặc định sắp xếp tăng dần.")
        ascending_order = True
    
    # Sắp xếp dữ liệu
    sorted_data = sort_data(data, sort_column, ascending_order)
    
    # In ra kết quả sau khi sắp xếp
    print(f"\nDữ liệu sau khi sắp xếp theo cột '{sort_column}' (Thứ tự: {'Tăng dần' if ascending_order else 'Giảm dần'}):")
    print(sorted_data)

    # Lưu dữ liệu đã sắp xếp vào tệp mới
    output_file_path = 'sorted_cars.csv'
    sorted_data.to_csv(output_file_path, index=False)
    print(f"\nDữ liệu đã được lưu vào tệp '{output_file_path}'.")

# Chạy hàm main
if __name__ == "__main__":
    main()
