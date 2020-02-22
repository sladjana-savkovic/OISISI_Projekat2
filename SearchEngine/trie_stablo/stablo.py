"""
Modul sadrži implementaciju trie stabla.
"""
from set.set_class import Set
from trie_stablo.queue import *
from main.parser import Parser
from collections import Counter

#Metoda vraca broj pojavljivanja trazenih rijeci u nekom dokumentu i broj nenultih
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
     return result,br

class TrieNode(object):
    """
    Implementacija cvora trie stabla
    """

    def __init__(self, char):
        self.char = char #slovo koje cvor sadrzi
        self.children = [] #djeca cvora su predstavljena listom
        self.link_dict = Set() #rjecnik linkova stranica u kojima se rijec nalazi i broj pojavljivanja svake rijeci u stranici

    def add(self, word, link):
        """
        Dodavanje rijeci u trie stablo, ako znam link stranice u kojoj se rijec nalazi
        """
        node = self
        for char in word:
            flag = False #Pretpostavka da nismo nasli takvo slovo
            # Trazimo vrijednost cvorova koji su djeca cvora node
            for child in node.children:
                if child.char == char:
                    # Kada smo nasli takvo slovo, taj cvor postaje sledeci roditelj
                    node = child
                    flag = True
                    break
            # Nismo nasli takav cvor pa ga dodajemo kao novo dijete
            if not flag:
                new_node = TrieNode(char)
                node.children.append(new_node)
                # Novi roditelj je cvor koji smo dodali
                node = new_node

        if link not in node.link_dict.ret_key():
            node.link_dict.add(link,1)
        else:
            node.link_dict.inc_value(link)

    #Metoda koja vraca skup stranica u kojima se nalazi trazena rijec i broj pojavljivanja svake rijeci u stranici
    def find_word(self, word):
        node = self
        #Ako je stablo prazno vracam prazan skup
        if not self.children:
            return {}
        for char in word:
            flag = True
            # Prolazi kroz djecu cvora node
            for child in node.children:
                if child.char == char:
                    flag = False
                    node = child
                    break
            if flag:
                return {}

        return node.link_dict

    #Metoda za obilazak stabla po sirini i ispis svakog cvora
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

            print('*****')
            print(e.link_dict)
            print('*****')

            for child in e.children:
                to_visit.enqueue(child)

    def check_depth(self):
        if len(self.children) == 0:
            return 0
        else:
            return 1

