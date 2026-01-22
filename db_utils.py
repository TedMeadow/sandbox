import sqlite3

def execute_query(param: str):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    sql = f"SELECT * FROM users WHERE id = '{param}'"
    
    cursor.execute(sql)
    return cursor.fetchall()