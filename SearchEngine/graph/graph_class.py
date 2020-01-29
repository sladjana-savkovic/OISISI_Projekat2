from main.parser import Parser

def make_graph():
    p = Parser()
    link,word=p.parse('C:\\Users\\Jelena\\Desktop\\za_projekat\\python-2.7.7-docs-html\\about.html')

    g = {'C:\\Users\\Jelena\\Desktop\\za_projekat\\python-2.7.7-docs-html\\about.html': link,
         }

    graph=Graph(g)
    print(graph)

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