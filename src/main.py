from pathlib import Path
from chargement import load_csv
from traitement import traitement
from db import init_db, insert_data
from sortie_generation import generer_fichier_test

def main():

    csv_path = Path("../data/fichier1.csv")
    db_path = Path("../data/base.db")
    dossier_sortie = Path("../data/sortie")

    csv_path.parent.mkdir(parents=True, exist_ok=True)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    dossier_sortie.mkdir(parents=True, exist_ok=True)

    init_db(db_path)

    lignes_valides, lignes_invalides = load_csv(csv_path)
    print(f"{len(lignes_invalides)} invalides")

    if not lignes_valides:
        print("Pas de ligne valide")
        return
    
    iban_som, banq_som, dest_som = traitement(lignes_valides)
    insert_data(db_path, lignes_valides, iban_som, banq_som, dest_som)
    generer_fichier_test(iban_som, banq_som, dest_som, dossier_sortie)

    print("Pipeline fini")

if __name__ == "__main__":
    main()