import csv
from pathlib import Path
from decimal import Decimal

donnees = [
    [
        "2024-03-01T09:12:00",
        "FR7630006000011234567890189",
        "FR",
        "BNPPARIBAS",
        "DE89370400440532013000",
        "DE",
        Decimal("1250.00"),
        "EUR"
    ],
    [
        "2024-03-01T10:45:00",
        "FR7630006000011234567890189",
        "FR",
        "BNPPARIBAS",
        "ES9121000418450200051332",
        "ES",
        Decimal("7400.50"),
        "EUR"
    ],
    [
        "2024-03-01T11:00:00",
        "FR7630006000019876543210000",
        "FR",
        "LCL",
        "DE89370400440532013000",
        "DE",
        Decimal("8200.00"),
        "EUR"
    ],
    [
        "2024-03-01T11:15:00",
        "FR7630006000019876543210000",
        "FR",
        "SG",
        "ES9121000418450200051332",
        "ES",
        Decimal("450.00"),
        "EUR"
    ],
    [
        "2024-03-01T11:30:00",
        "FR7630006000011234567890189",
        "FR",
        "BNPPARIBAS",
        "DE89370400440532013000",
        "DE",
        Decimal("999.00"),
        "EUR"
    ]
]

def csv_genrator(donnees):
    output = Path("data")
    output.mkdir(exist_ok=True)

    for i in range(3):
        path = output / f"fichier{i+1}.csv"

        with path.open("w", newline="", encoding="utf-8") as fichier:
            writer = csv.writer(fichier)

            writer.writerow([
                "datetime_transaction",
                "iban_origine",
                "pays_source",
                "banque_source",
                "iban_destinataire",
                "pays_destinataire",
                "montant",
                "devise"
            ])

            for ligne in donnees:
                writer.writerow(ligne)

    return True