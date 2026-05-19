import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._choiceTeam = None

    def handleCreaGrafo(self, e):
        self._model.buildGraph()
        n, m = self._model.getGraphDetails()

        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(
            ft.Text(f"Grafo correttamente creato! Il grafo contiene {n} nodi e {m} archi"))
        self._view.update_page()

    def handleDettagli(self, e):
        pass

    def handlePercorso(self, e):
        pass

    def fillDDYears(self):
        years = self._model.getAllYears()

        # yearsDD = []
        # for y in years:
             # yearsDD.append(ft.dropdown.Option(y))

        yearsDD = list(map(lambda x: ft.dropdown.Option(x), years)) # importante mettere list(map(...))
        # altrimenti non sarebbe permamente
        self._view._ddAnno.options = yearsDD
        self._view.update_page()

    def handleYearSelection(self, e):
        # quando viene selezionato un anno, deve recuperare i team che hanno giocato in quell'anno,
        # stamparli nel textfield e riempire il dropdown

        if self._view._ddAnno.value is None:
            self._view._txtOutSquadre.controls.clear()
            self._view._txtOutSquadre.controls.append(ft.Text("Selezionare un anno dal menu."))
            self._view.update_page()

        teams = self._model.getTeamsOfYear(self._view._ddAnno.value)
        self._view._txtOutSquadre.controls.clear()
        self._view._txtOutSquadre.controls.append(
            ft.Text(f"Nel {self._view._ddAnno.value} sono iscritte {len(teams)} squadre."))
        for t in teams:
            self._view._txtOutSquadre.controls.append(ft.Text(f"{t}"))
            self._view._ddSquadra.options.append(ft.dropdown.Option(data = t,
                                                                    text = t.name,
                                                                    on_click = self.readDDTeams))
        self._view.update_page()

    def readDDTeams(self, e):
        if e.controls.data is None:
            self._choiceTeam = None
        else:
            self._choiceTeam = e.controls.data

        print(f"Squadra selezionata: {self._choiceTeam}")
