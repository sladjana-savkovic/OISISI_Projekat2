from parser import *

from main.parser import Parser
from trie_stablo import stablo
from main.unos_upita import *
from graph.graph_class import *
from trie_stablo.stablo import find_word_document
from search_and_rank.pretraga_dokumenta import *


def main():
    p = Parser()
    link, words = p.parse('C:/Users/pc/Desktop/Stabla/python-2.7.7-docs-html/about.html')

    path = 'C:\\Users\\pc\Desktop\\Stabla\\python-2.7.7-docs-html'
    root = stablo.make_tree(path)
    make_graph(path)

    putanja = input("Unesite putanju do direktorijuma: ")
    upit = input("Unesite upit za pretragu: ")

    operator,words = parsiraj_upit(upit)

    result = pretraga_dokumenta(root,putanja,words,operator)

    print(result)

    # print(root.find_word('QA1067'))

    # print(find_word_document('these', 'C:\\Users\\pc\\Desktop\\Stabla\\python-2.7.7-docs-html\\about.html'))

if __name__ == "__main__":
    main()