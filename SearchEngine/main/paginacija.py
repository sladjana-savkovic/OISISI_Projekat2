
def paginacija(list, n):
    i = 0
    while True:
        ispis(list,i,i+n)
        if i == 0:
            print("Sledeca(>)   Promjena broja stranica(*)   Kraj(0)")
        elif i >= len(list)-n:
            print("Prethodna(<)   Promjena broja stranica(*)   Kraj(0)")
        else:
            print("Prethodna(<)   Sledeca(>)   Promjena broja stranica(*)   Kraj(0)")
        a = input("Unos: ")
        if a == '<':  # korisnik unio <
            if i == 0:
                if a == '0':
                    print("Kraj...")
                    break
                else:
                    i = i + n
            i = i - n
        elif a == '>': #korisnik unio >
            if i >= len(list)-n:
                if a == '0':
                    print("Kraj...")
                    break
                else:
                    i = i - n
            i = i + n
        elif a == '*': #korisnik unio *
            if i < len(list) - n:
                i = i + n

            n = input("Unesite broj stranica za ispis: ")
            n = int(n)

        elif a == '0':
            print("Kraj...")
            break

def ispis(list,a,b):
    for i in range(a,b):
        if i < len(list) and i >= 0:
            print(str(list[i].page) + " " + str(list[i].rank))
