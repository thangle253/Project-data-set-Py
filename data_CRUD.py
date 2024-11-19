import pandas as pd

class DataProcessing:
    def __init__(self, file_path, records_per_page=20):
        self.file_path = file_path
        self.data = self.load_data()  # Tải dữ liệu từ file CSV dưới dạng DataFrame
        self.records_per_page = records_per_page  # Số dòng hiển thị trên mỗi trang
        self.current_page = 0  # Trang hiện tại

    def load_data(self):
        try:
            # Tải dữ liệu từ file CSV dưới dạng DataFrame
            data = pd.read_csv(self.file_path)
            data.columns = data.columns.str.strip().str.replace("'", "")  # Loại bỏ khoảng trắng và dấu nháy đơn
        except FileNotFoundError:
            print(f"File {self.file_path} không tồn tại.")
            data = pd.DataFrame()  # Trả về DataFrame rỗng nếu không tìm thấy file
        return data

    def display_data(self, page=None):
        """ Hiển thị dữ liệu theo trang.
        :param page: Số thứ tự trang (0-indexed). Nếu không được cung cấp, hiển thị trang hiện tại.
        :return: DataFrame chứa dữ liệu của trang yêu cầu
        """
        if page is not None:
            self.current_page = page

        # Tính toán chỉ số bắt đầu và kết thúc
        start_index = self.current_page * self.records_per_page
        end_index = start_index + self.records_per_page

        # Lấy dữ liệu cho trang hiện tại
        page_data = self.data.iloc[start_index:end_index]

        if page_data.empty:
            print("Không có dữ liệu để hiển thị.")
        else:
            print(page_data)

        return page_data

    def describe_data(self):
        """Trả về thông tin mô tả dữ liệu từ file CSV dưới dạng DataFrame."""
        try:
            # Tạo DataFrame mô tả dữ liệu
            description = self.data.describe(include='all').transpose()  # Transpose để dễ đọc
            description.reset_index(inplace=True)  # Chuyển index thành cột 'index'
            description.rename(columns={'index': 'Thuộc tính'}, inplace=True)  # Đổi tên cột index

            return description
        except Exception as e:
            print(f"Lỗi khi mô tả dữ liệu: {e}")
            # Nếu gặp lỗi, trả về DataFrame với thông báo lỗi
            return pd.DataFrame({'Lỗi': [str(e)]})

    def get_total_pages(self):
        """
        Tính tổng số trang dựa trên số dòng trên mỗi trang.
        :return: Tổng số trang
        """
        total_records = len(self.data)
        total_pages = (total_records // self.records_per_page) + (1 if total_records % self.records_per_page > 0 else 0)
        return total_pages

    def next_page(self):
        """
        Chuyển đến trang tiếp theo.
        :return: DataFrame chứa dữ liệu trang tiếp theo
        """
        if self.current_page + 1 < self.get_total_pages():
            self.current_page += 1
        else:
            print("Đây là trang cuối cùng.")
        return self.display_data()

    def previous_page(self):
        """
        Quay về trang trước.
        :return: DataFrame chứa dữ liệu trang trước
        """
        if self.current_page > 0:
            self.current_page -= 1
        else:
            print("Đây là trang đầu tiên.")
        return self.display_data()

    def reset_pagination(self):
        """
        Đặt lại trang hiện tại về trang đầu tiên.
        """
        self.current_page = 0
        return self.display_data()

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
