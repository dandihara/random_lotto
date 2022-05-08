import psycopg2

class DBConfig():

    def __init__(self):
        self.db = psycopg2.connect(host = 'localhost', dbname = 'postgres', user = 'postgres', port = 5432, password = '0000')

    def connect(self):
        cursor = self.db.cursor()
        conn = self.db
        return conn,cursor