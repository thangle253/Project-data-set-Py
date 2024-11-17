import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd  # Import pandas library
from data_CRUD import DataProcessing  # Import từ module data_CRUD

class CarDataGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Data Management with Pagination")
        self.data_processor = DataProcessing('cars.csv')  # Khởi tạo với file dữ liệu
        self.data = self.data_processor.data  # Dữ liệu ban đầu
        self.current_page = 0  # Trang hiện tại
        self.records_per_page = 10  # Số dòng trên mỗi trang

        # Khung chính
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(pady=10, padx=10)

        # Bảng hiển thị dữ liệu
        self.tree = ttk.Treeview(self.main_frame, columns=('ID', 'buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class'), show='headings')
        for col in self.tree['columns']:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor='center')
        self.tree.pack()

        # Nút điều hướng phân trang
        self.pagination_frame = ttk.Frame(self.main_frame)
        self.pagination_frame.pack(pady=5)

        self.prev_button = ttk.Button(self.pagination_frame, text="Trang trước", command=self.previous_page)
        self.prev_button.grid(row=0, column=0, padx=5)

        self.page_label = ttk.Label(self.pagination_frame, text=f"Trang: {self.current_page + 1}")
        self.page_label.grid(row=0, column=1, padx=5)

        self.next_button = ttk.Button(self.pagination_frame, text="Trang sau", command=self.next_page)
        self.next_button.grid(row=0, column=2, padx=5)

        # Nút chức năng
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(pady=5)

        ttk.Button(self.button_frame, text="Hiển thị dữ liệu", command=self.display_data).grid(row=0, column=0, padx=5)
        ttk.Button(self.button_frame, text="Thêm bản ghi", command=self.add_record).grid(row=0, column=1, padx=5)
        ttk.Button(self.button_frame, text="Xóa bản ghi", command=self.delete_record).grid(row=0, column=2, padx=5)

        # Hiển thị trang đầu tiên
        self.display_data()

    def display_data(self):
    # Xóa dữ liệu cũ trong Treeview
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Lấy dữ liệu từ module data_CRUD
        data = self.data_processor.data

        # Kiểm tra dữ liệu không rỗng
        if isinstance(data, pd.DataFrame):
            if not data.empty:
                data = data.reset_index(drop=True)  # Đảm bảo chỉ số nhất quán
                for idx, row in data.iterrows():
                    self.tree.insert('', 'end', values=(idx, *row.values))
            else:
                messagebox.showwarning("Thông báo", "Không có dữ liệu để hiển thị!")
        else:
            messagebox.showerror("Lỗi", "Dữ liệu không đúng định dạng DataFrame.")



    def previous_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.display_data()

    def next_page(self):
        if (self.current_page + 1) * self.records_per_page < len(self.data):
            self.current_page += 1
            self.display_data()

    def add_record(self):
        # Thêm bản ghi mới
        new_window = tk.Toplevel(self.root)
        new_window.title("Thêm bản ghi mới")

        entries = {}
        fields = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
        for idx, field in enumerate(fields):
            ttk.Label(new_window, text=field).grid(row=idx, column=0, padx=5, pady=5)
            entry = ttk.Entry(new_window)
            entry.grid(row=idx, column=1, padx=5, pady=5)
            entries[field] = entry

        def save_record():
            record = [entry.get() for entry in entries.values()]
            self.data_processor.add_record(record)
            self.data_processor.save_data()
            self.data = self.data_processor.data  # Cập nhật dữ liệu sau khi thêm
            messagebox.showinfo("Thông báo", "Bản ghi đã được thêm!")
            new_window.destroy()
            self.display_data()

        ttk.Button(new_window, text="Lưu", command=save_record).grid(row=len(fields), column=0, columnspan=2, pady=10)

    def delete_record(self):
        # Xóa bản ghi
        selected_item = self.tree.selection()
        if selected_item:
            idx = self.tree.item(selected_item[0])['values'][0]
            self.data_processor.delete_record(idx)
            self.data_processor.save_data()
            self.data = self.data_processor.data  # Cập nhật dữ liệu sau khi xóa
            messagebox.showinfo("Thông báo", "Bản ghi đã được xóa!")
            self.display_data()
        else:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một bản ghi để xóa.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CarDataGUI(root)
    root.mainloop()
