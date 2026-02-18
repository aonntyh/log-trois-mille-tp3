from operators import add, subtract, multiply, divide

"""
Ce module contient les tests unitaires pour les opérations arithmétiques
"""

def test_add():
    """Teste l'addition de deux nombres."""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """Teste la soustraction de deux nombres."""
    assert subtract(5, 2) == 3
    assert subtract(2, 5) == -3

def test_multiply():
    """Teste la multiplication de deux nombres."""
    assert multiply(2, 3) == 6
    assert multiply(5, 0) == 0

def test_divide():
    """Teste la division de deux nombres."""
    assert divide(10, 2) == 5.0
    assert divide(5, 2) == 2.5
