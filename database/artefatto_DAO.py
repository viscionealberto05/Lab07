from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    @staticmethod
    def leggi_epoche():
        results = []
        cnx = ConnessioneDB.get_connection()

        if cnx is None:
            print("Connection failed")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT epoca
                       FROM artefatto"""
            cursor.execute(query)
            for row in cursor:
                epoca = row["epoca"]
                results.append(epoca)
            cursor.close()
            cnx.close()
            return results

    @staticmethod
    def trova_artefatti(museo:str, epoca:str):
        results = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Connection failed")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)

            if museo == epoca == "Nessun Filtro":
                query = """SELECT * FROM artefatto"""
                cursor.execute(query)
                for row in cursor:
                    artefatto = row["nome"]
                    results.append(artefatto)
                cursor.close()
                cnx.close()
                return results

            elif museo == "Nessun Filtro":
                query = """SELECT a.nome 
                            FROM artefatto a, museo m
                            WHERE m.id = a.id_museo AND a.epoca = %s"""
                cursor.execute(query, (epoca,))
                for row in cursor:
                    artefatto = row["nome"]
                    results.append(artefatto)
                cursor.close()
                cnx.close()
                return results

            elif epoca == "Nessun Filtro":
                query = """SELECT a.nome 
                            FROM artefatto a, museo m
                            WHERE m.id = a.id_museo AND m.nome = %s"""
                cursor.execute(query, (museo,))
                for row in cursor:
                    artefatto = row["nome"]
                    results.append(artefatto)
                cursor.close()
                cnx.close()
                return results

            else:
                query = """SELECT a.nome 
                            FROM artefatto a, museo m
                            WHERE  m.id = a.id_museo AND m.nome = %s AND a.epoca = %s"""
                cursor.execute(query, (museo, epoca,))
                for row in cursor:
                    artefatto = row["nome"]
                    results.append(artefatto)
                cursor.close()
                cnx.close()
                return results