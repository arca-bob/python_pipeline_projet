def traitement(lignes):
    iban_som = {}
    banq_som = {}
    dest_som = {}

    for row in lignes:
        iban_or = row[1]
        banque_so = row[3]
        iban_dest = row[4]
        montant = row[6]

        iban_som[iban_or] = iban_som.get(iban_or, 0) + montant
        banq_som[banque_so] = banq_som.get(banque_so, 0) + montant
        dest_som[iban_dest] = dest_som.get(iban_dest, 0) + montant

    return iban_som, banq_som, dest_som
