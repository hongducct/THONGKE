# Dữ liệu tiền điện thoại
tien_dt = [198, 185, 223, 221, 207, 203, 180, 195, 222, 177, 214, 216]

# a. Sửa tiền điện thoại tháng 2 thành 175
tien_dt[1] = 175

# b. Nhập thêm tiền điện thoại của 3 tháng tiếp theo
tien_dt.extend([201, 185])
# print(tien_dt)

# Tính lại số tiền trung bình mỗi tháng
so_thang = len(tien_dt)
tong_tien = sum(tien_dt)
tien_trung_binh = tong_tien / so_thang

# In kết quả
print("Số tiền điện thoại trung bình mỗi tháng: ", tien_trung_binh)
