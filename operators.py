def add(a,b):
    """
    Calcule l'addition de deux nombres.

    Args:
        a (float): Le premier nombre.
        b (float): Le deuxième nombre.

    Returns:
        float: Le résultat de l'addition (a + b).
    """
    return a + b

def subtract(a,b):
    """
    Calcule la soustraction de deux nombres.

    Args:
        a (float): Le premier nombre.
        b (float): Le deuxième nombre.

    Returns:
        float: Le résultat de la soustraction (a - b).
    """
    return a - b

def multiply(a,b):
    """
    Calcule la multiplication de deux nombres.

    Args:
        a (float): Le premier nombre.
        b (float): Le deuxième nombre.

    Returns:
        float: Le résultat de la multiplication (a * b).
    """
    return a * b

def divide(a,b):
    """
    Calcule la division de deux nombres.

    Args:
        a (float): Le premier nombre (le dividende).
        b (float): Le deuxième nombre (le diviseur).

    Returns:
        float: Le résultat de la division (a / b).
    Raises:
        ZeroDivisionError: Si le diviseur (b) est égal à zéro.
    """
    # app.py capturera la division par 0
    return a / b
