import sqlite3

# Import from the root of the project
from domain import vsoa
from domain import medewerker
import settings


def get_all_dossiers():
    try:
        with sqlite3.connect("../project.db") as dbconnectie:
            mijncursor = dbconnectie.cursor()
            mijncursor.execute("SELECT id, lid, type, verantwoordelijke FROM dossier")
            resultaat = mijncursor.fetchall()
            return resultaat
    except sqlite3.Error as e:
        print("Fout bij het ophalen van dossiers:", str(e))
        return None

def get_all_medewerkers():
    try:
        with sqlite3.connect("../project.db") as dbconnectie:
            mijncursor = dbconnectie.cursor()
            mijncursor.execute("SELECT id, naam FROM medewerker")
            resultaat = mijncursor.fetchall()
            return resultaat
    except sqlite3.Error as e:
        print("Fout bij het ophalen van medewerkers:", str(e))
        return None

def set_medewerker(medewerker):
    try:
        # Medewerker toevoegen
        with sqlite3.connect("../project.db") as dbconnectie:
            mijncursor = dbconnectie.cursor()
            query = "INSERT INTO medewerker (naam) VALUES (?)"
            mijncursor.execute(query, (medewerker,))
            dbconnectie.commit()
    except sqlite3.Error as e:
        print("Fout bij het toevoegen van medewerker:", str(e))

def set_dossier(lid, dossier_type, verantwoordelijke):
    try:
        # Dossier toevoegen
        with sqlite3.connect("../project.db") as dbconnectie:
            mijncursor = dbconnectie.cursor()
            query = "INSERT INTO dossier (lid, type, verantwoordelijke) VALUES (?, ?, ?)"
            mijncursor.execute(query, (lid, dossier_type, verantwoordelijke))
            dbconnectie.commit()
    except sqlite3.Error as e:
        print("Fout bij het toevoegen van dossier:", str(e))

