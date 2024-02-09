import mysql.connector

def salle():
    try:        
        connexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="LaPlateforme"
        ) 
        curseur = connexion.cursor()
        curseur.execute("SELECT nom, capacite FROM salle")
        salle = curseur.fetchall()   
        print(salle)

    except mysql.connector.Error as e:
        print(f"Une erreur est survenue: {e}")
        
salle()