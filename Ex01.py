# Sau khi chạy dòng  lệnh, danh sách bị thay đổi là list sẽ thêm 1 phần tử "GE000" ở đầu

# Dòng sửa sai đơn hàng cần cấp nhật do đã có thêm 1 phần tử mới ở đầu nên chỉ số bị lùi đi 1 đơn vị

# Sau khi chèn "GE000" vào đầu danh sách, "GE002" đang nằm ở index 3

# delivery_orders.remove(3) dòng này lỗi do remove không xóa theo index

# phương thức remove xóa theo giá trị

# để xóa thì ghi delivery_orders.remove("GE003-CANCEL")

# pop() có tác dụng xóa đi phần tử ở cuối và lấy ra giá trị của phần tử đã xóa

# tại vì biến đấy chưa có giá trị

# muốn lưu lại đơn hàng vừa xóa bằng pop thì cần khởi tạo ra 1 biến để lưu

# Danh sách đơn hàng ban đầu
delivery_orders = ["GE001", "GE002", "GE003-CANCEL"]

# Thêm đơn hàng mới vào cuối danh sách
delivery_orders.append("GE004")

# Chèn đơn hàng hỏa tốc vào đầu danh sách
delivery_orders.insert(0, "GE000")

# Sửa mã đơn hàng GE002 thành GE002-UPDATED
delivery_orders[2] = "GE002-UPDATED"

# Xóa đơn hàng bị khách hủy
delivery_orders.remove("GE003-CANCEL")

# Lấy đơn hàng cuối cùng ra để bàn giao cho tài xế khác
transferred_order = delivery_orders.pop()

print("Danh sách đơn hàng còn lại:", delivery_orders)
print("Đơn hàng được bàn giao:", transferred_order)