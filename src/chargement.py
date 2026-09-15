import csv
from decimal import Decimal
from pathlib import Path

def load_csv(path: Path):

    l = []

    with path.open("r", newline="", encoding="utf-8") as fichier:
        reader = csv.reader(fichier)

        next(reader)

        for row in reader:

            row[6] = Decimal(row[6])
            l.append(row)

    return l