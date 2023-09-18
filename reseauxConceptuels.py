from abc import ABC, abstractmethod
from reseauxConceptuelsSimple import AbcReseauConceptuelSimple

class AbcReseauConceptuel(AbcReseauConceptuelSimple) :
    '''
    Classe de base abstraite pour les réseaux conceptuels plus complets

    Un réseau conceptuel est un réseau dont les arcs sont décrit par un noeud
    En simplifié c'est une liste de triplet (origine, moyen, destination) ou autrement dit (objet, prédicat, valeur) décrivant les arrêtes entre les noeuds
    (un peu comme RDF mais avec la différence que les moyens (prédicats) sont des noeuds et les relations sont ordonnées au sein de (origine, moyen))

    Ces réseaux sont plus complets et peuvent récupérer les liste de relation par objet, mais aussi par prédicat ou valeur
    '''

    @abstractmethod
    def get_relations_of_predicat(self, by):
        '''
        Donne l'ensemble des doublés (objet, destination) du noeud donné en paramètre
        Renvois 'KeyError' si le noeuds origine n'existe pas

        :param by: id du noeud origine
        :type by: entier
        :return: liste de doublé (objets, destinations)
        :rtype: iterable of tuple
        '''
        raise NotImplementedError
    
    @abstractmethod
    def get_relations_of_value(self, to):
        '''
        Donne l'ensemble des doublés (objet, moyen) du noeud donné en paramètre
        Renvois 'KeyError' si le noeuds origine n'existe pas

        :param to: id du noeud origine
        :type to: entier
        :return: liste de doublé (objets, moyen)
        :rtype: iterable of tuple
        '''
        raise NotImplementedError
    
    #TODO
    #add method for retreive list of id from a double like (from,by), (from,to) or (by,to)
        
class SimpleReseauConceptuel(AbcReseauConceptuel) :
    '''Implémentation simple de la classe abstraite avec des objets standard de python'''

    def __init__(self):
        self.data = dict()
        
    def add_relation(self, fro, by, to):
        '''
        Ajoute une relation au graphe à la fin de l'ordre

        :param fro: id du noeud origine
        :type fro: entier
        :param by: id du noeud moyen
        :type by: entier
        :param to: id du noeud destination
        :type to: entier
        '''
        a = self.data.get(fro, {by : []})
        b = a.get(by, [])
        b.append(to)
        a[by] = b
        self.data[fro] = a
        
    def get_relationsOf(self, fro):
        '''
        Donne l'ensemble des doublés (moyen, destination) du noeud donné en paramètre
        Renvois 'KeyError' si le noeuds oringine n'existe pas

        :param fro: id du noeud origine
        :type fro: entier
        :return: liste de doublé (moyen, [destinations])
        :rtype: iterable of tuple
        '''
        return [ (b[0], b[1].copy()) for b in self.data[fro].items()]


    def remove_first_relation(self, fro, by, to):
        '''
        Retire la dernière relation donnée en paramètre
        Renvois 'KeyError' si la relation n'existe pas

        :param fro: id du noeud origine
        :type fro: entier
        :param by: id du noeud moyen
        :type by: entier
        :param to: id du noeud destination
        :type to: entier
        '''
        a = self.data[fro]
        b = a[by]
        try :
            b.remove(to)
        except ValueError as valueError:
            raise KeyError(str((fro, by, to)) + "not in network") from valueError
        if b == [] :
            a.pop(by)
            if a == {} :
                self.data.pop(fro)
        else :
            a[by] = b
            self.data[fro] = a