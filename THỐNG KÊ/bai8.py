import pandas as pd

# a. Đọc dữ liệu từ file CSV
data = pd.read_csv('./Du_lieu/SoLieu.csv')

# b. Số nam và số người sống ở thành phố
so_nam = len(data[data['GioiTinh'] == 'Nam'])
so_nguoi_thanh_pho = len(data[data['KhuVuc'] == 'Thành phố'])
print("Số nam trong nhóm được điều tra:", so_nam)
print("Số người sống ở thành phố trong nhóm được điều tra:", so_nguoi_thanh_pho)

# c. Số nam sống ở hải đảo và nữ sống ở nông thôn
so_nam_hai_dao = len(data[(data['GioiTinh'] == 'Nam') & (data['KhuVuc'] == 'Hải đảo')])
so_nu_nong_thon = len(data[(data['GioiTinh'] == 'Nữ') & (data['KhuVuc'] == 'Nông thôn')])
print("Số nam sống ở hải đảo:", so_nam_hai_dao)
print("Số nữ sống ở nông thôn:", so_nu_nong_thon)

# d. Tỷ lệ nữ sống ở thành phố và miền núi
so_nu_thanh_pho = len(data[(data['GioiTinh'] == 'Nữ') & (data['KhuVuc'] == 'Thành phố')])
so_nu_mien_nui = len(data[(data['GioiTinh'] == 'Nữ') & (data['KhuVuc'] == 'Miền núi')])
ty_le_nu_thanh_pho = so_nu_thanh_pho / len(data[data['GioiTinh'] == 'Nữ'])
ty_le_nu_mien_nui = so_nu_mien_nui / len(data[data['GioiTinh'] == 'Nữ'])
print("Tỷ lệ nữ sống ở thành phố:", ty_le_nu_thanh_pho)
print("Tỷ lệ nữ sống ở miền núi:", ty_le_nu_mien_nui)

# e. Phân tổ cột dữ liệu về tuổi và tính tỷ lệ người có độ tuổi không vượt quá 50
bins_tuoi = [0, 20, 30, 40, 50, 60, 70, 80]
labels_tuoi = ['0-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80']
data['TongHopTuoi'] = pd.cut(data['Tuoi'], bins=bins_tuoi, labels=labels_tuoi, right=False).astype(str)
ty_le_tuoi_vuot_qua_50 = len(data[data['TongHopTuoi'] <= '50']) / len(data)
print("Tỷ lệ những người được điều tra có độ tuổi không vượt quá 50:", ty_le_tuoi_vuot_qua_50)

# f. Phân tổ cột dữ liệu về thu nhập và tính tỷ lệ
bins_thu_nhap = [0, 20, 40, 60, 80, 100]
labels_thu_nhap = ['0-20', '20-40', '40-60', '60-80', '80-100']
data['TongHopThuNhap'] = pd.cut(data['ThuNhap'], bins=bins_thu_nhap, labels=labels_thu_nhap, right=False)

# i. Tỉ lệ người phải đóng thuế thu nhập nếu tổng thu nhập vượt quá 60 triệu VND
ty_le_phai_dong_thue = len(data[data['ThuNhap'] > 60]) / len(data)
print("Tỷ lệ người phải đóng thuế thu nhập nếu tổng thu nhập vượt quá 60 triệu VND:", ty_le_phai_dong_thue)

# ii. Tỉ lệ người có thu nhập hơn 80 triệu nằm trong khoảng tuổi (40, 50]
ty_le_thu_nhap_80_triệu = len(data[data['TongHopThuNhap'] == '80-100'])
ty_le_tuoi_40_den_50 = len(data[(data['TongHopTuoi'] > '40') & (data['TongHopTuoi'] <= '50')])
ty_le = ty_le_thu_nhap_80_triệu / ty_le_tuoi_40_den_50
print("Tỷ lệ người có thu nhập hơn 80 triệu nằm trong khoảng tuổi (40, 50]:", ty_le)
