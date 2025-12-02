from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = DAO.read_hub()
        hubs_dict = {hub.id: hub for hub in self._nodes}
        self._edges = DAO.read_spedizione(hubs_dict)
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        # TODO
        self._nodes = DAO.read_hub()
        hubs_dict = {hub.id: hub for hub in self._nodes}
        self._edges = DAO.read_spedizione(hubs_dict)

        for hub in self._nodes:
            self.G.add_node(hub)

        for t in self._edges:
            if t.peso >= threshold:
                 self.G.add_edge(t.hub1, t.hub2, weight=t.peso)



    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        return len(self._edges)



    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        return len(self._nodes)

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        for t in self._edges:
            return t.hub1, t.hub2, t.peso




