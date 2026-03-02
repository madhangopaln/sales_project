import sqlite3

DB_NAME = "sales.db"

def get_connection():
    try:
        conn = sqlite3.connect(DB_NAME)
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        raise


def create_tables(conn):
    try:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Customer (
            customer_id INTEGER PRIMARY KEY,
            age INTEGER
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Sales (
            sales_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Items (
            item_id INTEGER PRIMARY KEY,
            item_name TEXT
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Orders (
            order_id INTEGER PRIMARY KEY,
            sales_id INTEGER,
            item_id INTEGER,
            quantity INTEGER,
            FOREIGN KEY (sales_id) REFERENCES Sales(sales_id),
            FOREIGN KEY (item_id) REFERENCES Items(item_id)
        );
        """)

        conn.commit()
    except Exception as e:
        print(f"Table creation failed: {e}")
        raise


def insert_sample_data(conn):
    try:
        cursor = conn.cursor()

        customers = [(1,21),(2,23),(3,35),(4,40),(5,29)]
        sales = [(1,1),(2,1),(3,2),(4,3),(5,4)]
        items = [(1,'x'),(2,'y'),(3,'z')]

        orders = [
            (1,1,1,10),
            (2,1,2,None),
            (3,1,3,5),
            (4,2,1,2),
            (5,2,2,1),
            (6,3,1,3),
            (7,3,3,None),
            (8,4,2,4),
            (9,5,1,7)
        ]

        cursor.executemany("INSERT INTO Customer VALUES (?,?)", customers)
        cursor.executemany("INSERT INTO Sales VALUES (?,?)", sales)
        cursor.executemany("INSERT INTO Items VALUES (?,?)", items)
        cursor.executemany("INSERT INTO Orders VALUES (?,?,?,?)", orders)

        conn.commit()
    except Exception as e:
        print(f"Data insertion failed: {e}")
        raise