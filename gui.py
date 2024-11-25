import tkinter as tk
from tkinter import ttk, messagebox 
import pandas as pd
from PIL import Image, ImageTk  # Để xử lý hình ảnh
from data_CRUD import DataProcessing  # Import từ module data_CRUD
from data_cleaning import clean_data
from loc_timkiem import filter_data, get_unique_values, search_data
from sap_xep_du_lieu import sort_data
from visual_data import BieuDo1, BieuDo2, BieuDo3, BieuDo4, BieuDo5, BieuDo6

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
        self.update_icon = ImageTk.PhotoImage(Image.open("update.png").resize((170, 50)))

        # Background
        self.bg_label = tk.Label(self.root, image=self.root.background)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Tạo các nút chức năng
        self.button_frame = tk.Frame(self.root)
        self.button_frame.place(x=50, y=310)
        tk.Button(self.button_frame, image=self.show_table_icon, command=self.show_table).grid()

        self.button_frame = tk.Frame(self.root)
        self.button_frame.place(x=240, y=350) 
        tk.Button(self.button_frame, image=self.delete_record_icon, command=self.delete_record).grid()

        self.button_frame = tk.Frame(self.root)
        self.button_frame.place(x=50,y=390)
        tk.Button(self.button_frame, image=self.clean_icon, command=self.clean).grid()

        self.button_frame = tk.Frame(self.root)
        self.button_frame.place(x=240, y=430) 
        tk.Button(self.button_frame, image=self.describe_icon, command=self.describe).grid()

        self.button_frame = tk.Frame(self.root)
        self.button_frame.place(x=50, y=470)
        tk.Button(self.button_frame, image=self.add_record_icon, command=self.add_record).grid(row=4, column=0)

                                 
        self.button_frame = tk.Frame(self.root)
        self.button_frame.place(x=240, y=510) 
        tk.Button(self.button_frame, image=self.visualize_icon, command=self.visualize).grid(row=5, column=0)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.place(x=50, y=550)
        tk.Button(self.button_frame, image=self.sort_icon, command=self.sort).grid(row=6, column=0)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.place(x=240, y=590) 
        tk.Button(self.button_frame, image=self.search_icon, command=self.search).grid(row=7, column=0)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.place(x=50, y= 630)
        tk.Button(self.button_frame, image=self.filter_icon, command=self.filter).grid(row=8, column=0)
        
        self.button_frame = tk.Frame(self.root)
        self.button_frame.place(x=240, y= 670)
        tk.Button(self.button_frame, image=self.update_icon, command=self.update).grid(row=8, column=0)

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
    def show_table(self,):
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
                messagebox.showwarning("Cảnh báo", "Vui lòng chọn Không lọc các trường!")
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
        """Làm sạch dữ liệu: Loại bỏ các hàng trùng lặp và các giá trị NULL."""
        try:
            # Gọi hàm làm sạch từ module
            cleaned_data = clean_data("cars.csv")
            # Cập nhật lại dữ liệu đã làm sạch vào data_processor
            self.data_processor.data = cleaned_data
            messagebox.showinfo("Thành công", "Dữ liệu đã được làm sạch thành công!")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi làm sạch dữ liệu: {e}")

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
    
    def filter(self):
        """Hiển thị popup để người dùng chọn giá trị lọc cho từng cột."""
        filter_window = tk.Toplevel(self.root)
        filter_window.title("Lọc dữ liệu")
        # Danh sách các cột cần lọc
        columns = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
        entries = {}  # Lưu trữ các Combobox

        # Tạo giao diện chọn giá trị cho từng cột
        for idx, column in enumerate(columns):
            tk.Label(filter_window, text=f"Lọc theo '{column}':").grid(row=idx, column=0)
            # Lấy các giá trị duy nhất từ cột
            unique_values = get_unique_values(self.data_processor.data, column)
            combobox = ttk.Combobox(filter_window, values=['(Không lọc)'] + unique_values, state="readonly")  # Thêm "(Không lọc)"
            combobox.grid(row=idx, column=1)
            combobox.set('(Không lọc)')  # Đặt giá trị mặc định là "(Không lọc)"
            entries[column] = combobox

        # Nút thực hiện lọc
        def apply_filter():

            # Áp dụng lọc tuần tự
            for column, combobox in entries.items():
                value = combobox.get() # Lấy giá trị từ Combobox
                if value != '(Không lọc)':  # Chỉ lọc nếu không phải "(Không lọc)"
                    self.data_processor.data = filter_data(self.data_processor.data, column, value)
            if self.data_processor.data.empty:
                messagebox.showwarning("Cảnh báo", "Không tìm thấy dữ liệu phù hợp!")
            else:
                self.show_table()  
            # Reset về dữ liệu gốc sau khi thực hiện lọc
            self.data_processor.data = pd.read_csv('cars.csv') 
            filter_window.destroy() # Đóng cửa sổ popup


            
        # Nút áp dụng lọc
        tk.Button(filter_window, text="Lọc", command=apply_filter).grid(row=len(columns), column=0, columnspan=2, pady=20)

    def update(self):
        """Cập nhật giá trị trong bản ghi dựa trên ID."""
        update_window = tk.Toplevel(self.root)
        update_window.title("Cập nhật bản ghi")

        tk.Label(update_window, text="Nhập ID cần cập nhật:").grid(padx=5, pady=5)
        id_entry = ttk.Entry(update_window)
        id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Tạo Combobox cho mỗi thuộc tính (cột trong DataFrame)
        attribute_entries = {}
        for idx, column in enumerate(self.data_processor.data.columns):
            tk.Label(update_window, text=f"{column}:").grid(row=idx + 1, column=0, padx=10, pady=5)
            unique_values = self.data_processor.data[column].dropna().unique().tolist()  # Lấy giá trị duy nhất không NULL
            combobox = ttk.Combobox(update_window, values=['(Không cập nhật)'] + unique_values, state="readonly", width=30)
            combobox.grid(row=idx + 1, column=1, padx=10, pady=5)
            combobox.set('(Không cập nhật)')  # Mặc định là "Không cập nhật"
            attribute_entries[column] = combobox
        def apply_update():
            try:
                # Lấy ID từ Entry
                record_id = int(id_entry.get().strip())
                # Kiểm tra ID có tồn tại không
                if record_id < 0 or record_id >= len(self.data_processor.data):
                    messagebox.showerror("Lỗi", f"ID {record_id} không tồn tại.")
                    return
                # Tạo dictionary cho các thay đổi
                updates = {col: combo.get() for col, combo in attribute_entries.items() if combo.get() != '(Không cập nhật)'}
                # Gọi module DataProcessing để cập nhật
                if updates:
                    self.data_processor.update_record(record_id, updates)
                    self.data_processor.save_data()
                    messagebox.showinfo("Thành công", f"Đã cập nhật ID {record_id}:\n{updates}")
                    update_window.destroy()
                else:
                    messagebox.showinfo("Thông báo", "Không có thay đổi nào được thực hiện.")
            except ValueError:
                messagebox.showerror("Lỗi", "Vui lòng nhập ID hợp lệ.")
            except Exception as e:
                messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")
        ttk.Button(update_window, text="Cập nhật", command=apply_update).grid(row=len(self.data_processor.data.columns) + 1, column=0, columnspan=2, pady=20)
    
    def sort(self):
        """Hiển thị popup để người dùng chọn cột và thứ tự sắp xếp."""
        sort_window = tk.Toplevel(self.root)
        sort_window.title("Sắp xếp dữ liệu")
        # Danh sách các cột có thể sắp xếp
        columns = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
        # Tạo Combobox để chọn cột
        tk.Label(sort_window, text="Chọn cột để sắp xếp:").grid(row=0, column=0)
        column_combobox = ttk.Combobox(sort_window, values=columns, state="readonly") 
        column_combobox.grid(row=0, column=1, padx=10, pady=10) # Đặt Combobox vào cửa sổ
        column_combobox.set(columns[0])  # Giá trị mặc định là cột đầu tiên

        # Tạo Combobox để chọn thứ tự sắp xếp
        tk.Label(sort_window, text="Thứ tự sắp xếp:").grid(row=1, column=00)
        order_combobox = ttk.Combobox(sort_window, values=["Tăng dần", "Giảm dần"], state="readonly")
        order_combobox.grid(row=1, column=1, padx=10, pady=10)
        order_combobox.set("Tăng dần")  # Giá trị mặc định là "Tăng dần"

        def apply_sort():
            try:
                # Lấy cột và thứ tự sắp xếp từ Combobox
                sort_column = column_combobox.get()
                ascending_order = order_combobox.get() == "Tăng dần"
                # Thực hiện sắp xếp
                self.data_processor.data = sort_data(self.data_processor.data, sort_column, ascending_order)
                self.show_table() # Hiển thị dữ liệu đã sắp xếp
                # Thông báo thành công
                messagebox.showinfo("Thành công", f"Dữ liệu đã được sắp xếp theo cột '{sort_column}' ({'Tăng dần' if ascending_order else 'Giảm dần'}).")
                sort_window.destroy()
            except Exception as e:
                messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi sắp xếp dữ liệu: {e}")
        # Nút áp dụng sắp xếp
        tk.Button(sort_window, text="Sắp xếp", command=apply_sort).grid(row=2, column=0, columnspan=2,)

    def search(self):
        """Tìm kiếm bản ghi theo ID và hiển thị kết quả."""
        search_window = tk.Toplevel(self.root)
        search_window.title("Tìm kiếm bản ghi")

        tk.Label(search_window, text="Nhập ID cần tìm:").pack(pady=5)
        id_entry = tk.Entry(search_window)
        id_entry.pack(pady=5,padx = 5)
        def perform_search():
            search_id = id_entry.get().strip() # Lấy ID từ Entry, strip() để loại bỏ khoảng trắng
            if not search_id.isdigit():
                messagebox.showerror("Lỗi", "ID phải là số nguyên!")
                return
            search_id = int(search_id)
            result = search_data(self.data_processor.data, 'index', search_id) 
            print(result)
            if isinstance(result, pd.DataFrame) and not result.empty: 
                # Định dạng chi tiết bản ghi trực tiếp từ hàng duy nhất
                record_details = "\n".join([f"{col}: {val}" for col, val in result.iloc[0].items()])  
                messagebox.showinfo("Kết quả", f"Đã tìm thấy bản ghi:\n\n{record_details}")
            else:
                messagebox.showinfo("Không tìm thấy", f"Không có bản ghi với ID: {search_id}")
            search_window.destroy()
        tk.Button(search_window, text="Tìm kiếm", command=perform_search).pack()

    def visualize(self):
        """Hiển thị popup để người dùng chọn loại biểu đồ trực quan."""
        visualize_window = tk.Toplevel(self.root)
        visualize_window.title("Trực quan hóa dữ liệu")
        # Loại biểu đồ được định nghĩa trước
        chart_types = {
            "Phân tích sự phân phối các biến trong đánh giá ô tô": BieuDo1,
            "Phân tích ảnh hưởng của các thuộc tính xe hơi đến đánh giá chất lượng": BieuDo2,
            "Phân tích mối quan hệ giữa giá mua và mức độ an toàn của xe": BieuDo3,
            "Sự phân bố các lớp xe dựa trên giá mua và chi phí bảo dưỡng": BieuDo4,
            "Mối quan hệ giữa các đặc điểm khác nhau của xe và cách chúng phân bố theo các lớp xe": BieuDo5,
            "thống kê số lượng xe dựa trên mức đánh giá": BieuDo6
        }
        # Combobox chọn loại biểu đồ
        tk.Label(visualize_window, text="Chọn loại biểu đồ:").pack(pady=5)
        chart_combobox = ttk.Combobox(visualize_window, values=list(chart_types.keys()), state="readonly",width=60)
        chart_combobox.pack(padx=10)
        chart_combobox.set(list(chart_types.keys())[0])
        def apply_visualize():
            """Thực hiện trực quan hóa dữ liệu."""
            chart_type = chart_combobox.get()
            try:
                if chart_type in chart_types:
                    chart_types[chart_type]()  # Gọi hàm biểu đồ tương ứng
                    visualize_window.destroy()
            except Exception as e:
                messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi trực quan hóa dữ liệu: {e}")
        tk.Button(visualize_window, text="Áp dụng", command=apply_visualize).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = CarDataGUI(root)
    root.mainloop()
