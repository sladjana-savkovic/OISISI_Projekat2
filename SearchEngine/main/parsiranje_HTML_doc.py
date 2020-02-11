import os
from graph.graph_class import Graph
from main.parser import Parser
from trie_stablo.stablo import TrieNode

def make_tree_and_graph(dirname):
    p = Parser()
    g = {}
    root = TrieNode('*')
    for cur, dirs, files in os.walk(dirname):
        for f in files:
            if ".html" in f:
                link, words = p.parse(os.path.join(cur,f))
                g[os.path.join(cur, f)] = link
                i = 0
                while i < len(words):
                    root.add(words[i], os.path.join(cur,f))
                    i += 1
    graph = Graph(g)
    return root,g,graph