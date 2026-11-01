import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.DiGraph()  # grafo semplice
        self._idMapA = {}

    def getAllGeneri(self):
        return DAO.getAllGeneri()

    def creaGrafo(self, genere):
        self._grafo.clear()
        self._idMapA.clear()

        artista = DAO.getAllNodes(genere)
        for a in  artista:
            self._idMapA[a.ArtistId] = a
            self._grafo.add_node(a)
            # aggiungo i nodi
        print("2 - Nodi aggiunti")

        for a in artista:
            a.list_clienti.clear()
            a.popolarita = 0
            # a.clientiPerArtista = set(DAO.getClientiPerArtista(a.ArtistId))
            a.list_clienti = DAO.getClientiPerArtista(a.ArtistId, genere)
            a.popolarita = DAO.getPopolarita(a.ArtistId, genere)
        print("3 - Informazioni recuperate")

        for i in range(len( artista)):
            a1 =  artista[i]
            p1=a1.popolarita
            for j in range(i + 1, len( artista)):
                a2 =  artista[j]
                p2=a2.popolarita
                clientiComuni = (set(a1.list_clienti) & set(a2.list_clienti ))
              #  peso = 0
                #ND: & FUNZIONA SOLO CON I SET! SE HAI LE LISTE CONSERVTILE IN SET E POI CONFRONTALE
              #  for film in  clientiComuni:
               #     incasso=DAO.getIncassiPerFilm(film)
                #    peso+=incasso[0]
                if len(  clientiComuni) > 0 and a1!=a2:
                    peso=p1+p2
                    if p1 > p2:
                        self._grafo.add_edge(a1, a2, weight=peso)
                    elif p2 > p1:
                        self._grafo.add_edge(a2, a1, weight=peso)

                    else:
                        self._grafo.add_edge(a1, a2, weight=peso)
                        self._grafo.add_edge(a2, a1, weight=peso)


    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

    def get_num_nodes(self) -> int:
        return self._grafo.number_of_nodes()

    def get_num_edges(self) -> int:
        return self._grafo.number_of_edges()


