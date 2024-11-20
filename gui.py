import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from PIL import Image, ImageTk  # Để xử lý hình ảnh
from data_CRUD import DataProcessing  # Import từ module data_CRUD

class CarDataGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Giao diện quản lý dữ liệu car.csv")
        self.root.geometry("570x800")
        #background
        self.root.background = ImageTk.PhotoImage(Image.open("background.jpg").resize((570, 800)))
        self.data_processor = DataProcessing('cars.csv')  # Khởi tạo với file dữ liệu
        self.current_page = 0  # Trang hiện tại
        # Khung chứa nút chức năng
        self.button_frame = ttk.Frame(root)
            
        # Tải hình ảnh cho các nút chức năng
        self.clean_icon = ImageTk.PhotoImage(Image.open("clean.png").resize((170, 50)))
        self.add_record_icon = ImageTk.PhotoImage(Image.open("add.png").resize((170, 50)))
        self.delete_record_icon = ImageTk.PhotoImage(Image.open("delete.png").resize((170, 50)))
        self.show_table_icon = ImageTk.PhotoImage(Image.open("show.png").resize((170, 50)))
        self.describe_icon = ImageTk.PhotoImage(Image.open("describe.png").resize((170, 50)))
        self.visualize_icon = ImageTk.PhotoImage(Image.open("visual.png").resize((170, 50)))
        self.sort_icon = ImageTk.PhotoImage(Image.open("sort.png").resize((170, 50)))
        self.search_icon = ImageTk.PhotoImage(Image.open("search.png").resize((170, 50)))
        self.filter_icon = ImageTk.PhotoImage(Image.open("filter.png").resize((170, 50)))

        #bg
        self.bg_label = tk.Label(self.root, image=self.root.background)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        

        self.button_frame = ttk.Frame(self.root)
        self.button_frame.place(x=50, y=310)
        tk.Button(self.button_frame, image=self.show_table_icon, command=self.show_table).grid()

        self.button_frame = ttk.Frame(self.root)
        self.button_frame.place(x=240, y=350) 
        tk.Button(self.button_frame, image=self.delete_record_icon, command=self.delete_record).grid()

        self.button_frame = ttk.Frame(self.root)
        self.button_frame.place(x=50,y=390)
        tk.Button(self.button_frame, image=self.clean_icon, command=self.clean).grid()

        self.button_frame = ttk.Frame(self.root)
        self.button_frame.place(x=240, y=430) 
        tk.Button(self.button_frame, image=self.describe_icon, command=self.describe).grid()

        self.button_frame = ttk.Frame(self.root)
        self.button_frame.place(x=50, y=470)
        tk.Button(self.button_frame, image=self.add_record_icon, command=self.add_record).grid(row=4, column=0)

                                 
        self.button_frame = ttk.Frame(self.root)
        self.button_frame.place(x=240, y=510) 
        tk.Button(self.button_frame, image=self.visualize_icon, command=self.clean).grid(row=5, column=0)


        self.button_frame = ttk.Frame(self.root)
        self.button_frame.place(x=50, y=550)
        tk.Button(self.button_frame, image=self.sort_icon, command=self.clean).grid(row=6, column=0)


        self.button_frame = ttk.Frame(self.root)
        self.button_frame.place(x=240, y=590) 
        tk.Button(self.button_frame, image=self.search_icon, command=self.clean).grid(row=7, column=0)


        self.button_frame = ttk.Frame(self.root)
        self.button_frame.place(x=50, y= 630)
        tk.Button(self.button_frame, image=self.filter_icon, command=self.clean).grid(row=8, column=0)


       


       

         
         

        # Các nút chức năng
    

    def display_data(self):
        """ Hiển thị dữ liệu của trang hiện tại trong Treeview. """
        # Xóa dữ liệu cũ trong Treeview
        for row in self.tree.get_children():
            self.tree.delete(row)
        # Lấy dữ liệu của trang hiện tại từ data_processor
        page_data = self.data_processor.display_data()
        # Thêm dữ liệu vào Treeview, bao gồm cả cột index
        for idx, row in page_data.iterrows():
            self.tree.insert('', 'end', values=(idx, *row.tolist()))  # Thêm chỉ số idx làm cột đầu tiên
        # Cập nhật nhãn trang
        total_pages = self.data_processor.get_total_pages()
        self.page_label.config(text=f"Trang: {self.data_processor.current_page + 1}/{total_pages}")
    def next_page(self):
        """ Chuyển đến trang tiếp theo và hiển thị dữ liệu. """
        self.data_processor.next_page()
        self.display_data()
    def previous_page(self):
        """ Quay về trang trước và hiển thị dữ liệu """
        self.data_processor.previous_page()
        self.display_data()

    def goto_page(self):
        """Chuyển đến trang cụ thể dựa trên số trang người dùng nhập."""
        try:
            # Lấy số trang từ Entry
            page_number = int(self.page_entry.get()) - 1 
            total_pages = self.data_processor.get_total_pages() # Tổng số trang
            # Kiểm tra tính hợp lệ của số trang
            if 0 <= page_number < total_pages:
                self.data_processor.current_page = page_number
                self.display_data()
            else:
                messagebox.showwarning("Cảnh báo", f"Số trang không hợp lệ! Vui lòng nhập từ 1 đến {total_pages}.")
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên hợp lệ!")

    def show_table(self):
        """Hiển thị bảng dữ liệu trong cửa sổ mới."""
        self.table_window = tk.Toplevel(self.root)
        self.table_window.title("Bảng dữ liệu")
        self.table_window.geometry("900x500")  
        # Lấy tên cột từ DataFrame và thêm cột "index"
        columns = ['index'] + list(self.data_processor.data.columns)
        # Treeview hiển thị dữ liệu
        style = ttk.Style()
        style.configure("Treeview.Heading",foreground="black",   font=("Times new roman", 15, "bold"))  
        self.tree = ttk.Treeview(self.table_window, columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col)  # Tiêu đề cột 
            self.tree.column(col, anchor='center', width=100)  # Căn giữa và đặt độ rộng
        self.tree.pack(fill=tk.BOTH, expand=True) # Để Treeview mở rộng theo cửa sổ
        # Khung phân trang
        pagination_frame = ttk.Frame(self.table_window)
        pagination_frame.pack(pady=5)

        tk.Button(pagination_frame, text="Trang trước", command=self.previous_page).grid(row=0, column=0, padx=5)
        self.page_label = tk.Label(pagination_frame, text=f"Trang: 1/{self.data_processor.get_total_pages()}")
        self.page_label.grid(row=0, column=1, padx=5)
        tk.Button(pagination_frame, text="Trang sau", command=self.next_page).grid(row=0, column=2, padx=5)

        # Entry và nút nhập số trang
        tk.Label(pagination_frame, text="Nhập trang:").grid(row=1, column=0, padx=5)
        self.page_entry = ttk.Entry(pagination_frame, width=5)
        self.page_entry.grid(row=1, column=1, padx=5)
        tk.Button(pagination_frame, text="Chuyển", command=self.goto_page).grid(row=1, column=2, padx=5)

        # Hiển thị dữ liệu trang đầu tiên
        self.display_data()

    def add_record(self):
        # Hiển thị popup thêm bản ghi mới
        new_window = tk.Toplevel(self.root)
        new_window.title("Thêm bản ghi mới")
        new_window.geometry("400x300")

        fields_with_options = {
            'buying': ['low', 'med', 'high', 'vhigh'],
            'maint': ['low', 'med', 'high', 'vhigh'],
            'doors': ['2', '3', '4', '5more'],
            'persons': ['2', '4', 'more'],
            'lug_boot': ['small', 'med', 'big'],
            'safety': ['low', 'med', 'high'],
            'class': ['unacc', 'acc', 'good', 'vgood']
        }
        entries = {}

        for idx, (field, options) in enumerate(fields_with_options.items()):
            ttk.Label(new_window, text=field).grid(row=idx, column=0, padx=10, pady=5)
            combobox = ttk.Combobox(new_window, values=options, state="readonly")
            combobox.grid(row=idx, column=1, padx=10, pady=5)
            combobox.set(options[0])
            entries[field] = combobox

        def save_record():
            record = [combobox.get() for combobox in entries.values()]
            if any(not val for val in record):
                messagebox.showwarning("Cảnh báo", "Vui lòng chọn tất cả các trường!")
                return
            self.data_processor.add_record(record)
            self.data_processor.save_data()
            self.data = self.data_processor.data
            messagebox.showinfo("Thông báo", "Bản ghi đã được thêm!")
            new_window.destroy()

        ttk.Button(new_window, text="Thêm", command=save_record).grid(row=len(fields_with_options), column=0, columnspan=2, pady=10)

    def delete_record(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Xóa bản ghi")
        delete_window.geometry("300x100")

        ttk.Label(delete_window, text="Nhập ID cần xóa:").grid(row=0, column=0, padx=5, pady=5)
        id_entry = ttk.Entry(delete_window)
        id_entry.grid(row=0, column=1, padx=5, pady=5)

        def delete_data():
            record_id = id_entry.get()
            if not record_id:
                messagebox.showwarning("Cảnh báo", "Vui lòng nhập ID!")
                return
            self.data_processor.delete_record(int(record_id))
            self.data_processor.save_data()
            self.data = self.data_processor.data 
            messagebox.showinfo("Thông báo", f"Bản ghi với ID {record_id} đã được xóa!")
            delete_window.destroy() # Đóng cửa sổ popup

        ttk.Button(delete_window, text="Xóa", command=delete_data).grid(row=1, column=0, columnspan=2, pady=10)
    def clean(self):
        pass
    def describe(self):
        new_window = tk.Toplevel(self.root)
        new_window.title("Mô tả dữ liệu")
        new_window.geometry("800x400")
        description = self.data_processor.describe_data() # Lấy dữ liệu mô tả từ `data_processor`
        self.display_description_as_table(new_window, description) # Hiển thị DataFrame trong Treeview
        tk.Button(new_window, text="Đóng", command=new_window.destroy).pack(pady=10) # Nút đóng cửa sổ
    def display_description_as_table(self, window, description):
        """Hiển thị DataFrame dưới dạng bảng trong Treeview."""
        # Tạo Treeview với các cột từ DataFrame
        tree = ttk.Treeview(window, columns=list(description.columns), show='headings')
        for col in description.columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=150)  # Đặt độ rộng cột
        tree.pack(fill=tk.BOTH, expand=True) 
        # Thêm dữ liệu từ DataFrame vào Treeview
        for _, row in description.iterrows():
            tree.insert('', 'end', values=row.tolist())


   

    


if __name__ == "__main__":
    root = tk.Tk()
    app = CarDataGUI(root)
    root.mainloop()
