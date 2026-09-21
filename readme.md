Le projet charge les données, valide les lignes, calcule les agrégats, l’insert dans une base SQLite, génère un fichiers de sortie

Pour gérer les lignes invalide j'ai choisi:

les lignes invalides sont ignorées, les fichiers de sortie ne contiene pas les lignes invalides

Por gérer l'Idempotence j'ai utilisé:

des contraintes UNIQUE dans SQLite, INSERT OR IGNORE pour les transactions, INSERT OR REPLACE pour les agrégats


pour lancer le projet il faut utiliser la commande python generation.py afin de creer les fichier d'entré puis python main.py pour lancer la pipeline

pour lancer les tests il faut utiliser la commance pytest

Benjamin Dupille