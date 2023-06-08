# a. Nhập dữ liệu thành một vector tên là tien_dt
tien_dt = [198, 185, 223, 221, 207, 203, 180, 195, 222, 177, 214, 216]

# b. Tính tổng số tiền phải trả cho phí điện thoại trong năm
tong_tien = sum(tien_dt)
print("Tổng số tiền phải trả trong năm:", tong_tien, "nghìn đồng")

# c. Tìm tháng có số tiền ít nhất và nhiều nhất
thang_it_nhat = min(tien_dt)
thang_nhieu_nhat = max(tien_dt)
print("Tháng có số tiền ít nhất là tháng", tien_dt.index(thang_it_nhat) + 1, "với số tiền", thang_it_nhat, "nghìn đồng")
print("Tháng có số tiền nhiều nhất là tháng", tien_dt.index(thang_nhieu_nhat) + 1, "với số tiền", thang_nhieu_nhat, "nghìn đồng")

# d. Đếm số tháng bạn phải trả hơn 200 nghìn tiền điện thoại
so_thang_tren_200 = len([tien for tien in tien_dt if tien > 200])
print("Số tháng bạn phải trả hơn 200 nghìn tiền điện thoại:", so_thang_tren_200)

# e. Đếm số tháng tiền điện thoại không quá 190 nghìn
so_thang_duoi_190 = len([tien for tien in tien_dt if tien <= 190])
print("Số tháng tiền điện thoại không quá 190 nghìn:", so_thang_duoi_190)

# f. Đếm số tháng tiền điện thoại dao động trong khoảng [190, 210] nghìn
so_thang_trong_khoang = len([tien for tien in tien_dt if 190 <= tien <= 210])
print("Số tháng tiền điện thoại dao động trong khoảng [190, 210] nghìn:", so_thang_trong_khoang)

# g. Tính số tiền điện thoại trung bình mỗi tháng
so_thang = len(tien_dt)
tien_trung_binh = tong_tien / so_thang
print("Số tiền điện thoại trung bình mỗi tháng:", tien_trung_binh, "nghìn đồng")
