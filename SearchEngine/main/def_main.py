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
            print("Upit je u pogrešnom formatu!")
            continue
        parser_time = (time.time() - start_time)

        while True:
            try:
                n = input("Unesite broj stranica za ispis: ")
                n = int(n)
                break
            except ValueError:
                print("Pogrešan format broja!")

        start_time = time.time()
        result = pretraga_dokumenta(root,words,operator)
        search_time = (time.time() - start_time)

        #Nema rezultata pretrage za uneseni upit
        if result is None:
            option = 0
            #while petlja za slucaj da korisnik unese neki drugi simbol
            print("Nije pronadjena ni jedna stranica koja odgovara Vašem upitu.")
            while option is 0:
                    print("Novi upit(?)     Promjena korijenskog direktorijuma(!)      Kraj(0)")
                    a=input()
                    if a == '?':
                        option = 1
                    elif a == '!':
                        option = 2
                    elif a == '0':
                        option = 3
                        break
            if option is 1:
                continue
            elif option is 2:
                path = input("Unesite putanju korijenskog direktorijuma: ")
                start_time = time.time()
                root, g, graph = make_tree_and_graph(path)
                tree_graph_time = (time.time() - start_time)
                continue
            elif option is 3:
                print("\n\n---Tree and graph time: %s seconds ---" % round(tree_graph_time, 2))
                print("\n---Parser time: %s seconds ---" % round(parser_time, 2))
                print("\n---Search time: %s seconds ---" % round(search_time, 2))
                print("\n---SUM time: %s seconds ---" % round(
                    (tree_graph_time + parser_time + search_time), 2))
                break

        start_time = time.time()
        list = rang_pretraga(g, graph, words, result, operator,root)
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

        print("\nNovi upit(?)     Promjena korijenskog direktorijuma(!)     Kraj(0)")
        a = input()

        if a == '?':
            continue
        elif a == '!':
            path = input("Unesite putanju korijenskog direktorijuma: ")
            start_time = time.time()
            root, g, graph = make_tree_and_graph(path)
            tree_graph_time = (time.time() - start_time)
            continue
        elif a == '0':
            break

        #STAVITI U WHILE PETLJU!

if __name__ == "__main__":
    main()
