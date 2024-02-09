import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Laplateforme"
)

cursor = conn.cursor()

sql_query = "SELECT * FROM etudiant"

cursor.execute(sql_query)

results = cursor.fetchall()

for etudiant in results:
    print(etudiant)

cursor.close()
conn.close()
