from trie_stablo.stablo import find_word_document
from graph.graph_class import links_for_rank

class Element(object):

    def __init__(self, page, rank):
        self.page = page
        self.rank = rank


def rang_pretraga(g, graph, words, result, operator,root):
    list = []

    if result is None:
        return None

    for page in result:
        r1,r2,r3 = 0,0,0
        broj_rijeci,broj_nenultih=find_word_document(words,page)
        linkovi = links_for_rank(g,graph,page)

        if operator == "NOT":
            r1 = broj_rijeci[0]
        else:
            r1 = sum(broj_rijeci)/len(broj_rijeci) * broj_nenultih/len(broj_rijeci)
            if broj_nenultih == len(broj_rijeci):
                r1=r1*2

        r2=len(linkovi)

        for i in range(0,len(words)):
            d = root.find_word(words[i])
            p = d & linkovi
            for j in p.ret_key():

                if operator=='NOT':
                    if i==0 and d.ret_val(j)==0:
                        r3+=d.ret_val(j)/100
                    elif i==1 and d.ret_val(j)!=0:
                        r3 += d.ret_val(j)/100
                    else:
                        r3 += d.ret_val(j)

                elif operator=='AND':
                    if d.ret_val(j)==0:
                        r3 += d.ret_val(j)/100
                    else:
                        r3 += d.ret_val(j)

                elif operator=='OR' or (operator is None and len(words)>=1):
                    if d.ret_val(j)!=0:
                        r3 += d.ret_val(j)
                    else:
                        r3 += d.ret_val(j)/100
        r3=r3/100
        if r2 is not 0:
            r3 = r3/r2

        average_rank=round(r1*(1.0/2) + r2*(1.0/3) + r3*(1.0/6),2)

        e = Element(page, average_rank)
        list.append(e)

    return list