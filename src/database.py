import sqlite3
from datetime import datetime

class DatabaseManager():
    def __init__(self):
        self.conn = sqlite3.connect("prices.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS product_prices(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        price REAL,
        date TEXT                                                   
    )
""")
        
    def insert_price(self, title,price):
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = "INSERT INTO product_prices (title, price, date) VALUES (?,?,?)"
        self.cursor.execute(query, (title,price,current_date))
        self.conn.commit()