import mysql.connector

conn = mysql.connector.connect(
  host='localhost',
  user="root",
  passwd="deadman300$123",
  database="userdb"
)

cursor = conn.cursor()
query = 'SELECT EventID, `Time Generated` FROM test'
cursor.execute(query)
result = cursor.fetchall()

for r in result:
    print(r)

cursor.close()
conn.close()