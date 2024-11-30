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
            "Thống kê số lượng xe dựa trên mức đánh giá": BieuDo6
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
