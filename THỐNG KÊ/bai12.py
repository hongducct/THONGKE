import pandas as pd
import matplotlib.pyplot as plt

# a. Vẽ biểu đồ thân và lá cho cột tuổi
data = pd.read_csv('./Du_lieu/SoLieu.csv')
tuoi = data['Tuoi']
plt.boxplot(tuoi, vert=False)
plt.xlabel('Tuổi')
plt.show()
# Nhận xét: Biểu đồ hộp và râu cho cột tuổi sẽ cho ta thông tin về độ tập trung, phân tán và sự xuất hiện của ngoại lệ trong phân phối tuổi của nhóm được điều tra.

# b. Vẽ biểu đồ phân phối tần số cho cột thu nhập
thu_nhap = data['ThuNhap']
plt.hist(thu_nhap, bins=range(0, max(thu_nhap)+10, 10), edgecolor='black')
plt.xlabel('Thu nhập')
plt.ylabel('Tần số')
plt.show()
# Nhận xét: Biểu đồ phân phối tần số với độ rộng mỗi cột là 10 cho cột thu nhập sẽ cho ta thông tin về sự phân bố của thu nhập trong nhóm được điều tra.

# c. Vẽ biểu đồ thanh minh họa phân phối tần số của khu vực sống
khu_vuc_song = data['KhuVuc']
khu_vuc_song_counts = khu_vuc_song.value_counts()
plt.bar(khu_vuc_song_counts.index, khu_vuc_song_counts.values)
plt.xlabel('Khu vực sống')
plt.ylabel('Tần số')
plt.show()
# Nhận xét: Biểu đồ thanh minh họa phân phối tần số của khu vực sống sẽ cho ta thông tin về sự phân bố của nhóm được điều tra theo khu vực sống.

# d. Vẽ biểu đồ thanh minh họa phân phối tần số giới tính theo khu vực sống
gender_by_khu_vuc_song = pd.crosstab(data['KhuVuc'], data['GioiTinh'])
gender_by_khu_vuc_song.plot(kind='bar', stacked=True)
plt.xlabel('Khu vực sống')
plt.ylabel('Tần số')
plt.legend(title='Giới tính')
plt.show()
# Nhận xét: Biểu đồ thanh minh họa phân phối tần số giới tính theo khu vực sống sẽ cho ta thông tin về phân bố của giới tính trong từng khu vực sống và sự so sánh giữa các khu vực sống.

# e. Chọn một đại lượng để miêu tả độ tập trung cho mỗi cột dữ liệu và tính những đại lượng này
dai_luong = ['Trung bình cộng', 'Trung vị', 'Mode']
dulieu_cot = ['Tuoi', 'ThuNhap', 'KhuVucSong', 'GioiTinh']

for col in dulieu_cot:
    if col != 'GioiTinh':
        data_col = data[col]
        if col == 'KhuVuc':
            mode = data_col.mode().values
            modes = ', '.join(str(value) for value in mode)
            print(f'{col}:')
            print(f'Mode: {modes}')
        else:
            mean = data_col.mean()
            median = data_col.median()
            mode = data_col.mode().values[0]
            print(f'{col}:')
            print(f'Trung bình cộng: {mean}')
            print(f'Trung vị: {median}')
            print(f'Mode: {mode}')
    print('--------------')
