import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDGenre(self):
        try:
            self._view._ddGenre.options.clear()
            generi = self._model.getAllGeneri()
            for y in generi:
                self._view._ddGenre.options.append(ft.dropdown.Option(y))
                    #key=actor.id,
                #text=actor.name))
        except Exception as ex:
            self._view._txt_result.controls.append(
                ft.Text(f"Errore nel recupero dei GENERI: {ex}", color="red"))
        self._view.update_page()

    def handleCreaGrafo(self, e):
        pass

    def handleCreaGrafo(self,e):
        pass

    def handleCammino(self,e):
        pass