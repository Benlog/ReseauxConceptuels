from abc import ABC, abstractmethod

class AbcReseauConceptuel(ABC) :
    '''
    Classe de base pour les réseaux conceptuels

    Un réseau conceptuel est un réseau dont les arcs sont décrit par un noeud
    En simplifié c'est une liste de triplet (origine, moyen, destination) décrivant les arrêtes entre les noeuds
    (un peu comme RDF mais avec la différence que les moyens (prédicats) sont des noeuds et les relations sont ordonnées au sein de (origine, moyen))
    '''

    def __init__(self):
        super().__init__()

    @abstractmethod
    def addRelation(self, fro, by, to):
        '''
        Ajoute une relation au graphe à la fin de l'ordre

        :param fro: id du noeud origine
        :type fro: entier
        :param by: id du noeud moyen
        :type by: entier
        :param to: id du noeud destination
        :type to: entier
        '''
        pass
        
    @abstractmethod
    def getRelationsOf(self, fro):
        '''
        Donne l'ensemble des doublés (moyen, destination) du noeud donné en paramètre
        Renvois ''KeyError'' si le noeuds oringine n'existe pas

        :param fro: id du noeud origine
        :type fro: entier
        :return: liste de doublé (moyen, [destinations])
        :rtype: iterable of tuple
        '''
        pass

    @abstractmethod
    def removeFirstRelation(self, fro, by, to):
        '''
        Retire la dernière relation donnée en paramètre
        Renvois ''KeyError'' si la relation n'existe pas

        :param fro: id du noeud origine
        :type fro: entier
        :param by: id du noeud moyen
        :type by: entier
        :param to: id du noeud destination
        :type to: entier
        '''
        pass
        
class SimpleReseauConceptuel(AbcReseauConceptuel) :

    def __init__(self):
        self.data = dict()
        
    def addRelation(self, fro, by, to):
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
        
    def getRelationsOf(self, fro):
        '''
        Donne l'ensemble des doublés (moyen, destination) du noeud donné en paramètre
        Renvois ''KeyError'' si le noeuds oringine n'existe pas

        :param fro: id du noeud origine
        :type fro: entier
        :return: liste de doublé (moyen, [destinations])
        :rtype: iterable of tuple
        '''
        return [ (b[0], b[1].copy()) for b in self.data[fro].items()]


    def removeFirstRelation(self, fro, by, to):
        '''
        Retire la dernière relation donnée en paramètre
        Renvois ''KeyError'' si la relation n'existe pas

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
        except ValueError:
            raise KeyError((fro, by, to))
        if b == [] :
            a.pop(by)
            if a == {} :
                self.data.pop(fro)
        else :
            a[by] = b
            self.data[fro] = a