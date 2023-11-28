import pandas as pd

# Câu 1: Đọc dữ liệu từ tập tin drinks.csv và hiển thị thông tin cơ bản
drink = pd.read_csv('chương 3/drinks.csv', index_col=0)

# Hiển thị thông tin về kiểu dữ liệu, kích thước và tên cột
print("1. Type of drink:", type(drink))
print("   Shape of drink:", drink.shape)
print("   Columns of drink:", drink.columns)
print("   Head of drink:")
print(drink.head())
print("   Tail of drink:")
print(drink.tail())

# Câu 2: Số lượng bia tiêu thụ trung bình ở mỗi châu lục
average_beer_consumption = drink.groupby('continent')['beer_servings'].mean()
print("\n2. Số lượng bia tiêu thụ trung bình ở mỗi châu lục:")
print(average_beer_consumption)

# Câu 3: Thông tin thống kê tổng quát về số lượng rượu vang tiêu thụ ở mỗi châu lục
wine_consumption_stats = drink.groupby('continent')['wine_servings'].describe()
print("\n3. Thông tin thống kê tổng quát về số lượng rượu vang tiêu thụ ở mỗi châu lục:")
print(wine_consumption_stats)

# Câu 4: Số lượng bia và rượu tiêu thụ trung bình ở mỗi châu lục
average_beer_and_wine_consumption = drink.groupby('continent')[['beer_servings', 'wine_servings']].mean()
print("\n4. Số lượng bia và rượu tiêu thụ trung bình ở mỗi châu lục:")
print(average_beer_and_wine_consumption)

# Câu 5: Giá trị trung vị cho bia và rượu tiêu thụ ở mỗi châu lục
median_beer_and_wine_consumption = drink.groupby('continent')[['beer_servings', 'wine_servings']].median()
print("\n5. Giá trị trung vị cho bia và rượu tiêu thụ ở mỗi châu lục:")
print(median_beer_and_wine_consumption)

# Câu 6: Số lượng rượu mạnh (spirit_servings) tiêu thụ trung bình, lớn nhất và nhỏ nhất ở mỗi châu lục
spirit_stats = drink.groupby('continent')['spirit_servings'].agg(['mean', 'max', 'min'])
print("\n6. Số lượng rượu mạnh (spirit_servings) tiêu thụ trung bình, lớn nhất và nhỏ nhất ở mỗi châu lục:")
print(spirit_stats)

# Câu 7: Sắp xếp dữ liệu tăng dần theo số lượng bia tiêu thụ và hiển thị 5 quốc gia có lượng tiêu thụ nhiều nhất và ít nhất
sorted_by_beer_consumption = drink.sort_values(by='beer_servings', ascending=True)
print("\n7. 5 quốc gia có lượng tiêu thụ bia nhiều nhất:")
print(sorted_by_beer_consumption.tail())
print("\n   5 quốc gia có lượng tiêu thụ bia ít nhất:")
print(sorted_by_beer_consumption.head())