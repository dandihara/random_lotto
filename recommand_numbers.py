from db_config import DBConfig


db = DBConfig()
conn,cursor = db.connect()
sql = 'select * from lotto_numbers'
cursor.execute(sql)
data = cursor.fetchall()
time_numbers = [[0 for i in range(45)] for j in range(45)]
print(time_numbers)
for r in data:
    numbers = r[2:]
    for cursor in range(6):
        for num in range(6):
            if cursor != num:
                time_numbers[numbers[cursor]-1][numbers[num]-1] += 1

print(time_numbers)
        
    
