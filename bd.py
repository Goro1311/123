import sqlite3

def create_first_table():
    cursor.execute("CREATE TABLE types (id real, type text)")

def delete_type():
    cursor.execute("UPDATE types SET type = 'Artem' WHERE type = 'Абиссинская кошка'")

    
if __name__ == "__main__":
    conn = sqlite3.connect("my_test.db")
    cursor = conn.cursor()
    delete_type()
    conn.commit()
    conn.close()

    
