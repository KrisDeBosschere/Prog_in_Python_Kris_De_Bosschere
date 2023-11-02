import sys
import os

# Add the path to the master folder to sys.path
master_folder = r"C:\Users\krisd\pythonscripts\Prog_in_Python_Kris_De_Bosschere"
sys.path.append(master_folder)

# Now, you can import modules from other directories
from db import vsoadb
from domain import vsoa
from domain import medewerker
import settings
import sqlite3

print(vsoadb.get_all_dossiers())
