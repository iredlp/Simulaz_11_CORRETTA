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
        genere = self._view._ddGenre.value

        if not genere:
            self._view.create_alert("Selezionare il GENERE prima di creare il grafo.", color="red")
            return
        # try:
        # v1 = float(self._view._txtRatingMin.value.replace(",", "."))
        # v2 = float(self._view._txtRatingMax.value.replace(",", "."))
        # except (ValueError, AttributeError):
        # self._view.create_alert("Inserisci due valori numerici validi per la valutazione.")
        # return
        # v1 = self._view._txtRatingMin.value
        # v2 = self._view._txtRatingMax.value

        try:
            self._model.creaGrafo(genere)
            n_nodes = self._model.get_num_nodes()
            n_edges = self._model.get_num_edges()
            # Stampa immediata numero di vertici e archi (Punto 1.c)
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(
                ft.Text(f"Grafo creato con successo!\nNumero vertici: {n_nodes}\nNumero archi: {n_edges}",
                        color="green"))
            # RIEMPIO IL DROPDOWN DEI FILM DEL GRAFO
            self.fillDDArtisti(genere)
        except Exception as ex:
            self._view._txt_result.controls.append(
                ft.Text(f"Errore durante la creazione del grafo: {ex}", color="red"))
            # return

        top5 = self._model.getTop5Archi()
        self._view._txt_result.controls.append(ft.Text(f"Archi di peso maggiore", color="green"))

        for i, arco in enumerate(top5, start=1):
            a1, a2, dati = arco
            self._view._txt_result.controls.append(ft.Text(
                f"{i})  {a1.Name}  ({a1.ArtistId}) -- {a2.Name}  ({a2. ArtistId} )"
                f"(peso: {dati['weight']})")
            )
        top = self._model.getTop5ArchiInfluenz()
        # self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"  Arco influenza max: {top}", color="green"))

        self._view.update_page()


    def fillDDArtisti(self, genere):
        try:
            self._view._ddArtist.options.clear()
            attori = self._model.getAllNodes(genere)
            for actor in attori:
                self._view._ddArtist.options.append(ft.dropdown.Option(key=actor.ArtistId,
                                                                         text=actor.Name))
        # self._view.update_page()
        except Exception as ex:
            self._view._txt_result.controls.append(
                ft.Text(f"Errore nel recupero degli ARTISTI: {ex}", color="red"))

        self._view.update_page()

    def handleCammino(self,e):
        self._view._txt_result.controls.clear()
        if self._model.get_num_nodes() == 0 or self._model.get_num_edges() is None:
            self._view.create_alert("Creare prima il grafo!", color="red")
            return
        pass