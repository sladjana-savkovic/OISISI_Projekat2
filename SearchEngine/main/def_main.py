import time
from main.unos_upita import *
from search_and_rank.pretraga_dokumenta import *
from search_and_rank.rangirana_pretraga import *
from main.parsiranje_HTML_doc import *
from search_and_rank.sortiranje_dokumenata import *
from main.paginacija import *

def main():
    putanja = input("Unesite putanju do direktorijuma: ")
    upit = input("Unesite upit za pretragu: ")
    n = input("Unesite broj stranica za ispis: ")
    n = int(n)
    path = 'C:\\Users\\pc\Desktop\\Stabla\\python-2.7.7-docs-html'

    start_time = time.time()
    root,g,graph = make_tree_and_graph(path)
    tree_graph_time = (time.time() - start_time)

    start_time = time.time()
    operator,words = parsiraj_upit(upit)
    parser_time = (time.time() - start_time)

    start_time = time.time()
    result = pretraga_dokumenta(root,putanja,words,operator)
    search_time = (time.time() - start_time)

    start_time = time.time()
    list = rang_pretraga(g, graph, words, result, operator)
    rank_time = (time.time() - start_time)

    start_time = time.time()
    quickSort(list,0,len(list)-1)
    sort_time = (time.time() - start_time)

    paginacija(list, n)

    print("\n\n---Tree and graph time: %s seconds ---" % round(tree_graph_time,2))
    print("\n---Parser time: %s seconds ---" % round(parser_time,2))
    print("\n---Search time: %s seconds ---" % round(search_time,2))
    print("\n---Rank time: %s seconds ---" % round(rank_time,2))
    print("\n---Sort time: %s seconds ---" % round(sort_time,2))
    print("\n---SUM time: %s seconds ---" % round((tree_graph_time+parser_time+search_time+rank_time+sort_time),2))

if __name__ == "__main__":
    main()
