from db_config import DBConfig


db = DBConfig()
conn,cursor = db.connect()
sql = 'select * from lotto_numbers'
cursor.execute(sql)
data = cursor.fetchall()
time_numbers = [[0 for i in range(45)] for j in range(45)]

for r in data:
    numbers = r[2:]
    for cursor in range(6):
        for num in range(6):
            if cursor != num:
                time_numbers[numbers[cursor]-1][numbers[num]-1] += 1


percent_dicts = []
# 빈도수를 이용한 연관성 
for i,count_list in enumerate(time_numbers):
    whole_count = sum(count_list) - count_list[i]
    count_dict = {}
    print(whole_count)
    for j in range(len(count_list)):
        if j != i:
            count_dict[i] = round(count_list[j] / whole_count,3)
        else:
            count_dict[i] = 0
    percent_dicts.append(count_dict)

print(percent_dicts)        
    
