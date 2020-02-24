from set.set_class import *

def pretraga_dokumenta(root,words,operator,graph):
    #Rezultat pretrage je skup stranica koje zadovoljavaju upit
    result = Set()

    if len(words) == 1 and str(operator) == 'not':
        r = root.find_word(words[0])
        if len(r) != 0:
            for e in graph.vertices():
                if e not in r.ret_key():
                    result.add(e, 0)
        else:
            for e in graph.vertices():
                result.add(e, 0)
        if len(result) == 0:
            result = None

    #Upit se sastoji iz maksimalno dvije rijeci i operatora
    elif str(operator) in ['and','or','not']:
        #Odredjivanje skupa HTML stranica koje sadrze pojedinacne rijeci upita
        c1 = root.find_word(words[0])
        c2 = root.find_word(words[1])

        if str(operator) == "and":
            if len(c1) == 0 or len(c2) == 0:
                return None
            else:
                result = c1 & c2
        elif str(operator) == "or":
            if len(c1) == 0 and len(c2) == 0:
                return None
            elif len(c1) == 0:
                result = c2
            elif len(c2) == 0:
                result = c1
            else:
                result = c1 | c2
        elif str(operator) == "not":
            if (len(c1) == 0 and len(c2) != 0) or (len(c1) == 0 and len(c2) == 0):
                return None
            elif len(c1) != 0 and len(c2) == 0:
                result = c1
            else:
                result = c1 - c2
    #Upit se sastoji iz vise rijeci
    else:
        # Odredjivanje skupa HTML stranica koje sadrze pojedinacne rijeci upita
        flag = False
        for word in words:
            c1 = root.find_word(word)
            #Naisli smo na prvu rijec koja se nalazi u stablu
            if len(c1) != 0 and flag is False:
                rez = c1
                flag = True
            #Naisli smo na jos neku rijec koja se nalazi u stablu
            if len(c1) != 0 and flag is True:
                rez = rez | c1

        if flag is True:
            result = rez
        else:
            result = None

    return result
