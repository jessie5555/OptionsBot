import psycopg2
class PostgresqlDatabase():
    def __init__(self):
        self.conn =psycopg2.connect(
    database = "tickers",
    user='jessie',
    password='********',
    host='localhost',
    port='5432'
)
        self.conn.autocommit = True
        self.cursor  = self.conn.cursor()
        
    
    def create_tables(self):
        commands = (
            """
            CREATE TABLE ticker (
                ticker_id SERIAL PRIMARY KEY,
                ticker_name VARCHAR(255) NOT NULL
            )

            CREATE TABLE experation (
                id = SERIAL PRIMARY KEY
                ticker = VARCHAR255 NOT NULL
                expdata = DATE 
                CONSTRAINT fk_ticker FORIEGN KEY(ticker) REFERENCES ticker(ticker_name)


            )
            
            
            """





        )








conn.close
