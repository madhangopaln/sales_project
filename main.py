import os
from database import get_connection, create_tables, insert_sample_data
from sql_solution import run_sql_solution
from pandas_solution import run_pandas_solution

OUTPUT_DIR = "output"

def save_csv(df, filename):
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        df.to_csv(f"{OUTPUT_DIR}/{filename}",
                  sep=";",
                  index=False)
    except Exception as e:
        print(f"CSV write failed: {e}")
        raise


def main():
    try:
        conn = get_connection()
        create_tables(conn)
        insert_sample_data(conn)

        sql_df = run_sql_solution(conn)
        pandas_df = run_pandas_solution(conn)

        if not sql_df.equals(pandas_df):
            raise ValueError("Outputs do NOT match!")

        save_csv(sql_df, "sql_output.csv")
        save_csv(pandas_df, "pandas_output.csv")

        print("Both solutions produced identical results.")

    except Exception as e:
        print(f"Application error: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()