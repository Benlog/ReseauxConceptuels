import pandas as pd

class ReseauConceptuel :

    def __init__(self):
        self.reseau = pd.DataFrame(columns=["from","by","to"], dtype={"from" : int, "by" : int,"to" : int})

    def addRelation(self, fro, by, to):
        self.reseau.append({"from" : fro, "by" : by, "to" : to}, True)

    def removeLastRelation(self, fro, by, to):
        t = self.reseau[ (self.reseau["from"] == fro) & (self.reseau["by"] == by) & (self.reseau["to"] == to)]
        if t.size > 0:
            self.reseau.drop(t.index[-1], inplace = True)