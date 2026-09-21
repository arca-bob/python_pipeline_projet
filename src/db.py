import sqlite3
from pathlib import Path

def init_db(db_path: Path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            datetime_transaction TEXT,
            iban_origine TEXT,
            pays_source TEXT,
            banque_source TEXT,
            iban_destinataire TEXT,
            pays_destinataire TEXT,
            montant TEXT,
            devise TEXT,
            UNIQUE(datetime_transaction, iban_origine, iban_destinataire, montant)
    );""")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS iban_origine_somme (
            iban_origine TEXT PRIMARY KEY,
            total TEXT
        );""")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS banque_source_somme (
            banque_source TEXT PRIMARY KEY,
            total TEXT
        );""")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS iban_dest_somme (
            iban_destinataire TEXT PRIMARY KEY,
            total TEXT
        );""" )

    conn.commit()
    conn.close()
def insert_data(db_path: Path, lignes, iban_som, banq_som, dest_som):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    for row in lignes:
        cur.execute("""
            INSERT OR IGNORE INTO transactions (
                datetime_transaction, iban_origine, pays_source, banque_source,
                iban_destinataire, pays_destinataire, montant, devise
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", row)

    for iban, total in iban_som.items():
        cur.execute("""
            INSERT OR REPLACE INTO iban_origine_somme (iban_origine, total)
            VALUES (?, ?)
        """, (iban, int(total)))

    for banque, total in banq_som.items():
        cur.execute("""
            INSERT OR REPLACE INTO banque_source_somme (banque_source, total)
            VALUES (?, ?)
        """, (banque, int(total)))

    for dest, total in dest_som.items():
        cur.execute("""
            INSERT OR REPLACE INTO iban_dest_somme (iban_destinataire, total)
            VALUES (?, ?)
        """, (dest, int(total)))

    conn.commit()
    conn.close()
