import pandas as pd

# a. Đọc dữ liệu từ file CSV
data = pd.read_csv('./Du_lieu/HocSinh.csv')

# b. Số cột và số dòng của tập dữ liệu
num_columns = len(data.columns)
num_rows = len(data)
print("Số cột:", num_columns)
print("Số dòng:", num_rows)

# c. Lấy dữ liệu ở cột thứ 3 (Tuoi)
tuoi = data['Tuoi']
print("Dữ liệu ở cột Tuoi:")
print(tuoi)

# d. Lấy toàn bộ dữ liệu ở dòng thứ 10
dong_thu_10 = data.iloc[9]
print("Dữ liệu ở dòng thứ 10:")
print(dong_thu_10)

# e. Số học sinh nam và nữ
hoc_sinh_nam = data[data['GioiTinh'] == 'Nam']
hoc_sinh_nu = data[data['GioiTinh'] == 'Nu']
so_hoc_sinh_nam = len(hoc_sinh_nam)
so_hoc_sinh_nu = len(hoc_sinh_nu)
print("Số học sinh nam:", so_hoc_sinh_nam)
print("Số học sinh nữ:", so_hoc_sinh_nu)

# f. Tỷ lệ học sinh có mức độ yêu thích thể thao là 4
tyle_nam = len(hoc_sinh_nam[hoc_sinh_nam['TheThao'] == 4]) / so_hoc_sinh_nam
tyle_nu = len(hoc_sinh_nu[hoc_sinh_nu['TheThao'] == 4]) / so_hoc_sinh_nu
print("Tỷ lệ học sinh nam có mức độ yêu thích thể thao là 4:", tyle_nam)
print("Tỷ lệ học sinh nữ có mức độ yêu thích thể thao là 4:", tyle_nu)
