import pandas as pd

def clean_duplicates(data):  # Xóa các bản ghi trùng lặp
    return data.drop_duplicates()
def fill_missing_values(data, column, value):  # Điền giá trị vào các ô trống
    return data.fillna({column: value})

def main():
    # Tải dữ liệu từ file CSV
    file_path = 'cars.csv'
    data = pd.read_csv(file_path)

    print("Dữ liệu ban đầu:")
    print(data)

    # Print the columns to debug
    print("\nCác cột trong DataFrame:")
    print(data.columns)

    # Xóa các bản ghi trùng lặp
    data = clean_duplicates(data)
    print("\nDữ liệu sau khi xóa bản ghi trùng lặp:")
    print(data)

    # Điền giá trị vào các ô trống
    print("\nCác cột trong DataFrame:")
    print(data.columns)
    column = input("Nhập tên cột cần điền giá trị: ")
    value = input("Nhập giá trị cần điền: ")
    data = fill_missing_values(data, column, value)
    print(f"\nDữ liệu sau khi điền giá trị '{value}' vào các ô trống của cột '{column}':")
    print(data)
    # Lưu dữ liệu đã xử lý vào file mới
    data.to_csv('cleaned_cars.csv', index=False)
    print("\nDữ liệu đã được lưu vào file 'cleaned_cars.csv'.")

if __name__ == "__main__":
    main()