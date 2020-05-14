import sqlite3

database = sqlite3

conn = database.connect('password_database.db')

c = conn.cursor()

#c.execute("INSERT INTO password VALUES (3,'Tobi Gwiggner','www.casino.at','derit','11:21')")
conn.commit()
#c.execute("CREATE TABLE password (website text, password text, date text)")

c.execute("DROP TABLE password")
#c.execute("DELETE FROM password WHERE id = 10")
c.execute("CREATE TABLE password (website text, name text, password text, date text)")

#c.execute("SELECT * FROM password")
#database_row_count = str(c.fetchall())
#print(database_row_count)

#with conn:
#    c.execute("SELECT * FROM password")
#    print(len(c.fetchall()))
