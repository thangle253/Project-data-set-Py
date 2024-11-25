import pandas as pd

# Hàm tải dữ liệu từ tệp CSV
def load_data(file_path):
    """
    Tải dữ liệu từ tệp CSV.
    - file_path: Đường dẫn tới tệp CSV.
    - return: DataFrame chứa dữ liệu.
    """
    return pd.read_csv(file_path)

# Hàm đếm số lượng hàng trùng lặp
def count_duplicate_rows(data):
    """
    Đếm số lượng hàng trùng lặp trong DataFrame.
    - data: DataFrame cần kiểm tra.
    - return: Số lượng hàng trùng lặp và DataFrame chứa các hàng trùng lặp.
    """
    duplicate_count = data.duplicated(keep=False).sum()
    if duplicate_count > 0:
        duplicate_rows = data[data.duplicated(keep=False)]
        return duplicate_count, duplicate_rows
    else:
        return 0, pd.DataFrame()  # Trả về DataFrame rỗng nếu không có hàng trùng lặp

# Hàm loại bỏ các hàng trùng lặp hoàn toàn
def remove_duplicate_rows(data):
    """
    Loại bỏ các hàng trùng lặp trong DataFrame.
    - data: DataFrame cần xử lý.
    - return: DataFrame sau khi loại bỏ trùng lặp.
    """
    return data.drop_duplicates(keep='first')

# Hàm đếm số lượng giá trị NULL trong mỗi cột
def count_null_values(data):
    """
    Đếm số lượng giá trị NULL trong mỗi cột của DataFrame.
    - data: DataFrame cần kiểm tra.
    - return: Dictionary chứa số lượng giá trị NULL theo từng cột.
    """
    return data.isnull().sum().to_dict()

# Hàm loại bỏ các hàng chứa giá trị NULL (NaN)
def remove_null_values(data):
    """
    Loại bỏ các hàng chứa giá trị NULL (NaN).
    - data: DataFrame cần xử lý.
    - return: DataFrame sau khi loại bỏ các hàng chứa NULL.
    """
    return data.dropna()

# Hàm làm sạch dữ liệu tổng hợp
def clean_data(file_path):
    """
    Thực hiện làm sạch dữ liệu từ tệp CSV và lưu kết quả vào tệp mới.
    - file_path: Đường dẫn tới tệp CSV đầu vào.
    """
    # Tải dữ liệu từ tệp CSV
    data = load_data(file_path)

    # Đếm và xử lý trùng lặp
    duplicate_count, _ = count_duplicate_rows(data)
    if duplicate_count > 0:
        data = remove_duplicate_rows(data)

    # Đếm và xử lý giá trị NULL
    null_counts = count_null_values(data)
    if any(null_counts.values()):
        data = remove_null_values(data)

    # Lưu dữ liệu đã làm sạch vào tệp CSV
    data.to_csv(file_path, index=False)
    return data
