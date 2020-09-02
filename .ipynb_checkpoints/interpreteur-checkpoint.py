from abc import ABC, abstractmethod

class AbcInterpreteur(ABC) :
    '''
    Classe de base pour les interpréteurs
    '''
    
    def __init__(self):
        super().__init__()
        
    def __call__(self, reseau, noeud):
        '''
        Appelle l'interpréteur sur le réseau à partir du noeud donné
        
        :param reseau: reseau conceptuel à utiliser
        :type reseau: AbcReseauConceptuel
        :param noeud: noeud de départ
        '''
        pass