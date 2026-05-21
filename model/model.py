import itertools
import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._teams = []
        self._idMapTeams = {}

    # minuto 50:00
    def getPath(self):
        pass

    def _ricorsione(self):
        pass

    def buildGraph(self, year):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._teams)

        # arco tra ogni nodo del grafo
        # for u in self._grafo.nodes():
            # for v in self._grafo.nodes():
                # if u != v:
                    # self._grafo.add_edge(u, v)

        # in alternativa usa combinations (libreria python)
        myEdges = list(itertools.combinations(self._teams, 2)) # prendo team 2 a 2 -> restituisce lista di tuple
        self._grafo.add_edges_from(myEdges) # add_edges_from vuole lista di tuple

        mapSalary = DAO.getSalariesTeam(year, self._idMapTeams)

        for e in self._grafo.edges():
            salario1 = mapSalary[e[0]]
            salario2 = mapSalary[e[1]]
            peso = salario1 + salario2
            self._grafo[e[0]][e[1]]["weight"] = peso # eventualmente tutta una riga

    def getAllYears(self):
        return DAO.getAllYears()

    def getTeamsOfYear(self, year):
        self._teams = DAO.getTeamsOfYear(year)
        self._idMapTeams = {t.ID: t for t in self._teams}
        return self._teams

    def getGraphDetails(self):
        return len(self._grafo.nodes()), len(self._grafo.edges())

    def getVicini(self, source):
        vicini = self._grafo.neighbors(source)
        viciniTuple = []
        for v in vicini:
            viciniTuple.append((v, self._grafo[source][v]["weight"]))

        viciniTuple.sort(key=lambda x: x[1], reverse=True)
        return viciniTuple
