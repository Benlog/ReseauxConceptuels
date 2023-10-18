"""Création et outils d'index"""
from bidict import bidict
from reseauxConceptuelsSimple import SimpleReseauConceptuelSimple as SRCS

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
        base = bidict()
        id_set = set([0])
    else :
        id_set = set(base.keys())

    if index_to_caracter_tuple_list is None:
        index_to_caracter_tuple_list = [
            (i, j) for i, j in enumerate(defaultCaracterList, start=max(id_set)+1)
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
        for id_elem, elem in i.items():
            if id_elem in id_set:
                id_max += 1
                id_elem = id_max
            base.put(id_elem, elem)

    return base

# éléments de base du graphe:
#    1 : sujet (contient) objet
#    2 : sujet (type) objet
#    3 : sujet (element suivant) objet


def create_linked_chain_graph(graph, id_list_to_store, contain_id, next_elem_id, first_id = None):
    """Gènère un graphe de type liste chainer pour stocker les id de id_list_to_store

    Args:
        graph (SRCS): réseau conceptuel auquel ajouter la liste chainé
        contain_id (int): id de l'élément contient
        next_elem_id (int): id de l'élément élément suivant
        id_list_to_store (list[int]): liste des id à stocker dans cette liste
        first_id (int): id du 1er élément de la liste, sera mis à graph.max si vide
    """
    if first_id is None :
        first_id = graph.max + 1

    curent_id = first_id

    for elem in id_list_to_store:
        graph.add_relation(curent_id, contain_id, elem)
        curent_id += 1
        graph.add_relation(curent_id-1, next_elem_id, curent_id)

    return





# class TextGraphCreator():
#    '''
#    Class pour créer des chaines de lettres lié en suivant la
#    '''
#    def createALinkedChain(self, text):
