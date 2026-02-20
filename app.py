from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

# Initialisation de l'application Flask
app = Flask(__name__)

# Dictionnaire permettant de faire la correspondance entre les symboles d'opérations et leurs fonctions mathématiques
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    cette fonction analyse une chaîne de caractères mathématique simple et exécute l'opération.
    elle agit comme un parseur pour des expressions de type "a+b".
    Elle ne supporte actuellement qu'un seul opérateur par calcul.

    Args:
        expr (str): L'expression mathématique récupérée depuis l'interface.

    Returns:
        float: Le résultat numérique du calcul après exécution de la fonction correspondante.

    Raises:
        ValueError: Si l'expression est vide, mal formatée, contient plusieurs opérateurs, 
                    ou si les opérandes ne sont pas des nombres valides.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")
    # Nettoyage de la chaîne afin d'éviter les erreurs liées aux espaces involontaires et inutiles
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Recherche de la position de l'opérateur unique dans la chaîne
    for i, ch in enumerate(s):
        if ch in OPS:
            # cette section empêche les expressions complexes (ex: 100+200+300) non supportées
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # Vérification du fait que l'opérateur n'est pas au début ou à la fin (ex: "+100" ou "100+")
    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")
    
    # Découpage de la chaîne en deux parties autour de l'opérateur : la partie gauche (left) de l'opérateur et sa partie droite (right)
    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        # Conversion des segments en nombres flottants pour le calcul
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")
    
    # Appel dynamique de la fonction mathématique via le dictionnaire OPS
    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Cette fonction gère l'affichage initial de la calculatrice (GET) et le traitement
    des soumissions de formulaires (POST).

    Returns:
        str: Le rendu du template 'index.html' avec le résultat ou le message d'erreur.
    """
    result = ""
    if request.method == 'POST':
        # Récupération de la saisie utilisateur depuis le champ 'display' du formulaire
        expression = request.form.get('display', '')
        try:
            # Calcul du résultat
            result = calculate(expression)
        except Exception as e:
            # Capture de toutes les erreurs (division par zéro, mauvais format) pour l'affichage côté client
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Lancement de l'application en mode 'debug' pour faciliter la correction d'erreurs en rechargeant automatiquement le serveur à chaque modification du code 
    app.run(debug=True)
