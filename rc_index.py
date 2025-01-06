"""Index creation and tools for conceptual networks."""
from typing import List, Optional
from bidict import bidict
from reseaux_conceptuels_simple import SimpleReseauConceptuelSimple

# Constants
DEFAULT_CHAR_LIST = [chr(i) for i in range(0, 0xFFFF)]
CONTAINS_ID = 0  # ID for "contains" relationship
NEXT_ELEM_ID = 1  # ID for "next element" relationship

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
            (i, j) for i, j in enumerate(DEFAULT_CHAR_LIST,
            start=max(id_set)+1)
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


def create_linked_chain_graph(graph: SimpleReseauConceptuelSimple,
                            id_list: List[int],
                            contain_id: int,
                            next_elem_id: int,
                            first_id: Optional[int] = None) -> None:
    """Generate a linked chain graph to store IDs.
    
    Args:
        graph: Conceptual network to add the linked chain
        id_list: List of IDs to store
        contain_id: ID of the "contains" relationship
        next_elem_id: ID of the "next element" relationship 
        first_id: ID of first element (uses graph.max+1 if None)
    """
    if first_id is None :
        first_id = graph.max + 1

    curent_id = first_id

    for elem in id_list:
        graph.add_relation(curent_id, contain_id, elem)
        curent_id += 1
        graph.add_relation(curent_id-1, next_elem_id, curent_id)

    return



# class TextGraphCreator():
#    '''
#    Class pour créer des chaines de lettres lié en suivant la
#    '''
#    def createALinkedChain(self, text):
