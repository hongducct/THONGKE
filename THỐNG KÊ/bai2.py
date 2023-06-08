import numpy as np

# a. Nhập dữ liệu thành một vectơ có tên tiền_dt
tien_dt = np.array([198, 185, 223, 221, 207, 203, 180, 195, 222, 177, 214, 216])

# b. Tính tổng số tiền phải trả trong năm
tong_tien = np.sum(tien_dt)
print("Tổng số tiền phải trả trong năm:", str(tong_tien), "đơn vị")

# c. Tìm tháng có số tiền ít nhất và nhiều nhất
thang_it_nhat = np.argmin(tien_dt) + 1
thang_nhieu_nhat = np.argmax(tien_dt) + 1
so_tien_it_nhat = np.min(tien_dt)
so_tien_nhieu_nhat = np.max(tien_dt)
print("Tháng có số tiền ít nhất:", thang_it_nhat)
print("Số tiền ít nhất:", so_tien_it_nhat)
print("Tháng có số tiền nhiều nhất:", thang_nhieu_nhat)
print("Số tiền nhiều nhất:", so_tien_nhieu_nhat)

# d. Tìm số tháng có số tiền điện thoại trên 200 nghìn
so_thang_tren_200 = np.sum(tien_dt > 200)
print("Số tháng có số tiền trên 200 nghìn:", so_thang_tren_200)

# e. Tìm số tháng có số tiền điện thoại không quá 190 nghìn
so_thang_khong_qua_190 = np.sum(tien_dt <= 190)
print("Số tháng có số tiền không quá 190 nghìn:", so_thang_khong_qua_190)

# f. Tìm số tháng có số tiền điện thoại trong khoảng [190, 210] nghìn
so_thang_trong_khoang = np.sum((tien_dt >= 190) & (tien_dt <= 210))
print("Số tháng có số tiền trong khoảng [190, 210] nghìn:", so_thang_trong_khoang)

# g. Tính số tiền điện thoại trung bình mỗi tháng
tien_trung_binh = np.mean(tien_dt)
print("Số tiền điện thoại trung bình mỗi tháng:", str(tien_trung_binh), "đơn vị")
