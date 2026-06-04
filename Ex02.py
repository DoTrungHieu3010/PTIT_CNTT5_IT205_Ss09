# insert(0, "GE100-FAST"): chèn vào đầu, các phần tử cũ bị đẩy sang phải

# express_orders[1] = ...: sửa nhầm vì "GE101" bị đẩy sang index 1

# "GE102-WRONG" nằm ở index 2 sau khi chèn

# pop(3): xóa sai vì "GE103-CANCEL" không còn ở vị trí 3

# Xóa đúng dùng: express_orders.remove("GE103-CANCEL")

# pop() mặc định lấy phần tử cuối

# current_order = express_orders.pop() sai vì lấy cuối thay vì đầu

# Lấy đúng đơn đầu: current_order = express_orders.pop(0)

# Cần sửa các dòng: cập nhật index, dùng remove(), và pop(0)

# Danh sách đơn hàng ban đầu
express_orders = ["GE101", "GE102-WRONG", "GE103-CANCEL"]

# Thêm đơn hàng mới vào cuối danh sách
express_orders.append("GE104")

# Chèn đơn hàng hỏa tốc vào đầu danh sách
express_orders.insert(0, "GE100-FAST")

# Sửa mã đơn hàng bị nhập sai
express_orders[2] = "GE102-UPDATED"

# Xóa đơn hàng bị khách hủy
express_orders.remove("GE103-CANCEL")

# Lấy đơn hàng đầu tiên ra để bắt đầu giao
current_order = express_orders.pop(0)

print("Danh sách đơn hàng còn lại:", express_orders)
print("Đơn hàng đang giao:", current_order)