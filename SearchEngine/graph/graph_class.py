from main.parser import Parser
import os

def make_graph(dirname):
    p = Parser()

    g={}
    for r,d,f in os.walk(dirname):
        for file in f:
            if ".html" in file:
                link,word=p.parse(os.path.join(r,file))
                g[os.path.join(r,file)] = link

    graph=Graph(g)
    return g,graph

def links_for_rank(g,graph, path):
    br = 0
    s=set()
    for a in range(0, len(graph.vertices())):
        r = graph.vertices()[a]
        if g[r].__contains__(path):
            br += 1
            s.add(r)

    return br,s

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
    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    # dodaje novu vezu u graf
    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
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

    #funkcija koja vraca sve putanje od jednog do drugog cvora
    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex,
                                                     end_vertex,
                                                     path)
                for p in extended_paths:
                    paths.append(p)
        return paths