import pandas as pd

def run_sql_solution(conn):
    try:
        query = """
        SELECT 
            c.customer_id AS Customer,
            c.age AS Age,
            i.item_name AS Item,
            SUM(o.quantity) AS Quantity
        FROM Orders o
        JOIN Sales s ON o.sales_id = s.sales_id
        JOIN Customer c ON s.customer_id = c.customer_id
        JOIN Items i ON o.item_id = i.item_id
        WHERE c.age BETWEEN 18 AND 35
              AND o.quantity IS NOT NULL
        GROUP BY c.customer_id, i.item_id
        HAVING SUM(o.quantity) > 0
        ORDER BY c.customer_id, i.item_name;
        """

        df = pd.read_sql_query(query, conn)
        df["Quantity"] = df["Quantity"].astype(int)
        return df

    except Exception as e:
        print(f"SQL query failed: {e}")
        raise