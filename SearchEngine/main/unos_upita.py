
def parsiraj_upit(upit, root):
    if " AND " in upit:
        text = upit.split(' ',3)
        a1,b1,c1 = root.find_word(text[0])
        a2, b2, c2 = root.find_word(text[2])
        print(c1)
        print(c2)
        if (len(c1) is 0 and len(c2) is 0):
            print("Oba prazna")
        elif len(c1) is 0:
            print(c2)
        elif len(c2) is 0:
            print(c1)
        else:
            print(c1.intersection(c2))

    elif " OR " in upit:
        text = upit.split(' ', 3)
        a1, b1, c1 = root.find_word(text[0])
        a2, b2, c2 = root.find_word(text[2])
        print(c1)
        print(c2)
        if (len(c1) is 0 and len(c2) is 0):
            print("Oba prazna")
        elif len(c1) is 0:
            print(c2)
        elif len(c2) is 0:
            print(c1)
        else:
            print(c1.union(c2))

    elif " NOT " in upit:
        text = upit.split(' ', 3)
        a1, b1, c1 = root.find_word(text[0])
        a2, b2, c2 = root.find_word(text[2])
        print(c1)
        print(c2)
        if (len(c1) is 0 and len(c2) is 0):
            print("Oba prazna")
        elif len(c1) is 0:
            print("Prazan skup")
        elif len(c2) is 0:
            print(c1)
        else:
            print(c1.difference(c2))

    elif " " not in upit:
        a1, b1, c1 = root.find_word(upit)
        print(c1)
    else:
        text = upit.split()
        print(text)
        flag = False

        for i in text:
            a1, b1, c1 = root.find_word(i)
            if (len(c1) is not 0 and flag is False):
                rez = c1
                flag = True
            if (len(c1) is not 0 and flag is True):
                rez.union(c1)

        if(flag is True):
            print(rez)
        else:
            print("Nema rezultata")
