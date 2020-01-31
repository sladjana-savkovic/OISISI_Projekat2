
def parsiraj_upit(upit):

    words = []
    if (" AND " in upit) or (" OR " in upit) or (" NOT " in upit):
        text = upit.split(' ',3)
        operator = text[1]
        words.append(text[0])
        words.append(text[2])
        return text[1],words
    elif " " not in upit:
        #Upit sadrzi samo jednu rijec
        words.append(upit)
        return None,words
    else:
        #Upit sadrzi vise rijeci
        text = upit.split()
        return None,text