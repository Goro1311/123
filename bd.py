import sqlite3

def create_first_table():
    cursor.execute("CREATE TABLE types (id real, type text)")

def add_three_rows():
    cursor.execute("INSERT INTO types VALUES ('1','Абиссинская кошка')")
    cursor.execute("INSERT INTO types VALUES ('2','Австралийский мист')")
    cursor.execute("INSERT INTO types VALUES ('3','Американская жесткошерсная')")

    
if __name__ == "__main__":
    conn = sqlite3.connect("my_test.db")
    cursor = conn.cursor()
    create_first_table()
    add_three_rows()
    conn.commit()
    conn.close()

    
