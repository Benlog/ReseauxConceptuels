"""Module des réseaux conceptuels de base"""
from abc import ABC, abstractmethod


class AbcReseauConceptuelSimple(ABC):
    """
    Classe de base abstraite pour les réseaux conceptuels

    Un réseau conceptuel est un réseau dont les arcs sont décrit par un noeud
    En simplifié c'est une liste de triplet (origine, moyen, destination) décrivant les arrêtes entre les noeuds
    (un peu comme RDF mais avec la différence que les moyens (prédicats) sont des noeuds et les relations sont ordonnées au sein de (origine, moyen))
    """
    @property
    @abstractmethod
    def max(self):
        raise NotImplementedError

    @abstractmethod
    def add_relation(self, fro, by, to):
        """
        Ajoute une relation au graphe à la fin de l'ordre

        :param fro: id du noeud origine
        :type fro: entier
        :param by: id du noeud moyen
        :type by: entier
        :param to: id du noeud destination
        :type to: entier
        """
        raise NotImplementedError

    @abstractmethod
    def get_relations_of(self, fro):
        """
        Donne l'ensemble des doublés (moyen, destination) du noeud donné en paramètre
        Renvois 'KeyError' si le noeuds oringine n'existe pas

        :param fro: id du noeud origine
        :type fro: entier
        :return: liste de doublé (moyen, [destinations])
        :rtype: iterable of tuple
        """
        raise NotImplementedError

    @abstractmethod
    def remove_first_relation(self, fro, by, to):
        """
        Retire la dernière relation donnée en paramètre
        Renvois 'KeyError' si la relation n'existe pas

        :param fro: id du noeud origine
        :type fro: entier
        :param by: id du noeud moyen
        :type by: entier
        :param to: id du noeud destination
        :type to: entier
        """
        raise NotImplementedError


class SimpleReseauConceptuelSimple(AbcReseauConceptuelSimple):
    """Implémentation simple de la classe abstraite avec des objets standard de python"""

    def __init__(self):
        self._data = {}
        self._max = 0

    @property
    def max(self):
        return self._max

    def add_relation(self, fro, by, to):
        """
        Ajoute une relation au graphe à la fin de l'ordre

        :param fro: id du noeud origine
        :type fro: entier
        :param by: id du noeud moyen
        :type by: entier
        :param to: id du noeud destination
        :type to: entier
        """

        self._max = max(self._max, fro, by, to)

        a = self._data.get(fro, {by: []})
        b = a.get(by, [])
        b.append(to)
        a[by] = b
        self._data[fro] = a

    def get_relations_of(self, fro):
        """
        Donne l'ensemble des doublés (moyen, destination) du noeud donné en paramètre
        Renvois 'KeyError' si le noeuds oringine n'existe pas

        :param fro: id du noeud origine
        :type fro: entier
        :return: liste de doublé (moyen, [destinations])
        :rtype: iterable of tuple
        """
        return [(b[0], b[1].copy()) for b in self._data[fro].items()]

    def remove_first_relation(self, fro, by, to):
        """
        Retire la dernière relation donnée en paramètre
        Renvois 'KeyError' si la relation n'existe pas

        :param fro: id du noeud origine
        :type fro: entier
        :param by: id du noeud moyen
        :type by: entier
        :param to: id du noeud destination
        :type to: entier
        """
        a = self._data[fro]
        b = a[by]
        try:
            b.remove(to)
        except ValueError as err:
            raise KeyError(str((fro, by, to)) + "not in network") from err
        if b == []:
            a.pop(by)
            if a == {}:
                self._data.pop(fro)
        else:
            a[by] = b
            self._data[fro] = a
