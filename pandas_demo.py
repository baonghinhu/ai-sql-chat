import pandas as pd
import numpy as np

# Tạo dummy data
data = {
    'Tên': ['Hưng', 'Linh', 'Minh', 'Hà', 'Long'],
    'Tuổi': [25, 30, 28, 22, 35],
    'Lương': [15000000, 20000000, 18000000, 12000000, 25000000],
    'Phòng': ['IT', 'HR', 'IT', 'Sales', 'Finance']
}

# Tạo DataFrame
df = pd.DataFrame(data)

print("=== Dữ liệu gốc ===")
print(df)
print("\n")

# Thông tin cơ bản
print("=== Thông tin DataFrame ===")
print(df.info())
print("\n")

# Thống kê
print("=== Thống kê lương ===")
print(df['Lương'].describe())
print("\n")

# Lọc dữ liệu
print("=== Nhân viên tuổi >= 28 ===")
print(df[df['Tuổi'] >= 28])
print("\n")

# Sắp xếp
print("=== Sắp xếp theo lương (giảm dần) ===")
print(df.sort_values('Lương', ascending=False))
print("\n")

# Nhóm dữ liệu
print("=== Lương trung bình theo Phòng ===")
print(df.groupby('Phòng')['Lương'].mean())
print("\n")

# Thêm cột mới
df['Lương_Tỷ'] = df['Lương'] / 1000000
print("=== Thêm cột Lương tính bằng Triệu ===")
print(df)
