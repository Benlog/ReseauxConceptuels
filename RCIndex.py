import bidict as bd

defaultCaracterList = [chr(i) for i in range(0, 0xFFFF)]


def create_base_caracter_index(base=None, index_to_caracter_tuple_list=None):
    """
    Créé ou met à jour l'index avec les correspondances de caractères

    :param base: bidict à mettre à jour, créer un bidict vide si None
    :type base: bidict
    :param index_to_caracter_tuple_list: liste de tuple (int, char) de 
        correspondance entre un index et un charactère
    :type index_to_caracter_tuple_list: list(tuple(int, char))
    """
    if base is None:
        base = bd.bidict()

    if index_to_caracter_tuple_list is None:
        index_to_caracter_tuple_list = [
            (i, j) for i, j in enumerate(defaultCaracterList)
        ]

    base.putall(index_to_caracter_tuple_list)
    return base


def merge_index(index_list):
    """Fusionne tout les bidict d'une liste et évite les id répétés

    Args:
        indexList (list): liste de bidict{id:elem}

    Returns:
        bidict: la liste fusionné de tout les bidict
    """

    base = index_list[0]
    id_set = set(base.keys())
    for i in index_list[1:]:
        id_max = max(id_set)
        for id, elem in i:
            if id in id_set:
                id_max += 1
                id = id_max
            base.put(id, elem)

    return base


# class TextGraphCreator():
#    '''
#    Class pour créer des chaines de lettres lié en suivant la
#    '''
#    def createALinkedChain(self, text):
