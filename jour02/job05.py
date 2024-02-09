import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="LaPlateforme"
)

mycursor = mydb.cursor()

sql_query = "SELECT SUM(superficie) FROM etage"

mycursor.execute(sql_query)

superficie_totale = mycursor.fetchone()[0]

print(f"La superficie de La Plateforme est de {superficie_totale} m2")

mycursor.close()
mydb.close()
