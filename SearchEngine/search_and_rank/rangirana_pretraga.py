from graph.graph_class import links_for_rank

class Element(object):

    def __init__(self, page, rank):
        self.page = page
        self.rank = rank

def scale_number(unscaled, to_min, to_max, from_min, from_max):
    return (to_max-to_min)*(unscaled-from_min)/(from_max-from_min)+to_min

def scale_list(l, to_min, to_max):
    return [scale_number(i, to_min, to_max, min(l), max(l)) for i in l]

def rang_pretraga(g, words, result, operator,root):
    list=[]

    r1,r2,r3=[],[],[]
    if operator in ["and", "not"]:
        r1 = result.ret_all_val()

    for page in result:
        links = links_for_rank(g,page)
        r2.append(len(links))

        if operator not in ["and", "not"]:
            broj_rijeci, broj_nenultih = root.find_word_document(words, page)
            r1.append(sum(broj_rijeci) * broj_nenultih / len(broj_rijeci))

        p = result & links
        if p is not None:
            r3.append(sum(p.ret_all_val()))
        else:
            r3.append(0)

    if len(result) > 1:
        if sum(r1)!=0:
            r1 = scale_list(r1,0,30)
        if sum(r2)!=0:
            r2 = scale_list(r2,0,20)
        if sum(r3)!=0:
            r3 = scale_list(r3,0,50)

    i=0
    for page in result:
        list.append(Element(page, round(r1[i]+r2[i]+r3[i],2)))
        i+=1

    return list