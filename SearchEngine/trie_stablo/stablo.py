"""
Modul sadrži implementaciju trie stabla.
"""
import os

from set.set_class import Set
from trie_stablo.queue import *
from main.parser import Parser
from collections import Counter

#Funkcija vraca broj pojavljivanja trazenih rijeci u nekom dokumentu
def find_word_document(word_list, path):
     p = Parser()
     result = [] #rezultujuci niz broja pojavljivanja
     br = 0 #broj ne nula elemenata u nizu
     link, words = p.parse(path)
     count = Counter(words)
     for i in range(0,len(word_list)):
         if count[word_list[i]] > 0:
             br += 1
         result.append(count[word_list[i]])
     return  result,br

class TrieNode(object):
    """
    Implementacija cvora trie stabla
    """

    def __init__(self, char: str):
        self.char = char #slovo koje cvor sadrzi
        self.children = [] #djeca cvora su predstavljena listom
        self.word_finished = False #oznaka za kraj rijeci
        self.link_set = Set() #skup linkova stranica u kojima se rijec nalazi
        self.counter = 0 #koliko puta se ista rijec javlja u dokumentu

    def add(self, word: str, link: str):
        """
        Dodavanje rijecu u trie stablo, ako znam link stranice u kojoj se rijec nalazi
        """
        node = self
        for char in word:
            found_in_child = False
            # Trazimo vrijednost cvorova koji su djeca cvora node
            for child in node.children:
                if child.char == char:
                    # Kada smo nasli takvo slovo, taj cvor postaje sledeci roditelj
                    node = child
                    found_in_child = True
                    break
            # Nismo nasli takav cvor pa ga dodajemo kao novo dijete
            if not found_in_child:
                new_node = TrieNode(char)
                node.children.append(new_node)
                # Novi roditelj je cvor koji smo dodali
                node = new_node
        # Dodavanje je zavrseno
        node.word_finished = True
        node.link_set.add(link)
        node.counter += 1

    def find_word(self, word: str):
        node = self
        # Ako je stablo prazno, vracamo False
        if not self.children:
            return False, 0, {}
        for char in word:
            char_not_found = True
            # Prolazi kroz djecu cvora node
            for child in node.children:
                if child.char == char:
                    char_not_found = False
                    node = child
                    break
            if char_not_found:
                return False, 0, {}
        return True, node.counter, node.link_set



    def breath_first(self):
        node = self
        if not node.children:
            print("")
            return

        to_visit = Queue()
        to_visit.enqueue(node)

        while not to_visit.is_empty():
            e = to_visit.dequeue()
            print(e.char)
            for s in e.link_set:
                print(s)

            for child in e.children:
                to_visit.enqueue(child)


