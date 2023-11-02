import sys
import os

# Add the path to the master folder to sys.path
master_folder = r"C:\Users\krisd\pythonscripts\Prog_in_Python_Kris_De_Bosschere"
sys.path.append(master_folder)

# import modules from other directories
from db import vsoadb
from domain import vsoa
from domain import medewerker
import settings
import sqlite3


keuze = input("Wat zou je willen doen? \n Alle dossiers opvragen, typ 1 \n Alle medewerkers opvragen, typ 2 \n Een medewerker toevoegen, typ 3 \n Een dossier toevoegen, typ 4 \n Een csv bestand krijgen van alle dossiers, typ 5 \n ")
if keuze not in ('1','2','3','4','5'):
	print("Je gaf een verkeerde input!")
else :
	print(f"Je koos voor {keuze}")

