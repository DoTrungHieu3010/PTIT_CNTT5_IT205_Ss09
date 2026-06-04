# Input/Output
# Input: lựa chọn menu, mã đơn hàng nhập từ bàn phím 
# Output: danh sách đơn hàng hiển thị, thông báo thêm/xóa thành công hoặc lỗi, thông báo thoát chương trình.

# Giải pháp
# Dùng vòng lặp while True để hiển thị menu liên tục
# Dùng input() để nhận lựa chọn
# Kiểm tra hợp lệ: nếu không phải số 1–4 thì báo lỗi
# Chức năng 1: duyệt danh sách bằng enumerate() để in ra
# Chức năng 2: chuẩn hóa mã đơn hàng (strip(), upper()), thêm bằng append()
# Chức năng 3: chuẩn hóa mã nhập vào, kiểm tra bằng in, nếu có thì remove(), nếu không thì báo lỗi
# Chức năng 4: break để thoát

# order_list = ["GE001", "GE002", "GE003"]
# while True:
#     in ra menu
#     choice = input()
#     if choice == "1":
#         nếu order_list rỗng → in "Danh sách trống"
#         ngược lại → in từng đơn hàng với số thứ tự
#     elif choice == "2":
#         nhập mã mới, strip, upper
#         append vào order_list
#     elif choice == "3":
#         nhập mã cần xóa, strip, upper
#         nếu mã trong order_list → remove
#         ngược lại → in "Không tìm thấy"
#     elif choice == "4":
#         in "Thoát chương trình"
#         break
#     else:
#         in "Lựa chọn không hợp lệ"


order_list = ["GE001", "GE002", "GE003"]

while True:
    print("""
        ===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====
        1. Hiển thị danh sách đơn hàng
        2. Thêm đơn hàng mới
        3. Xóa đơn hàng theo mã
        4. Thoát chương trình
        """)
    choice = int(input("Nhập lựa chọn của bạn: "))
    match choice:
        case 1:
            if len(order_list) == 0:
                print("Đơn hàng đang trống")
            else:
                print("Danh sách đơn hàng hiện tại: ")
                for i, order in enumerate(order_list, start= 1):
                    print(f"{i}. {order}")
        case 2:
            new_order = input("Nhập mã đơn hàng mới: ").strip().upper()
            order_list.append(new_order)
        case 3:
            delete_order = input("Nhập mã đơn hàng cần xóa: ").strip().upper()
            if delete_order in order_list:
                order_list.remove(delete_order)
            else:
                print("Không tìm thấy đơn hàng cần xóa")
        case 4:
            print("Thoát chương trình")
            break
        case _ :
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại")
            
            
            
            
            
            
            
            
            
