import pandas as pd

def run_pandas_solution(conn):
    try:
        customers = pd.read_sql("SELECT * FROM Customer", conn)
        sales = pd.read_sql("SELECT * FROM Sales", conn)
        orders = pd.read_sql("SELECT * FROM Orders", conn)
        items = pd.read_sql("SELECT * FROM Items", conn)

        df = orders.merge(sales, on="sales_id") \
                   .merge(customers, on="customer_id") \
                   .merge(items, on="item_id")

        df = df[(df["age"].between(18,35)) & (df["quantity"].notna())]

        result = df.groupby(
            ["customer_id","age","item_name"],
            as_index=False
        )["quantity"].sum()

        result = result[result["quantity"] > 0]

        result.columns = ["Customer","Age","Item","Quantity"]
        result["Quantity"] = result["Quantity"].astype(int)

        return result.sort_values(["Customer","Item"])

    except Exception as e:
        print(f"Pandas solution failed: {e}")
        raise