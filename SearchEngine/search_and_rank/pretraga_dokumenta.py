import os
from main.parser import Parser
from set.set_class import *


def pretraga_dokumenta(root,path,words,operator):
    #Rezultat pretrage je skup stranica koje zadovoljavaju upit
    result = Set()
    p = Parser()
    #path_set sadrzi sve putanje od unesenog direktorijuma zajedno sa njegovim poddirektorijumima
    path_set = Set()
    for cur, dirs, files in os.walk(path):
        for f in files:
            if ".html" in f:
                path_set.add(os.path.join(cur,f))

    op_set = Set()
    if operator == "AND":
        a1, b1, c1 = root.find_word(words[0])
        a2, b2, c2 = root.find_word(words[1])
        if len(c1) is 0 or len(c2) is 0:
            return None
        else:
            op_set = c1 & c2
    if operator == "OR":
        a1,b1,c1 = root.find_word(words[0])
        a2, b2, c2 = root.find_word(words[1])
        if len(c1) is 0 and len(c2) is 0:
            return None
        elif len(c1) is 0:
            op_set = c2
        elif len(c2) is 0:
            op_set = c1
        else:
            op_set = c1 | c2
    if operator == "NOT":
        a1, b1, c1 = root.find_word(words[0])
        a2, b2, c2 = root.find_word(words[1])
        if (len(c1) is 0 and len(c2) is not 0) or (len(c1) is 0 and len(c2) is 0):
            return None
        elif len(c1) is not 0 and len(c2) is 0:
            op_set = c1
        else:
            op_set = c1 - c2
    else:
        flag = False
        for i in words:
            a1, b1, c1 = root.find_word(i)
            if len(c1) is not 0 and flag is False:
                rez = c1
                flag = True
            if len(c1) is not 0 and flag is True:
                rez = rez | c1

        if flag is True:
            op_set = rez
        else:
            op_set = None

    if (path_set is None) or (op_set is None):
        result = None
    else:
        result = op_set & path_set

    return result