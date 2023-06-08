import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Tập dữ liệu
diem_thi = pd.Series([61, 27, 26, 37, 30, 47, 87, 90, 63, 46, 67, 19, 81, 47, 100, 25, 45, 60, 65, 53, 35, 28, 80, 95, 57, 37, 45, 25, 48, 60, 48, 47, 30, 47, 60, 61, 55, 48, 60, 90])

# a. Số đo hướng tâm
trung_binh_cong = diem_thi.mean()
trung_vi = diem_thi.median()
mode = diem_thi.mode().values[0]
print("Trung bình cộng:", trung_binh_cong)
print("Trung vị:", trung_vi)
print("Mode:", mode)

# b. Đại lượng mô tả độ phân bố
tu_phan_vi = np.percentile(diem_thi, [25, 50, 75])
phan_vi_10 = np.percentile(diem_thi, 10)
phan_vi_60 = np.percentile(diem_thi, 60)
phan_vi_90 = np.percentile(diem_thi, 90)
print("Tứ phân vị:", tu_phan_vi)
print("Phân vị thứ 10:", phan_vi_10)
print("Phân vị thứ 60:", phan_vi_60)
print("Phân vị thứ 90:", phan_vi_90)

# c. Đại lượng mô tả độ phân tán
khoang_bien_thien = diem_thi.max() - diem_thi.min()
do_trai_giua = np.percentile(diem_thi, 75) - np.percentile(diem_thi, 25)
phuong_sai = diem_thi.var()
do_lech_chuan = diem_thi.std()
print("Khoảng biến thiên:", khoang_bien_thien)
print("Độ trải giữa:", do_trai_giua)
print("Phương sai:", phuong_sai)
print("Độ lệch chuẩn:", do_lech_chuan)

# d. Vẽ biểu đồ hộp và râu
plt.boxplot(diem_thi, vert=False)
plt.xlabel('Điểm Thi')
plt.show()
