import pandas as pd

# a. Nhập dữ liệu vào data frame
data = {'TT': [1, 2, 3, 4, 5, 6, 7, 8],
        'luong': [6.0, 5.0, 4.5, 3.8, 8.0, 8.0, 4.0, 5.0],
        'gioi_tinh': ['Nam', 'Nu', 'Nam', 'Nu', 'Nu', 'Nam', 'Nam', 'Nu'],
        'tot_nghiep': ['K', 'K', 'TB', 'K', 'G', 'G', 'TB', 'TB'],
        'tuoi': [22, 25, 23, 22, 22, 23, 22, 24]
}

sinh_vien = pd.DataFrame(data)

# b. Dữ liệu về sinh viên nữ
sinh_vien_nu = sinh_vien[sinh_vien['gioi_tinh'] == 'Nu']
print("Dữ liệu về sinh viên nữ:")
print(sinh_vien_nu)

# c. Dữ liệu về sinh viên nam
sinh_vien_nam = sinh_vien[sinh_vien['gioi_tinh'] == 'Nam']
print("Dữ liệu về sinh viên nam:")
print(sinh_vien_nam)

# d. Danh sách lương khởi điểm của sinh viên nữ
luong_nu = sinh_vien_nu['luong']
print("Danh sách lương khởi điểm của sinh viên nữ:")
print(luong_nu)

# e. Danh sách tuổi của sinh viên nam
tuoi_nam = sinh_vien_nam['tuoi']
print("Danh sách tuổi của sinh viên nam:")
print(tuoi_nam)

# f. Danh sách sinh viên có lương khởi điểm trên 6 triệu
luong_tren_6 = sinh_vien[sinh_vien['luong'] > 6.0]
print("Danh sách sinh viên có lương khởi điểm trên 6 triệu:")
print(luong_tren_6)

# g. Thông tin về những người có lương cao nhất
luong_cao_nhat = sinh_vien[sinh_vien['luong'] == sinh_vien['luong'].max()]
print("Thông tin về những người có lương cao nhất:")
print(luong_cao_nhat)

# h. Thêm thông tin của sinh viên mới
sinh_vien_moi = pd.DataFrame({'TT': [9],
                              'luong': [7.5],
                              'gioi_tinh': ['Nam'],
                              'tot_nghiep': ['G'],
                              'tuoi': [None]})
sinh_vien = sinh_vien.append(sinh_vien_moi, ignore_index=True)
print("Dữ liệu sau khi thêm sinh viên mới:")
print(sinh_vien)

# i. Thêm cột điểm khóa luận tốt nghiệp
diem_khoa_luan = [8, 7.5, 7, 7, 9, 9.5, 8, 8, 9]
sinh_vien['diem_khoa_luan'] = diem_khoa_luan
print("Dữ liệu sau khi thêm cột điểm khóa luận:")
print(sinh_vien)

# j. Loại bỏ số liệu trống không trong data frame
sinh_vien = sinh_vien.dropna()
print("Dữ liệu sau khi loại bỏ số liệu trống:")
print(sinh_vien)
