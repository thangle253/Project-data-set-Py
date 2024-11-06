from data_CRUD import DataProcessing
from data_cleaning import clean_duplicates, fill_missing_values
import pandas as pd

def main():
    file_path = 'cars1.csv'
    dp = DataProcessing(file_path)
    
    while True:
        # Hiển thị menu
        print("\nMenu:")  
        print("0. Thoát")
        print("1. Hiển thị dữ liệu")
        print("2. Thêm bản ghi mới")
        print("3. Cập nhật bản ghi")
        print("4. Xóa bản ghi")
        print("5. Lưu dữ liệu")
        print("6. Làm sạch dữ liệu")


        choice = input("Chọn chức năng (1-6): ")
        
        if choice == '1':
            dp.display_data()
        elif choice == '2':
            new_record = input("Nhập bản ghi mới (các trường cách nhau bởi dấu phẩy): ")
            new_record = new_record.split(',')
            expected_field_count = len(dp.get_sample_record())
            if len(new_record) == expected_field_count:
                dp.add_record(new_record)
            else:
                print(f"Số lượng trường không hợp lệ. Mong đợi {expected_field_count} trường.")
        elif choice == '3':
            index = input("Nhập vị trí cần cập nhật: ")
            if index.isdigit():
                index = int(index)
                if 0 <= index < len(dp.data):
                    updated_record = input("Nhập bản ghi mới (các trường cách nhau bởi dấu phẩy): ")
                    updated_record = updated_record.split(',')
                    dp.update_record(index, updated_record)
                else:
                    print("Vị trí không hợp lệ. Vui lòng nhập lại.")
            else:
                print("Vị trí không hợp lệ.")
        elif choice == '4':
            index = input("Nhập vị trí cần xóa: ")
            if index.isdigit():
                index = int(index)
                if 0 <= index < len(dp.data):
                    dp.delete_record(index)
                else:
                    print("Vị trí không hợp lệ. Vui lòng nhập lại.")
            else:
                print("Vị trí không hợp lệ.")
        elif choice == '5':
            dp.save_data()
        elif choice == '0':
            print("Đang thoát chương trình...")
            break
        elif choice == '6':
            print("1. Xóa các bản ghi trùng lặp")
            print("2. Điền giá trị vào các ô trống")
            cleaning_choice = input("Chọn chức năng làm sạch dữ liệu (1 hoặc 2): ")
            if cleaning_choice == '1':
                data = pd.read_csv(file_path)
                data = clean_duplicates(data)
                print("\nDữ liệu sau khi xóa bản ghi trùng lặp:")
                print(data)
                data.to_csv('cleaned_cars.csv', index=False) # Lưu dữ liệu đã xử lý vào file mới
                print("\nDữ liệu đã được lưu vào file 'cleaned_cars.csv'.")
            elif cleaning_choice == '2':
                print("\nCác cột trong DataFrame:")
                print(data.columns)
                column = input("Nhập tên cột cần điền giá trị: ")
                value = input("Nhập giá trị cần điền: ")
                data = fill_missing_values(data, column, value)
                print(f"\nDữ liệu sau khi điền giá trị '{value}' vào các ô trống của cột '{column}':")
                print(data)
                data.to_csv('cleaned_cars.csv', index=False)
                print("\nDữ liệu đã được lưu vào file 'cleaned_cars.csv'.")
        else:
            print("Chức năng không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
