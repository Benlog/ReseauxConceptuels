"""Interpreter classes for conceptual networks."""

from abc import ABC, abstractmethod
from typing import Any
from reseaux_conceptuels_simple import AbcReseauConceptuelSimple


class AbcInterpreteur(ABC):
    """Base class for network interpreters."""

    def __init__(self):
        pass

    def __call__(self, network: AbcReseauConceptuelSimple, node: int) -> Any:
        """Interpret the network starting from the given node.

        Args:
            network: The conceptual network to interpret
            node: Starting node ID

        Returns:
            The interpretation result
        """
        return self.interpret(network, node)

    @abstractmethod
    def interpret(self, network: AbcReseauConceptuelSimple, node: int) -> Any:
        """Implement the interpretation logic."""
        raise NotImplementedError
