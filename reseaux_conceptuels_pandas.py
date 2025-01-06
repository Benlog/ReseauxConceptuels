"""Implementation of conceptual networks using pandas DataFrame."""

from typing import List, Tuple
import pandas as pd
from reseaux_conceptuels_simple import AbcReseauConceptuelSimple


class PandaReseauConceptuelSimple(AbcReseauConceptuelSimple):
    """Pandas implementation of conceptual networks."""

    def __init__(self):
        self._reseau = pd.DataFrame(
            columns=["from", "by", "to"],
            dtype={"from": int, "by": int, "to": int}
        )
        self._max = 0

    @property
    def max(self) -> int:
        """Return the maximum node ID."""
        return self._max

    def add_relation(self, fro: int, by: int, to: int) -> None:
        """Add a new relation to the network."""
        self._max = max(self._max, fro, by, to)
        new_row = pd.DataFrame({"from": [fro], "by": [by], "to": [to]})
        self._reseau = pd.concat([self._reseau, new_row], ignore_index=True)

    def get_relations_of(self, fro: int) -> List[Tuple[int, List[int]]]:
        """Get all relations for a given origin node."""
        if fro not in self._reseau["from"].values:
            raise KeyError(f"Node {fro} not found")

        relations = self._reseau[self._reseau["from"] == fro]
        result = []
        for by in relations["by"].unique():
            to_list = relations[relations["by"] == by]["to"].tolist()
            result.append((by, to_list))
        return result

    def remove_first_relation(self, fro: int, by: int, to: int) -> None:
        """Remove the first occurrence of a relation."""
        mask = (
            (self._reseau["from"] == fro)
            & (self._reseau["by"] == by)
            & (self._reseau["to"] == to)
        )
        if not mask.any():
            raise KeyError(f"Relation ({fro}, {by}, {to}) not found")
        idx = self._reseau[mask].index[0]
        self._reseau.drop(idx, inplace=True)
