import csv
import pandas as pd
class DataProcessing:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()  # Tải dữ liệu từ file CSV

    
    def load_data(self):
        # Logic để tải dữ liệu từ file CSV
        data = []
        try:
            with open(self.file_path, mode='r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            print(f"File {self.file_path} không tồn tại.")
        return data
    

    def get_sample_record(self):
        # Trả về bản ghi đầu tiên từ dữ liệu để lấy số trường
        if self.data:
            return self.data[0]
        return []

    def display_data(self):
        # Hiển thị dữ liệu
        if self.data:
            df = pd.DataFrame(self.data)
            print(df)
        else:
            print("Không có dữ liệu để hiển thị.")

    def add_record(self, record):
        # Thêm bản ghi
        self.data.append(record)
        print("Bản ghi đã được thêm.")

    def update_record(self, index, record):
        # Cập nhật bản ghi
        if 0 <= index < len(self.data):
            self.data[index] = record
            print("Bản ghi đã được cập nhật.")
        else:
            print("Vị trí không hợp lệ.")

    def delete_record(self, index):
        # Xóa bản ghi
        if 0 <= index < len(self.data):
            self.data.pop(index)
            print("Bản ghi đã được xóa.")
        else:
            print("Vị trí không hợp lệ.")

    def save_data(self):
        # Lưu dữ liệu vào file CSV
        with open(self.file_path, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.data)
        print("Dữ liệu đã được lưu thành công.")


