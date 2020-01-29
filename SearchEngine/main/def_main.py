from parser import *

from main.parser import Parser
from trie_stablo import stablo
from main.unos_upita import *

def main():
    p = Parser()
    link, words = p.parse('C:/Users/pc/Desktop/Stabla/python-2.7.7-docs-html/about.html')

    root = stablo.make_tree()

    putanja = input("Unesite putanju do direktorijuma: ")
    upit = input("Unesite upit za pretragu: ")

    parsiraj_upit(upit,root)

if __name__ == "__main__":
    main()