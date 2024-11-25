# Xác định thứ tự các giá trị trong các cột
value_order = {
    'buying': {'vhigh': 4, 'high': 3, 'med': 2, 'low': 1},
    'maint': {'vhigh': 4, 'high': 3, 'med': 2, 'low': 1},
    'doors': {'5more': 5, '4': 4, '3': 3, '2': 2},
    'persons': {'more': 3, '4': 2, '2': 1},
    'lug_boot': {'big': 3, 'med': 2, 'small': 1},
    'safety': {'high': 3, 'med': 2, 'low': 1},
    'class': {'vgood': 4, 'good': 3, 'acc': 2, 'unacc': 1}
}
def convert_values(data, column):
    """
    Chuyển đổi giá trị trong cột thành số dựa trên thứ tự đã xác định.
    """
    if column not in value_order:
        raise ValueError(f"Cột '{column}' không có thứ tự giá trị được định nghĩa.")
    return data[column].map(value_order[column])
def sort_data(data, sort_column, ascending_order=True):
    """
    Sắp xếp dữ liệu theo cột và thứ tự giá trị.
    - data: DataFrame cần sắp xếp.
    - sort_column: Tên cột cần sắp xếp.
    - ascending_order: True nếu muốn sắp xếp tăng dần, False nếu giảm dần.
    - return: DataFrame đã được sắp xếp.
    """
    if sort_column not in value_order:
        raise ValueError(f"Cột '{sort_column}' không thể sắp xếp vì không có thứ tự giá trị được định nghĩa.")
    data[f'{sort_column}_numeric'] = convert_values(data, sort_column)
    sorted_data = data.sort_values(by=f'{sort_column}_numeric', ascending=ascending_order)
    sorted_data = sorted_data.drop(columns=[f'{sort_column}_numeric'])  # Xóa cột 'numeric' sau khi sắp xếp
    return sorted_data
