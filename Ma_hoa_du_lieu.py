import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Hàm tải dữ liệu từ tệp CSV
file_path = 'cars.csv'
# Hàm tải dữ liệu từ tệp CSV
def load_data(file_path):
    return pd.read_csv(file_path)
# Hàm kiểm tra các cột cần mã hóa
def validate_columns(data, columns_to_encode):
    missing_columns = [col for col in columns_to_encode if col not in data.columns]
    if missing_columns:
        print(f"Các cột sau không tồn tại trong dữ liệu: {missing_columns}")
        raise KeyError("Không thể mã hóa các cột không tồn tại trong dữ liệu.")
    print("Tất cả các cột cần mã hóa đều có trong dữ liệu.")

# Hàm mã hóa dữ liệu
def encode_columns(data, columns_to_encode):
    encoder = LabelEncoder()
    for column in columns_to_encode:
        data[column] = encoder.fit_transform(data[column])
        print(f"Đã mã hóa cột: {column}")
    return data

# Hàm lưu dữ liệu vào tệp CSV
def save_data(data, output_file):
    data.to_csv(output_file, index=False)
    print(f"Dữ liệu đã được lưu vào tệp: {output_file}")

# Hàm main
def main():
    # Đường dẫn tới tệp dữ liệu và tệp xuất ra
    file_path = 'cars.csv'
    output_file = 'encoded_cars.csv'

    # Danh sách các cột cần mã hóa
    columns_to_encode = ['buying', 'maint', 'lug_boot', 'safety']

    # Gọi các hàm xử lý dữ liệu
    data = load_data(file_path)  # Tải dữ liệu
    print("Dữ liệu ban đầu:")
    print(data.head())

    validate_columns(data, columns_to_encode)  # Kiểm tra cột
    data = encode_columns(data, columns_to_encode)  # Mã hóa dữ liệu

    print("\nDữ liệu sau khi mã hóa:")
    print(data.head())

    save_data(data, output_file)  # Lưu dữ liệu

# Chạy chương trình
if __name__ == "__main__":
    main()
