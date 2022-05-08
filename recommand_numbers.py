from db_config import DBConfig


db = DBConfig()
conn,cursor = db.connect()
sql = 'select * from lotto_numbers'
cursor.execute(sql)
data = cursor.fetchall()
for r in data:
    print(r)