import os
from os.path import isfile, isdir
from graph.graph_class import Graph
from main.parser import Parser
from trie_stablo.stablo import TrieNode

def make_tree_and_graph(f):
    p = Parser()
    g = Graph()
    root = TrieNode('*')

    recursive_walk(f, p, g, root)
    return root,g

def recursive_walk(f,p,g,root):

    if isfile(f) is not False and ".html" in f: #f je html fajl
        link, words = p.parse(f)
        g.add_vertex(f)
        g.add_edge(f,link)
        i = 0
        while i < len(words):
            root.add(words[i], f)
            i += 1

    elif isdir(f) is not False:  #f je direktorijum
        for dir in os.listdir(f):
            recursive_walk(os.path.join(f,dir),p,g,root)


