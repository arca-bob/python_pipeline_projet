import csv
from pathlib import Path

def generer_fichier_test(iban_som, banq_som, dest_som, dossier_sortie: Path):
    dossier_sortie.mkdir(exist_ok=True)

    with open(dossier_sortie / "iban_origine_somme.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["iban_origine", "total"])
        for iban, total in iban_som.items():
            writer.writerow([iban, int(total)])

    with open(dossier_sortie / "banque_source_somme.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["banque_source", "total"])
        for banque, total in banq_som.items():
            writer.writerow([banque, int(total)])

    with open(dossier_sortie / "iban_dest_somme.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["iban_destinataire", "total"])
        for dest, total in dest_som.items():
            writer.writerow([dest, int(total)])
