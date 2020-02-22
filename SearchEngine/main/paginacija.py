
def paginacija(list, n):
    i = 0
    while True:
        ispis(list,i,i+n)
        if len(list) <= 1 or len(list) == n:
            print("Kraj paginacije(0)")
        elif i == 0:
            print("Broj preostalih stranica: " + str(len(list) - n))
            print("Sledeca(>)   Promjena broja stranica(*)   Kraj paginacije(0)")
        elif i >= len(list)-n:
            print("Broj preostalih stranica: 0")
            print("Prethodna(<)   Promjena broja stranica(*)   Kraj paginacije(0)")
        else:
            print("Broj preostalih stranica: " + str(len(list) - i - n))
            print("Prethodna(<)   Sledeca(>)   Promjena broja stranica(*)   Kraj paginacije(0)")
        a = input()
        if a == '<':  # korisnik unio <
            if i == 0:
                if a == '0':
                    break
                else:
                    i = i + n
            i = i - n
        elif a == '>': #korisnik unio >
            if i >= len(list)-n:
                if a == '0':
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
            break

def ispis(list,a,b):
    for i in range(a,b):
        if i < len(list) and i >= 0:
            print(str(list[i].page) + " " + str(list[i].rank))

