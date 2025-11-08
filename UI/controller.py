import flet as ft
from UI.view import View
from model.model import Model


'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti

        #Queste variabili vengono continuamente aggiornate a seconda del valore
        #selezionato nella dropdown, contenuta nella view, dall'utente.
        #Ogni volta che viene effettuato un cambiamento, l'on change della DD passa
        #il valore selezionato al controller

        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN

    #La DD viene popolata mediante la funzione che segue, la quale
    #viene chiamata a seguito di "options". Dopo aver ottenuto dal model
    #la lista creo una nuova lista che poi viene passata alla view per rendere
    #visibili le opzioni all'utente

    def popola_dropdown(self):
        lista_provvisoria = self._model.get_musei()
        lista_nomi_musei = []
        lista_nomi_musei.append(ft.DropdownOption("Nessun Filtro"))

        for museo in lista_provvisoria:
            nome = museo.nome
            lista_nomi_musei.append(ft.DropdownOption(nome))

        return lista_nomi_musei

    def popola_dropdown_epoche(self):
        lista_provvisoria = sorted(self._model.get_epoche())
        lista_epoche = []
        lista_epoche.append(ft.DropdownOption("Nessun Filtro"))

        for epoca in lista_provvisoria:
            lista_epoche.append(ft.DropdownOption(epoca))

        return lista_epoche


    # CALLBACKS DROPDOWN

    #Funzioni che aggiornano i valori di museo ed epoca inizialmente = None

    def aggiorna_nome_museo(self,e):
        self.museo_selezionato = e.control.value
        #print(self.museo_selezionato)

    def aggiorna_epoca(self,e):
        self.epoca_selezionata = e.control.value
        #print(self.epoca_selezionata)


    # AZIONE: MOSTRA ARTEFATTI

    #Definisco la funzione per selezionare gli artefatti filtrati, che viene chiamata al premere
    #del bottone nella view, se l'utente non ha selezionato alcun valore viene restituito un messaggio
    #d'errore.

    #Quando la ricerca va a buon fine (file_dao -> model -> controller -> view) allora aggiungo
    #alla listview della view gli artefatti trovati, aggiorno la pagina, poi pulisco la listview.

    #Dopo aver pulito la listview, finchè la pagina non viene riaggiornata, i risultati della precedente
    #ricerca rimangono visibili all'utente. Chiamo un update per la pagina per pulirla solo prima
    #di mostrare la listview riempita con artefatti corrispondenti a una nuova richiesta.


    def mostra_artefatti(self, e):
        if self.museo_selezionato == None or self.epoca_selezionata == None:
            self._view.alert.show_alert("Selezionare valori dal menu.")
        else:
            self._view.update()
            lista_artefatti = self._model.get_artefatti_filtrati(self.museo_selezionato,self.epoca_selezionata)
            if len(lista_artefatti) == 0:
                self._view.alert.show_alert("Non ci sono artefatti trovati per la tua ricerca.")
            else:
                for artefatto in lista_artefatti:
                    #print(artefatto)
                    self._view.lista_risultati_ricerca.controls.append(ft.Text(artefatto))
                self._view.update()
                self._view.lista_risultati_ricerca.controls.clear()


