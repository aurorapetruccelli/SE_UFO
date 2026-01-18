import datetime
import networkx as nx
from geopy import distance
from database.dao import DAO


class Model:
    def __init__(self):
        self.G = nx.Graph()
        self.sightins=[]
        self.nodes = []
        self.state = []
        self.result = {}
        self.G = nx.Graph()


    def read_year(self):
        self.sightings = DAO.get_sightings()
        result = []
        for s in self.sightings:
            if s.s_datetime.year not in result:
                result.append(s.s_datetime.year)

        return result

    def read_shape(self,year):
        result = []
        for s in self.sightings:
            if s.shape not in result and s.s_datetime.year == year:
                result.append(s.shape)

        print(result)
        return result

    def crea_grafo(self,year,shape):
        self.nodes = DAO.get_states()
        for n in self.nodes:
            self.G.add_node(n.id)

        connessioni = DAO.get_connessioni(year,shape)

        self.G.add_weighted_edges_from(connessioni)


    def vicini(self):
        result = {}
        for n in self.G.nodes:
            result[n] = 0
            for v in self.G.neighbors(n):
                result[n]+= int(self.G[n][v]["weight"])
        print(result)
        return result

    def distanza(self,n,v):
        self.state = DAO.get_states_complete()
        dizionario = {}
        for s in self.state:
            dizionario[s.id] = s

        dis = distance.geodesic((dizionario[n].lat, dizionario[n].lng), (dizionario[v].lat, dizionario[v].lng)).km
        return dis

    def ricerca(self):
        self.peso_migliore = 0
        self.cammino_migliore=[]

        for n in self.G.nodes:
            partial_node = [n]
            partial_edges = []
            self.ricorsione(partial_node,partial_edges,0,0)

        print(f"{self.peso_migliore} {self.cammino_migliore}")
        return self.peso_migliore,self.cammino_migliore

    def ricorsione(self,partial_node,partial_edges,peso_corrente,peso_totale):
        # peso degli archi deve essere crescente
        # peso geodesic max
        ultimo_nodo = partial_node[-1]


        if peso_totale>self.peso_migliore:
            self.peso_migliore = peso_totale
            self.cammino_migliore = partial_edges.copy()


        for n in self.G.neighbors(ultimo_nodo):
            if self.G[ultimo_nodo][n]["weight"] > peso_corrente:
                partial_node.append(n)
                partial_edges.append((ultimo_nodo, n, self.G[ultimo_nodo][n]["weight"],self.distanza(ultimo_nodo, n)))
                self.ricorsione(partial_node,partial_edges,self.G[ultimo_nodo][n]["weight"],peso_totale+self.distanza(str(ultimo_nodo), str(n)))
                partial_node.pop()
                partial_edges.pop()
