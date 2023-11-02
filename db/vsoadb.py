import sqlite3

# Import from the root of the project
from domain import vsoa
from domain import medewerker
import settings


def get_all_dossiers():
	with sqlite3.connect("project.db") as dbconnectie:
		resultaat = dbconnectie.execute("SELECT id, lid, type, verantwoordelijke FROM dossier")
		print(resultaat.fetchall())

# def get_medewerkers():
	# alle medewerkers opvragen

# def set_medewerkers():
	# medewerker toevoegen

# def set_dossier():
	# dossier toevoegen

