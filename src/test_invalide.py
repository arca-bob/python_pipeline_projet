import tempfile
from chargement import load_csv
from sortie_generation import generer_fichier_test
import csv
from pathlib import Path

def test_lignes_invalides():

    contenu = """date;iban_o;pays_o;banque;iban_d;pays_d;montant;devise
                2024-01-01;FR1;FR;BNP;DE1;DE;100;EUR
                2024-01-02;FR2;FR;LCL;DE2;DE;abc;EUR 
                2024-01-03;FR3;FR;SG;DE3;DE;200;EUR
            """

    with tempfile.NamedTemporaryFile("w+", delete=False, encoding="utf-8") as f:
        f.write(contenu)
        f.flush()
        chemin = f.name

    valides, invalides = load_csv(chemin)

    assert len(valides) == 2
    assert len(invalides) == 1
    assert "abc" in invalides[0]


def test_ignore_invalides(tmp_path):

    iban_som = {"FR1": 100, "FR3": 200}
    banq_som = {"BNP": 100, "SG": 200}
    dest_som = {"DE1": 100, "DE3": 200}

    dossier = tmp_path / "sortie"
    generer_fichier_test(iban_som, banq_som, dest_som, dossier)

    assert (dossier / "iban_origine_somme.csv").exists()

    with open(dossier / "iban_origine_somme.csv", newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    assert ["FR1", "100"] in rows
    assert ["FR3", "200"] in rows
    assert not any("abc" in row for row in rows)


def test_ignore_invalides(tmp_path):
    iban_som = {"FR1": 100, "FR3": 200}
    banq_som = {"BNP": 100, "SG": 200}
    dest_som = {"DE1": 100, "DE3": 200}

    dossier = tmp_path / "sortie"
    generer_fichier_test(iban_som, banq_som, dest_som, dossier)

    assert (dossier / "iban_origine_somme.csv").exists()

    with open(dossier / "iban_origine_somme.csv", newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    assert ["FR1", "100"] in rows
    assert ["FR3", "200"] in rows
    assert not any("abc" in row for row in rows)
