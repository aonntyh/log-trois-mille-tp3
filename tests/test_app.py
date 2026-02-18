import pytest
from app import calculate

"""
Ce module contient des tests unitaires pour la logique de calcul.
"""

def test_calculate_valid():
    """Vérifie que le calcul d'expressions valides retourne le bon résultat."""
    assert calculate("1 + 2") == 3
    assert calculate("5 - 2") == 3
    assert calculate("2 * 3") == 6
    assert calculate("10 / 2") == 5.0

def test_calculate_invalid_format():
    """Vérifie la gestion des formats d'expression invalides."""
    with pytest.raises(ValueError, match="invalid expression format"):
        calculate("1")
    with pytest.raises(ValueError, match="invalid expression format"):
        calculate("+1")
    with pytest.raises(ValueError, match="invalid expression format"):
        calculate("1+")

def test_calculate_multiple_operators():
    """Vérifie qu'un seul opérateur est autorisé par expression."""
    with pytest.raises(ValueError, match="only one operator is allowed"):
        calculate("1 + 2 + 3")

def test_calculate_non_numeric():
    """Vérifie que les opérandes doivent être des nombres."""
    with pytest.raises(ValueError, match="operands must be numbers"):
        calculate("a + b")

def test_calculate_empty():
    """Vérifie la gestion d'une expression vide."""
    with pytest.raises(ValueError, match="empty expression"):
        calculate("")
