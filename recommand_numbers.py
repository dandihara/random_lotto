from db_config import DBConfig


db = DBConfig()
conn,cursor = db.connect()
sql = 'select * from lotto_numbers'
cursor.execute(sql)
data = cursor.fetchall()
time_numbers = [[0 for i in range(45)] for j in range(45)]
for r in data:
    print(r)
    
