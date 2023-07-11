import sqlite3

connection = sqlite3.connect("test.db")

cur = connection.cursor()

# cur.execute("CREATE TABLE t(c1, c2,c3)")

cur.execute("SELECT name FROM sqlite_master")
for i in cur:
    print(i)