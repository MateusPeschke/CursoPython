import sqlite3
conn = sqlite3.connect("Aula06\exeple.db")
c = conn.cursor()


#Creat Table
c.execute('''CREATE TABLE stocks
            (date text, trans text,symbol text, qty real, price real)''')
c.execute("DELECTE from stocks VALUES")

# Incsert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

c.execute("SELECT * FROM stocks")
resutado = c.fetchall()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
print(resutado)
c.execute("DELETE table stocks")