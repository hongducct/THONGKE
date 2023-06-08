tien_dt = [198, 185, 223, 221, 207, 203, 180, 195, 222, 177, 214, 216]
# a. Sửa tiền điện thoại tháng 2 thành 175
tien_dt[1] = 175

# b. Nhập thêm tiền điện thoại của 3 tháng tiếp theo
tien_dt.extend([0, 201, 185])

# Tính lại số tiền trung bình bạn phải trả mỗi tháng
so_thang_moi = len(tien_dt)
tong_tien_moi = sum(tien_dt)
tien_trung_binh_moi = tong_tien_moi / so_thang_moi

print("Sau khi sửa và thêm dữ liệu mới ")
print("Số tiền điện thoại trung bình mỗi tháng:", tien_trung_binh_moi, "nghìn đồng")
