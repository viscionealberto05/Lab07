from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    @staticmethod
    def leggi_musei():
        results = []
        cnx = ConnessioneDB.get_connection()

        if cnx is None:
            print("Connection failed")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * 
                       FROM museo"""
            cursor.execute(query)
            for row in cursor:
                museo = Museo(row["id"],row["nome"],row["tipologia"])
                results.append(museo)
            cursor.close()
            cnx.close()
            return results

