import pandas as pd

# Đọc dữ liệu từ tập tin euro2012.csv và tạo data frame euro12
euro12 = pd.read_csv('euro2012.csv')

# Câu 1: In type, shape, danh sách các cột của euro12
print("1. Type of euro12:", type(euro12))
print("   Shape of euro12:", euro12.shape)
print("   Columns of euro12:", euro12.columns)

# Câu 2: In giá trị cột Goals
print("\n2. Goals column:")
print(euro12['Goals'])

# Câu 3: Số đội tham gia Euro2012 và thông tin của Euro2012
num_teams = euro12['Team'].nunique()
print("\n3. Number of teams in Euro2012:", num_teams)
print("   Information of Euro2012:")
print(euro12.info())

# Câu 4: Tạo data frame mới 'discipline' chỉ chứa 3 cột 'Team', 'Yellow Cards', 'Red Cards'
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]

# Câu 5: Sắp xếp discipline giảm dần theo 2 cột 'Red Cards', 'Yellow Cards'
discipline_sorted = discipline.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=False)

# Câu 6a: Trung bình Yellow Cards
average_yellow_cards = euro12['Yellow Cards'].mean()

# Câu 6b: Lọc các đội đã ghi hơn 6 bàn thắng
teams_with_more_than_6_goals = euro12[euro12['Goals'] > 6]

# Câu 7: In các đội mà tên bắt đầu bằng 'G'
teams_starting_with_G = euro12[euro12['Team'].str.startswith('G')]

# Câu 8: In 7 cột đầu của euro12
print("\n8. First 7 columns of euro12:")
print(euro12.iloc[:, :7])

# Câu 9: In tất cả các cột, trừ 3 cột cuối
print("\n9. All columns except the last 3:")
print(euro12.iloc[:, :-3])

# Câu 10: In các cột Team, Goals, Shooting Accuracy, Yellow Cards, Red Cards
selected_columns = ['Team', 'Goals', 'Shooting Accuracy', 'Yellow Cards', 'Red Cards']
print("\n10. Selected columns:")
print(euro12[selected_columns])

# Câu 11: In các cột chỉ hiển thị 'Team', 'Shooting Accuracy' từ 'England', 'Italy', 'Russia'
selected_teams = ['England', 'Italy', 'Russia']
selected_columns_11 = ['Team', 'Shooting Accuracy']
print("\n11. Selected columns for England, Italy, Russia:")
print(euro12[euro12['Team'].isin(selected_teams)][selected_columns_11])