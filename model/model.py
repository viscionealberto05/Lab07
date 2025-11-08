from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):

        #Inizializzazione ad attributi delle classi MuseoDAO e ArtefattoDAO
        #Così da poter interagire con il db secondo, i parametri provenienti dal controller
        #che a sua volta li legge dalla view

        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""

        #Per trovare gli artefatti che soddisfano la richiesta dell'utente uso artefatto_dao
        #che comunica con il DB permettendomi di eseguire delle query SQL. Le interrogazioni filtrano
        #esattamente leggendo i valori di epoca e museo che provengono dalla view e che con l'on change
        #sono stati restituiti al controller, il quale ha chiamato il model.

        lista_artefatti = self._artefatto_dao.trova_artefatti(museo, epoca)
        return lista_artefatti

    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""

        #Interrogazione SQL con cui ottengo la lista di tutte le epoche per cui
        #esistono artefatti associati

        lista_epoche = ArtefattoDAO.leggi_epoche()
        return lista_epoche

    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""

        #Interrogazione SQL con cui ottengo la lista dei nomi dei musei

        lista_musei = MuseoDAO.leggi_musei()
        return lista_musei

