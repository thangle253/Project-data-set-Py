import pandas as pd

def filter_data(data, column, condition):
    """
    Lọc dữ liệu theo cột và giá trị cụ thể.
    - data: DataFrame
    - column: Tên cột cần lọc
    - condition: Giá trị điều kiện
    """
    return data[data[column] == condition] 
# Hàm lấy danh sách các giá trị duy nhất trong một cột
def get_unique_values(data, column):
    """
    Lấy danh sách giá trị duy nhất của một cột.
    - data: DataFrame
    - column: Tên cột
    """
    return data[column].unique().tolist()
    
def search_data(data, id_column, id_value):
    """
    Tìm kiếm bản ghi dựa trên ID.
    - data: DataFrame cần tìm kiếm.
    - id_column: Tên cột chứa ID.
    - id_value: Giá trị ID cần tìm.
    - return: DataFrame chứa kết quả tìm kiếm hoặc thông báo nếu không tìm thấy.
    """
    if 'index' not in data.columns:
        data = data.reset_index()  # Thêm cột 'index' từ chỉ số của DataFrame
    if id_column not in data.columns: 
        raise ValueError(f"Cột '{id_column}' không tồn tại trong dữ liệu.")
    result = data[data[id_column] == id_value]
    
    if result.empty:
        return f"Không tìm thấy bản ghi với {id_column} = {id_value}."
    return result

