'''outils pour faire des stats'''

def compte_ngram(ngram, liste):
    """compte les ngram (1 ou plusieurs éléments à la suite) dans une liste

    Args:
        ngram (iter[T]): le ngram (1 ou plusieurs éléments à la suite) à compter dans la liste
        liste (iter[T]): la liste ou compter les ngram

    Returns:
        int : nombre d'occurence de ngram dans la liste
    """

    total = 0
    for i,_ in enumerate(liste):
        condition_all = True
        for n in ngram:
            if not n == liste[i]:
                condition_all = False
                break
            i += 1
        if condition_all:
            total += 1

    return total

def liste_tout_ngram(liste):
    """_summary_

    Args:
        liste (list[T]): _description_

    Returns:
        set[T]: _description_
    """

    ngram_temp = []
    for e in liste:
        ngram_temp.append([e])
        for e2 in ngram_temp[:-1]:
            e2.append(e)

    ngram_set = set()
    for e in ngram_temp:
        ngram_set.add(tuple(e))

    return ngram_set


def liste_tout_adjacents(liste):
    length = len(liste)

    return [[[liste[i3+i2] for i3 in range(length - i)] for i2 in range(i+1)] for i in range(length)]    
