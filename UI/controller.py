import flet as ft
import networkx as nx


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

        self._list_shape=[]

    def populate_dd(self):
         #Metodo per popolare i dropdown
        option = self._model.read_year()
        self._view.dd_year.options = [ft.dropdown.Option(str(o)) for o in option]

        self._view.page.update()

    def choice_year(self,e):
        self._populate_dd_shape()

    def _populate_dd_shape(self):
        self._list_shape = self._model.read_shape(int(self._view.dd_year.value))

        for shape in self._list_shape:
            self._view.dd_shape.options.append(ft.dropdown.Option(shape))

        self._view.update()

    def handle_graph(self, e):
        #Handler per gestire creazione del grafo
        year = int(self._view.dd_year.value)
        shape = str(self._view.dd_shape.value)
        self._model.crea_grafo(year,shape)

        self._view.lista_visualizzazione_1.controls.clear()
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f" Numero nodi: {nx.number_of_nodes(self._model.G)} Numero archi: {nx.number_of_edges(self._model.G)}"))

        dizionario_vicini=self._model.vicini()
        for chiave,valore in dizionario_vicini.items():
            self._view.lista_visualizzazione_1.controls.append(ft.Text(f"Nodo: {chiave} somma dei pesi su archi {valore}"))

        self._view.page.update()

    def handle_path(self, e):
        peso,cammino = self._model.ricerca()
        self._view.lista_visualizzazione_2.controls.clear()
        self._view.lista_visualizzazione_2.controls.append(ft.Text(f"Peso cammino max: {peso}"))
        for c in cammino:
            self._view.lista_visualizzazione_2.controls.append(ft.Text(f"{c[0]}--> {c[1]}: weight {c[2]} distance {c[3]}"))

        self._view.page.update()
