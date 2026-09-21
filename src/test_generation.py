import csv
from pathlib import Path
from sortie_generation import generer_fichier_test

def test_generation():

    iban_som = {"FR1": 300, "FR2": 300}
    banq_som = {"BNP": 300, "LCL": 300}
    dest_som = {"DE1": 300, "DE2": 300}

    dossier = Path("data/test_sortie")
    dossier.mkdir(parents=True, exist_ok=True)

    generer_fichier_test(iban_som, banq_som, dest_som, dossier)

    assert (dossier / "iban_origine_somme.csv").exists()
    assert (dossier / "banque_source_somme.csv").exists()
    assert (dossier / "iban_dest_somme.csv").exists()

    with open(dossier / "iban_origine_somme.csv", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    assert ["FR1", "300"] in rows
    assert ["FR2", "300"] in rows
