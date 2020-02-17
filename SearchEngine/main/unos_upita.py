
def parsiraj_upit(upit):
    words = []

    if " " not in upit:
        if upit.upper() in ['AND','OR','NOT']:
            return None,None
        words.append(upit)
        return None, words
    else:
        text = upit.split(' ')
        #Primjer upita: NOT Python
        if (text[0].upper() == "NOT") and (len(text) is 2) and (text[1].upper() not in ['AND','OR','NOT']):
            words.append(text[1])
            return text[0],words
        #Primjer upita: Python AND Java
        elif (text[1].upper() in ['AND','OR','NOT']) and (len(text) is 3) \
                and (text[0].upper() not in ['AND','OR','NOT']) and (text[2].upper() not in ['AND','OR','NOT']):
            words.append(text[0])
            words.append(text[2])
            return text[1],words
        #Primjer upita: python java
        elif ("AND" not in text) and ("OR" not in text) and ("NOT" not in text) \
                and ("and" not in text) and ("or" not in text) and ("not" not in text):
            return None,text
        #Pogresan upit: and AND Java
        else:
            return None,None