import pandas as pd

# 1. Tự tạo dữ liệu dummy (Dictionary)
data = {
    'Ngày': ['2026-01-01', '2026-01-02', '2026-01-03', '2026-01-04', '2026-01-01'],
    'Sản phẩm': ['Laptop', 'Chuột', 'Laptop', 'Bàn phím', 'Chuột'],
    'Số lượng': [5, 10, 3, 7, 12],
    'Giá bán': [1500, 20, 1500, 50, 25]
}

# 2. Chuyển thành DataFrame (Bảng dữ liệu của Pandas)
df = pd.DataFrame(data)

# 3. Tính toán thêm cột mới: Thành tiền = Số lượng * Giá bán
df['Thành tiền'] = df['Số lượng'] * df['Giá bán']

# 4. Hiển thị bảng dữ liệu
print("--- Bảng dữ liệu bán hàng ---")
print(df)

# 5. Thống kê đơn giản: Tính tổng doanh thu theo Sản phẩm
summary = df.groupby('Sản phẩm')['Thành tiền'].sum().reset_index()

print("\n--- Tổng doanh thu theo từng sản phẩm ---")
print(summary)

# 6. Lọc dữ liệu: Chỉ lấy các đơn hàng có Số lượng > 5
df_filtered = df[df['Số lượng'] > 5]

print("\n--- Các đơn hàng có số lượng lớn hơn 5 ---")
print(df_filtered)