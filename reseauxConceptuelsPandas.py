import pandas as pd
from reseauxConceptuelsSimple import AbcReseauConceptuelSimple

class PandaReseauConceptuelSimple(AbcReseauConceptuelSimple) :
    """_summary_

    Args:
        AbcReseauConceptuelSimple (_type_): _description_
    """

    def __init__(self):
        self.reseau = pd.DataFrame(columns=["from","by","to"], dtype={"from" : int, "by" : int,"to" : int})

    def add_relation(self, fro, by, to):
        self.reseau.append({"from" : fro, "by" : by, "to" : to}, True)

    #def get_relations_of

    def remove_first_relation(self, fro, by, to):
        t = self.reseau[ (self.reseau["from"] == fro) & (self.reseau["by"] == by) & (self.reseau["to"] == to)]
        if t.size > 0:
            self.reseau.drop(t.index[0], inplace = True)

    #def removeLastRelation(self, fro, by, to):
    #    t = self.reseau[ (self.reseau["from"] == fro) & (self.reseau["by"] == by) & (self.reseau["to"] == to)]
    #    if t.size > 0:
    #        self.reseau.drop(t.index[-1], inplace = True)