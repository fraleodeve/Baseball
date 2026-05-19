import itertools
import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._teams = []

    def buildGraph(self):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._teams)

        # arco tra ogni nodo del grafo
        # for u in self._grafo.nodes():
            # for v in self._grafo.nodes():
                # if u != v:
                    # self._grafo.add_edge(u, v)

        # in alternativa usa combinations (libreria python)
        myEdges = itertools.combinations(self._teams, 2) # prendo team 2 a 2 -> restituisce lista di tuple
        self._grafo.add_edges_from(myEdges) # add_edges_from vuole lista di tuple

    def getAllYears(self):
        return DAO.getAllYears()

    def getTeamsOfYear(self, year):
        self._teams = DAO.getTeamsOfYear(year)
        return self._teams

    def getGraphDetails(self):
        return len(self._grafo.nodes()), len(self._grafo.edges())