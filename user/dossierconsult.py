import sys
import os
import sqlite3
import csv
import pandas as pd

# Voeg het pad naar de hoofdmap toe aan sys.path
master_folder = r"C:\Users\krisd\pythonscripts\Prog_in_Python_Kris_De_Bosschere"
sys.path.append(master_folder)

# Importeer modules uit andere mappen
from db import vsoadb
from domain.dossier import Dossier
from domain.medewerker import Medewerker
import settings

def main():
    keuze = input("Wat zou je willen doen? \n Alle dossiers opvragen, typ 1 \n Alle medewerkers opvragen, typ 2 \n Een medewerker toevoegen, typ 3 \n Een dossier toevoegen, typ 4 \n Een CSV-bestand krijgen van alle dossiers, typ 5 \n ")

    if keuze not in ('1', '2', '3', '4', '5'):
        print("Je gaf een verkeerde input!")
    else:
        print(f"Je koos voor {keuze}")

    if keuze == '1':
        dossiers = vsoadb.get_all_dossiers()
        if dossiers:
            for dossier in dossiers:
                print(dossier)
        else:
            print("Geen dossiers gevonden.")

    elif keuze == '2':
        medewerkers = vsoadb.get_all_medewerkers()
        if medewerkers:
            for medewerker in medewerkers:
                print(medewerker)
        else:
            print("Geen medewerkers gevonden.")

    elif keuze == '3':
        naam = input("Voer de naam van de medewerker in: ")
        # maak een nieuw medewerker object aan
        nieuwe_medewerker = Medewerker(naam)
        # Voeg het medewerker object toe aan de database
        vsoadb.set_medewerker(nieuwe_medewerker.naam)
        print("Medewerker toegevoegd.")

    elif keuze == '4':
        lid = input("Voer het lid in: ")
        dossier_type = input("Voer het type in: ")
        verantwoordelijke = input("Voer de verantwoordelijke in: ")
        # Maak een nieuw dossier-object aan
        nieuw_dossier = Dossier(lid, dossier_type, verantwoordelijke)
        # Voeg het dossier-object toe aan de database
        vsoadb.set_dossier(nieuw_dossier.lid, nieuw_dossier.type, nieuw_dossier.verantwoordelijke)
        print("Dossier toegevoegd aan de database.")

    elif keuze == '5':
        dossiers = vsoadb.get_all_dossiers()
        if dossiers:
            # Maak een gegevensframe van de dossiersgegevens
            df = pd.DataFrame(dossiers, columns=["id", "lid", "type", "verantwoordelijke"])
        
            # Exporteer naar een CSV-bestand
            df.to_csv("dossiers.csv", index=False)
            print("CSV-bestand 'dossiers.csv' gegenereerd.")
        
            # Exporteer naar een Excel-bestand
            df.to_excel("dossiers.xlsx", index=False)
            print("Excel-bestand 'dossiers.xlsx' gegenereerd.")
        else:
            print("Geen dossiers gevonden om naar CSV en Excel te exporteren.")
    
    else:
        pass

if __name__ == "__main__":
    main()