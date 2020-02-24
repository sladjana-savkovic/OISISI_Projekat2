from set.set_class import *

def links_for_rank(g, path):
    s=Set()
    for r in g.vertices():
        if path in g.ret_edge(r):
            s.add(r,0)
    return s

class Graph(object):

    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    # vraca sve cvorove u grafu
    def vertices(self):
        return list(self.__graph_dict.keys())

    def add_vertex(self, v):
        if v not in self.__graph_dict.keys():
            self.__graph_dict[v] = []

    def add_edge(self,v,e):
        if v in self.vertices():
            self.__graph_dict[v] = e

    def ret_edge(self,v):
        if v in self.vertices():
            return list(self.__graph_dict[v])
        return None

    def __str__(self):
        a=""
        for v in self.vertices():
           a += str(v) + " " + str(self.ret_edge(v)) + "\n"
        return a