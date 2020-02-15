import time
from main.unos_upita import *
from search_and_rank.pretraga_dokumenta import *
from search_and_rank.rangirana_pretraga import *
from main.parsiranje_HTML_doc import *
from search_and_rank.sortiranje_dokumenata import *
from main.paginacija import *

def main():
    path = input("Unesite putanju korijenskog direktorijuma: ")
    start_time = time.time()
    root, g, graph = make_tree_and_graph(path)
    tree_graph_time = (time.time() - start_time)

    while True:
        upit = input("Unesite upit za pretragu: ")

        start_time = time.time()
        operator,words = parsiraj_upit(upit)
        #Ako je pogresan upit
        if operator is None and words is None:
            print("Upit je u pogresnom formatu!")
            continue
        parser_time = (time.time() - start_time)

        n = input("Unesite broj stranica za ispis: ")
        n = int(n)

        start_time = time.time()
        result = pretraga_dokumenta(root,words,operator)
        search_time = (time.time() - start_time)

        #Nema rezultata pretrage za uneseni upit
        if result is None:
            option = 0
            while option is 0:
                    print("Nije pronadjena ni jedna stranica koja odgovara Vašem upitu.")
                    a = input("Ponovi pretragu (?)      Kraj(0)")
                    if a == '0':
                        option = 2
                        break
                    elif a == '?':
                        option = 1
            if option is 1:
                path = input("Unesite putanju korijenskog direktorijuma: ")
                start_time = time.time()
                root, g, graph = make_tree_and_graph(path)
                tree_graph_time = (time.time() - start_time)
                continue
            elif option is 2:
                break

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
