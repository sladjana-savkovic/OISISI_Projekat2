
def parsiraj_upit(upit):
    # povratna vrijednost je operator i lista parsiranih rijeci
    words = []
    upit = upit.strip() #uklanjanje razmaka sa pocetka i kraja upita
    upit = upit.lower() #pretvaranje stringa u mala slova zbog insensitive pretrage

    if " " not in upit:
        if upit in ['and','or','not']:
            return None,None
        words.append(upit)
        return None, words
    else:
        text = upit.split() #split po whitespace karakterima
        #Primjer upita: not Python
        if (text[0] == "not") and (len(text) == 2) and (text[1] not in ['and','or','not']):
            words.append(text[1])
            return text[0],words
        #Primjer upita: Python and Java
        elif (text[1] in ['and','or','not']) and (len(text) == 3) \
                and (text[0] not in ['and','or','not']) and (text[2] not in ['and','or','not']):
            words.append(text[0])
            words.append(text[2])
            return text[1],words
        #Primjer upita: python java
        elif ("and" not in text) and ("or" not in text) and ("not" not in text):
            return None,text
        #Pogresan upit: and and Java
        else:
            return None,None