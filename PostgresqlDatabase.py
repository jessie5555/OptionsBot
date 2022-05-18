import psycopg2
import csv


class PostgresqlDatabase():
    def __init__(self):
        self.conn =psycopg2.connect(
        database = "tickers",
        user='jessie',
        password='password',
        host='localhost',
        port='5432'
)
        self.conn.autocommit = True
        self.cursor  = self.conn.cursor()
        
    def create_stock_tables(self):
        path = "./tickers.csv"
        f = open(path, "r")
        cols = []
        while (True):
            first = f.readline().strip()
            if not first:
                break
            cols.append(first)
        print(cols)
        for col in cols:
            print(col)
            sqlQuery = 'DROP TABLE IF EXISTS ' + col +  ";\n"
            sqlQuery += 'CREATE TABLE ' + col + ' (' + '\n'
            sqlQuery += 'id serial PRIMARY KEY, \n'
            sqlQuery += 'date DATE NOT NULL, \n' 
            sqlQuery += 'time TIME NOT NULL, \n'
            sqlQuery += "open_price REAL NOT NULL,\n"
            sqlQuery += "close_price REAL NOT NULL \n"

            sqlQuery = sqlQuery[:-2]
            sqlQuery += ");"
        print(sqlQuery)
        self.cursor.execute(sqlQuery)
        self.conn.commit()
        self.cursor.close()



con = PostgresqlDatabase()
con.create_stock_tables()


