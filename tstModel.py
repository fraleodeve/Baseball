from model.model import Model

mymodel = Model()

mymodel.getTeamsOfYear(1984)
mymodel.buildGraph(1984)
nodi, archi = mymodel.getGraphDetails()

print(f"Grafo Creato! Il grafo ha {nodi} nodi e {archi} archi.")

