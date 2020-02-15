from set.set_class import *

def links_for_rank(g,graph, path):
    s=Set()
    for a in range(0, len(graph.vertices())):
        r = graph.vertices()[a]
        if g[r].__contains__(path):
            s.add(r,r)
    return s

class Graph(object):

    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    # vraca sve cvorove u grafu
    def vertices(self):
        return list(self.__graph_dict.keys())

    # vraca sve veze u grafu
    def edges(self):
        return self.__generate_edges()

    #dodaje novi cvor u graf
    def add_vertex(self, v):
        if v not in self.__graph_dict:
            self.__graph_dict[v] = []

    # dodaje novu vezu u graf
    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    # pravljene nove veze
    def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for n in self.__graph_dict[vertex]:
                if {n, vertex} not in edges:
                    edges.append({vertex, n})
        return edges

    #za ispis
    def __str__(self):
        res = "cvorovi: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nveze: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res