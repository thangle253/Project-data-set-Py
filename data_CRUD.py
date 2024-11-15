import pandas as pd

class DataProcessing:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()  # Tải dữ liệu từ file CSV dưới dạng DataFrame

    def load_data(self):
        try:
            # Tải dữ liệu từ file CSV dưới dạng DataFrame
            data = pd.read_csv(self.file_path)
        except FileNotFoundError:
            print(f"File {self.file_path} không tồn tại.")
            data = pd.DataFrame()  # Trả về DataFrame rỗng nếu không tìm thấy file
        return data

    def display_data(self):
        # Hiển thị dữ liệu dưới dạng DataFrame
        print(self.data)

    def describe_data(self):
        # Đọc dữ liệu từ tệp cars.csv
        cars_df = pd.read_csv(self.file_path)
        print( cars_df.describe(include='all'))
       

    def add_record(self, record):
        # Thêm bản ghi vào DataFrame
        record_df = pd.DataFrame([record], columns=self.data.columns)
        self.data = pd.concat([self.data, record_df], ignore_index=True)
        print("Bản ghi đã được thêm.")

    def update_record(self, index, record):
        # Cập nhật bản ghi
        if 0 <= index < len(self.data):
            for key, value in record.items():
                if key in self.data.columns:
                    self.data.at[index, key] = value
            print("Bản ghi đã được cập nhật.")
        else:
            print("Vị trí không hợp lệ.")

    def delete_record(self, index):
        # Xóa bản ghi
        if 0 <= index < len(self.data):
            self.data = self.data.drop(index).reset_index(drop=True)
            print("Bản ghi đã được xóa.")
        else:
            print("Vị trí không hợp lệ.")

    def save_data(self):
        # Lưu dữ liệu vào file CSV
        self.data.to_csv(self.file_path, index=False)
        print("Dữ liệu đã được lưu thành công.")


