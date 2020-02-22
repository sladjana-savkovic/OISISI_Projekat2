
def temp(niz, l, h, sort):
    i = (l - 1)
    pivot = niz[h].rank #pivot

    for j in range(l, h):
        if sort == 0:
            if niz[j].rank >= pivot:
                i = i + 1
                niz[i], niz[j] = niz[j], niz[i]
        else:
            if niz[j].rank <= pivot:
                i = i + 1
                niz[i], niz[j] = niz[j], niz[i]

    niz[i + 1], niz[h] = niz[h], niz[i + 1]
    return (i + 1)

def quickSort(niz, l, h, sort):
    if l < h:
        p = temp(niz, l, h, sort)

        quickSort(niz, l, p - 1, sort)
        quickSort(niz, p + 1, h, sort)