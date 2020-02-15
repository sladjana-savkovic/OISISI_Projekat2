from set.set_class import *

def pretraga_dokumenta(root,words,operator):
    #Rezultat pretrage je skup stranica koje zadovoljavaju upit
    result = Set()

    #Upit se sastoji iz dvije rijeci i operatora
    if operator in ['AND','OR','NOT']:
        #Odredjivanje skupa HTML stranica koje sadrze pojedinacne rijeci upita
        c1 = root.find_word(words[0])
        c2 = root.find_word(words[1])
        if operator == "AND":
            if len(c1) is 0 or len(c2) is 0:
                return None
            else:
                result = c1 & c2
        elif operator == "OR":
            if len(c1) is 0 and len(c2) is 0:
                return None
            elif len(c1) is 0:
                result = c2
            elif len(c2) is 0:
                result = c1
            else:
                result = c1 | c2
        elif operator == "NOT":
            if (len(c1) is 0 and len(c2) is not 0) or (len(c1) is 0 and len(c2) is 0):
                return None
            elif len(c1) is not 0 and len(c2) is 0:
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
            if len(c1) is not 0 and flag is False:
                rez = c1
                flag = True
            #Naisli smo na jos neku rijec koja se nalazi u stablu
            if len(c1) is not 0 and flag is True:
                rez = rez | c1

        if flag is True:
            result = rez
        else:
            result = None

    return result
