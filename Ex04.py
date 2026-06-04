# Input/Output
# Input: lựa chọn menu, mã đơn hàng và trạng thái
# Output: danh sách đơn hàng hiển thị, thông báo thêm/sửa/xóa, thống kê trạng thái, hoặc thông báo lỗi/thoát

# Dùng vòng lặp while True để hiển thị menu chính
# Dùng input() để nhận lựa chọn và kiểm tra hợp lệ
# Chức năng 1: duyệt danh sách bằng enumerate() để in ra, nếu rỗng thì báo trống
# Chức năng 2: hiển thị menu con, xử lý thêm/sửa/xóa với chuẩn hóa dữ liệu (strip(), upper()), kiểm tra vị trí hợp lệ
# Chức năng 3: duyệt danh sách, tách trạng thái bằng split(" - "), đếm số lượng từng trạng thái
# Chức năng 4: thoát bằng break
# Edge cases: nhập sai menu, nhập sai vị trí, nhập chữ thay vì số, danh sách rỗng

# order_list = []
# while True:
#     in ra menu chính
#     choice = input()
#     if choice == "1":
#         hiển thị danh sách hoặc báo trống
#     elif choice == "2":
#         hiển thị menu con
#         xử lý thêm/sửa/xóa/quay lại
#     elif choice == "3":
#         duyệt danh sách, đếm trạng thái, in thống kê
#     elif choice == "4":
#         in "Thoát chương trình", break
#     else:
#         in "Lựa chọn không hợp lệ"


# Hệ thống quản lý đơn hàng Grab Express

# Hệ thống quản lý đơn hàng Grab Express

# Hệ thống quản lý đơn hàng Grab Express

order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED",
    "GE004 - PENDING"
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Cập nhật danh sách đơn hàng")
    print("3. Thống kê đơn hàng theo trạng thái")
    print("4. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()

    match choice:
        case "1":
            if not order_list:
                print("Danh sách đơn hàng hiện đang trống.")
            else:
                print("Danh sách đơn hàng hiện tại:")
                for idx, order in enumerate(order_list, start=1):
                    print(f"{idx}. {order}")

        case "2":
            while True:
                print("\n----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----")
                print("1. Thêm đơn hàng mới")
                print("2. Sửa đơn hàng theo vị trí")
                print("3. Xóa đơn hàng theo vị trí")
                print("4. Quay lại menu chính")

                sub_choice = input("Nhập lựa chọn của bạn (1-4): ").strip()

                match sub_choice:
                    case "1":
                        code = input("Nhập mã đơn hàng: ").strip().upper()
                        status = input("Nhập trạng thái đơn hàng: ").strip().upper()
                        order_list.append(f"{code} - {status}")
                        print(f"Đã thêm đơn hàng: {code} - {status}")

                    case "2":
                        pos = input("Nhập vị trí đơn hàng cần sửa: ").strip()
                        if pos.isdigit():
                            pos = int(pos)
                            if 1 <= pos <= len(order_list):
                                 
                                code = input("Nhập mã đơn hàng mới: ").strip().upper()
                                status = input("Nhập trạng thái mới: ").strip().upper()
                                order_list[pos - 1] = f"{code} - {status}"
                                print(f"Đã cập nhật đơn hàng tại vị trí {pos}.")
                            else:
                                print("Không tồn tại đơn hàng ở vị trí này!")
                        else:
                            print("Vị trí không hợp lệ!")

                    case "3":
                        pos = input("Nhập vị trí đơn hàng cần xóa: ").strip()
                        if pos.isdigit():
                            pos = int(pos)
                            if 1 <= pos <= len(order_list):
                                remove = order_list.pop(pos - 1)
                                print(f"Đã xóa đơn hàng: {remove}")
                            else:
                                print("Không tồn tại đơn hàng ở vị trí này!")
                        else:
                            print("Vị trí không hợp lệ!")

                    case "4":
                        break

                    case _:
                        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

        case "3":
            statuses = {"PENDING": 0, "DELIVERING": 0, "COMPLETED": 0, "CANCELLED": 0}
            for order in order_list:
                parts = order.split(" - ")
                if len(parts) == 2:
                    status = parts[1].strip().upper()
                    if status in statuses:
                        statuses[status] += 1
            print("\n===== THỐNG KÊ ĐƠN HÀNG =====")
            for key, value in statuses.items():
                print(f"{key}: {value}")
            print(f"Tổng số đơn hàng: {len(order_list)}")

        case "4":
            print("Thoát chương trình.")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

