from main.unos_upita import *
from search_and_rank.pretraga_dokumenta import *
from search_and_rank.rangirana_pretraga import *
from main.parsiranje_HTML_doc import *
from search_and_rank.sortiranje_dokumenata import *
from main.paginacija import *

def main():
    option = 0
    while True:
        if option == 0:
            path = input("Unesite putanju korijenskog direktorijuma: ")
            root, g = make_tree_and_graph(path)
            if root.check_depth() == 0 or isfile(path):
                print("Putanja nije odgovarajuća. Stablo pretrage je prazno.")
                continue
            option += 1
        if option == 1:
            upit = input("Unesite upit za pretragu: ")
            operator, words = parsiraj_upit(upit)
            if operator is None and words is None:
                print("Upit je u pogrešnom formatu!")
                continue
            option += 1
        if option == 2:
            result = pretraga_dokumenta(root, words, operator,g)
            if result is None:
                option = 4
            else:
                option += 1
        if option == 3:
            try:
                n = input("Unesite broj stranica za ispis: ")
                n = int(n)
                option += 1
            except ValueError:
                print("Pogrešan format broja!")
                continue
        if option == 4:
            if result is not None:
                try:
                    s = input("Izaberite način sortiranja (rastući rang - 1 / opadajući rang - 0): ")
                    s = int(s)
                    if s != 0 and s != 1:
                        continue
                except ValueError:
                    print("Pogrešan format za sortiranje!")
                    continue

                list = rang_pretraga(g, words, result, operator, root)
                quickSort(list, 0, len(list) - 1, s)
                paginacija(list, n)
            else:
                print("Nije pronadjena ni jedna stranica koja odgovara Vašem upitu.")

            while True:
                print("\nPromjena korijenskog direktorijuma(!)      Novi upit(?)        Promjena načina sortiranja(/)       Kraj(0)")
                a = input()
                if a == '!':
                    option = 0
                    break
                elif a == '?':
                    option = 1
                    break
                elif a == '/':
                    option = 4
                    break
                elif a == '0':
                    option = 5
                    break

            if option == 5:
                break

if __name__ == "__main__":
     main()

