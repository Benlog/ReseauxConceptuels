"""Statistical analysis tools for conceptual networks."""

from typing import List, Set, Tuple, TypeVar, Counter

T = TypeVar("T")


def count_ngrams(ngram: List[T], sequence: List[T]) -> int:
    """Count occurrences of an n-gram in a sequence.

    Args:
        ngram: The n-gram pattern to count
        sequence: The sequence to search in

    Returns:
        Number of occurrences of ngram in sequence
    """
    total = 0
    n = len(ngram)
    for i in range(len(sequence) - n + 1):
        if sequence[i : i + n] == ngram:
            total += 1
    return total


def liste_tout_ngram(liste: List[T]) -> Set[Tuple[T]]:
    """_summary_

    Args:
        liste (list[T]): _description_

    Returns:
        set[T]: _description_
    """

    ngram_temp = []
    for e in liste:
        ngram_temp.append([e])
        for e2 in ngram_temp[:-1]:
            e2.append(e)

    ngram_set = set()
    for e in ngram_temp:
        ngram_set.add(tuple(e))

    return ngram_set


def liste_tout_adjacents(liste: List[T]) -> List[List[List[T]]]:
    """Génère la liste de toutes les adjacences de taille 1 à n

    Args:
        liste (iter[T]): la liste dans laquelle optenir les adjacences

    Returns:
        liste[liste[T]]: la liste de liste des adjacences de taille n, puis
        n-1, puis n-2, ... jusqu'à 1
    """
    length = len(liste)

    return [
        [[liste[i3 + i2] for i3 in range(length - i)] for i2 in range(i + 1)]
        for i in range(length)
    ]


def set_ngram(liste: List[T]) -> List[Set[Tuple[T]]]:
    """Génère la liste de toutes les adjacences uniques de taille 1 à n

    Args:
        liste (iter[T]): la liste dans laquelle optenir les adjacences uniques

    Returns:
        liste[liste[Tuple(T)]]: la liste de liste des adjacences de taille n,
        puis n-1, puis n-2, ... jusqu'à 1
    """
    length = len(liste)
    return [
        set(tuple(liste[i3 + i2] for i3 in range(length - i)) for i2\
            in range(i + 1))
        for i in range(length)
    ]


def count_ngram(liste: List[T]) -> List[Counter[Tuple[T]]]:
    """Génère le compte de toutes les adjacences uniques de taille 1 à n

    Args:
        liste (iter[T]): la liste dans laquelle optenir les adjacences uniques

    Returns:
        liste[Counter[tuple[T]]]: la liste de compteur des adjacences de taille
        n, puis n-1, puis n-2, ... jusqu'à 1
    """
    length = len(liste)
    return [
        Counter(
            tuple(liste[i3 + i2] for i3 in range(length - i)) for i2\
                in range(i + 1)
        )
        for i in range(length)
    ]
