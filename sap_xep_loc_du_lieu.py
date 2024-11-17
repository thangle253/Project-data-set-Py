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
def filter_data(data, column, condition):
    # Lọc dữ liệu theo điều kiện của người dùng
    filtered_data = data[data[column] == condition]
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
    
    filtered_data = sorted_data 
    # Lọc dữ liệu theo một số điều kiện
      # In ra danh sách các giá trị hợp lệ cho các cột
    print(f"Giá trị hợp lệ cho 'buying': {data['buying'].unique()}")
    print(f"Giá trị hợp lệ cho 'maint': {data['maint'].unique()}")
    print(f"Giá trị hợp lệ cho 'doors': {data['doors'].unique()}")
    print(f"Giá trị hợp lệ cho 'persons': {data['persons'].unique()}")
    print(f"Giá trị hợp lệ cho 'lug_boot': {data['lug_boot'].unique()}")
    print(f"Giá trị hợp lệ cho 'safety': {data['safety'].unique()}")
    print(f"Giá trị hợp lệ cho 'class': {data['class'].unique()}")
    
    while True:
        print("\n===== MENU =====")
        print("1. Lọc dữ liệu theo 'buying'")
        print("2. Lọc dữ liệu theo 'maint'")
        print("3. Lọc dữ liệu theo 'doors'")
        print("4. Lọc dữ liệu theo 'persons'")
        print("5. Lọc dữ liệu theo 'lug_boot'")
        print("6. Lọc dữ liệu theo 'safety'")
        print("7. Lọc dữ liệu theo 'class'")
        print("8. Thoát")

        choice = input("Chọn cột lọc (1-8): ")

        if choice == '1':
            print("\nLựa chọn giá trị cho 'buying':")
            print(", ".join(data['buying'].unique()))
            buying_choice = input("Nhập giá trị: ")
            if buying_choice in data['buying'].unique():
                filtered_data = filter_data(data, 'buying', buying_choice)
                print(f"Dữ liệu sau khi lọc theo 'buying' = {buying_choice}:")
                print(filtered_data)
            else:
                print("Giá trị không hợp lệ!")

        elif choice == '2':
            print("\nLựa chọn giá trị cho 'maint':")
            print(", ".join(data['maint'].unique()))
            maint_choice = input("Nhập giá trị: ")
            if maint_choice in data['maint'].unique():
                filtered_data = filter_data(data, 'maint', maint_choice)
                print(f"Dữ liệu sau khi lọc theo 'maint' = {maint_choice}:")
                print(filtered_data)
            else:
                print("Giá trị không hợp lệ!")

        elif choice == '3':
            print("\nLựa chọn số cửa cho 'doors':")
            print(", ".join(data['doors'].unique()))
            doors_choice = input("Nhập giá trị: ")
            if doors_choice in data['doors'].unique():
                filtered_data = filter_data(data, 'doors', doors_choice)
                print(f"Dữ liệu sau khi lọc theo 'doors' = {doors_choice}:")
                print(filtered_data)
            else:
                print("Giá trị không hợp lệ!")

        elif choice == '4':
            print("\nLựa chọn số người cho 'persons':")
            print(", ".join(data['persons'].unique()))
            persons_choice = input("Nhập giá trị: ")
            if persons_choice in data['persons'].unique():
                filtered_data = filter_data(data, 'persons', persons_choice)
                print(f"Dữ liệu sau khi lọc theo 'persons' = {persons_choice}:")
                print(filtered_data)
            else:
                print("Giá trị không hợp lệ!")

        elif choice == '5':
            print("\nLựa chọn giá trị cho 'lug_boot':")
            print(", ".join(data['lug_boot'].unique()))
            lug_boot_choice = input("Nhập giá trị: ")
            if lug_boot_choice in data['lug_boot'].unique():
                filtered_data = filter_data(data, 'lug_boot', lug_boot_choice)
                print(f"Dữ liệu sau khi lọc theo 'lug_boot' = {lug_boot_choice}:")
                print(filtered_data)
            else:
                print("Giá trị không hợp lệ!")

        elif choice == '6':
            print("\nLựa chọn giá trị cho 'safety':")
            print(", ".join(data['safety'].unique()))
            safety_choice = input("Nhập giá trị: ")
            if safety_choice in data['safety'].unique():
                filtered_data = filter_data(data, 'safety', safety_choice)
                print(f"Dữ liệu sau khi lọc theo 'safety' = {safety_choice}:")
                print(filtered_data)
            else:
                print("Giá trị không hợp lệ!")

        elif choice == '7':
            print("\nLựa chọn giá trị cho 'class':")
            print(", ".join(data['class'].unique()))
            class_choice = input("Nhập giá trị: ")
            if class_choice in data['class'].unique():
                filtered_data = filter_data(data, 'class', class_choice)
                print(f"Dữ liệu sau khi lọc theo 'class' = {class_choice}:")
                print(filtered_data)
            else:
                print("Giá trị không hợp lệ!")

        elif choice == '8':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")

    # Lưu dữ liệu đã xử lý vào tệp mới
    filtered_data.to_csv(output_file_path, index=False)
    print(f"\nDữ liệu đã được lưu vào tệp '{output_file_path}'.")

# Chạy hàm main
if __name__ == "__main__":
    main()
