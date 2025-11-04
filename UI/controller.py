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
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
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
    def aggiorna_nome_museo(self,e):
        self.museo_selezionato = e.control.value
        #print(self.museo_selezionato)

    def aggiorna_epoca(self,e):
        self.epoca_selezionata = e.control.value
        #print(self.epoca_selezionata)


    # AZIONE: MOSTRA ARTEFATTI
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


