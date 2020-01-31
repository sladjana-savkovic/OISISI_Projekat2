from main.unos_upita import *
from graph.graph_class import *
from search_and_rank.pretraga_dokumenta import *
from search_and_rank.rangirana_pretraga import *
from trie_stablo import stablo


def main():
    path = 'C:\\Users\\pc\Desktop\\Stabla\\python-2.7.7-docs-html'
    root = stablo.make_tree(path)
    g,graph = make_graph(path)

    putanja = input("Unesite putanju do direktorijuma: ")
    upit = input("Unesite upit za pretragu: ")

    operator,words = parsiraj_upit(upit)

    result = pretraga_dokumenta(root,putanja,words,operator)
    print(result)

    dict = rang_pretraga(g,graph,words,result,operator)
    print(dict)

if __name__ == "__main__":
    main()