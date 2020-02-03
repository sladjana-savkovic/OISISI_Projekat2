import os
from graph.graph_class import Graph
from main.parser import Parser
from trie_stablo.stablo import TrieNode

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

def make_tree(dirname):
    p = Parser()
    root = TrieNode('*')
    for cur, dirs, files in os.walk(dirname):
        for f in files:
            if ".html" in f:
                link, words = p.parse(os.path.join(cur,f))
                i = 0
                while i < len(words):
                    root.add(words[i], os.path.join(cur,f))
                    i += 1
    return root