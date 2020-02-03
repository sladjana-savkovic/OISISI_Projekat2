from trie_stablo.stablo import find_word_document
from graph.graph_class import links_for_rank


class Element(object):

    def __init__(self, page, rank):
        self.page = page
        self.rank = rank


def rang_pretraga(g, graph, words, result, operator):
    list = []

    if result is None:
        return None

    for page in result:
        r1, r2, r3 = 0, 0, 0
        broj_rijeci, broj_nenultih = find_word_document(words, page)
        linkovi = links_for_rank(g, graph, page)
        r2 = len(linkovi)

        for l in linkovi:
            r, b = find_word_document(words, l)
            if operator == "NOT":
                r3 += sum(r)
            else:
                r3 += sum(r) / len(r)
        r3 = r3 / r2

        if operator == "NOT":
            r1 = broj_rijeci[0]
        else:
            r1 = sum(broj_rijeci) / len(broj_rijeci) * broj_nenultih / len(broj_rijeci)

        average_rank = round(r1 * (1.0 / 2) + r2 * (1.0 / 3) + r3 * (1.0 / 6), 2)

        e = Element(page, average_rank)
        list.append(e)

    return list