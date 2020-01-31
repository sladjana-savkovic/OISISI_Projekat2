from trie_stablo.stablo import find_word_document
from graph.graph_class import links_for_rank

def rang_pretraga(g, graph, words, result, operator):
    dict = {}

    for page in result:
        r1,r2,r3 = 0,0,0
        broj_rijeci,broj_nenultih=find_word_document(words,page)
        linkovi = links_for_rank(g,graph,page)
        r2=len(linkovi)

        for l in linkovi:
            r, b = find_word_document(words,l)
            if operator == "NOT":
                r3 += sum(r)
            else:
                r3 += sum(r)/len(r)
        r3 = r3/r2

        if operator == "NOT":
            r1 = broj_rijeci[0]
        else:
            r1 = sum(broj_rijeci)/len(broj_rijeci) * broj_nenultih/len(broj_rijeci)

        average_rank=r1*(1.0/2) + r2*(1.0/3) + r3*(1.0/6)

        dict[page] = average_rank

    return dict