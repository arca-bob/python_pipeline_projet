from decimal import Decimal

def load_csv(path):
    v = []
    i = []

    with open(path, encoding="utf-8") as f:
        next(f)

        for ligne in f:

            if not ligne.strip():
                continue

            cols = ligne.strip().split(",")

            try:

                if len(cols) != 8:
                    raise ValueError("Colonnes manquantes")

                date, iban_o, pays_o, banque, iban_d, pays_d, montant, devise = cols

                montant = Decimal(montant)
                montant_centimes = int(montant * 100)
                v.append([
                    date, iban_o, pays_o, banque,
                    iban_d, pays_d, montant_centimes, devise
                ])

            except Exception:
                i.append(ligne)

    return v, i
