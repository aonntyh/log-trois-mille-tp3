# Documentation des tests

Ce répertoire contient les tests unitaires du projet.

## Procédure d'exécution

Pour lancer l'ensemble des tests, exécutez la commande suivante depuis le root du projet :

```bash
uv run pytest
```

## Couverture des tests

La suite de tests est structurée en deux modules :

1. Validation des opérateurs (`test_operators.py`) :
   - Vérification des opérations arithmétiques (addition, soustraction, multiplication et division).

2. Validation de la logique plus générale (`test_app.py`) :
  - Vérification du traitement des expressions soumises par l'utilisateur
  - Validation de la gestion des erreurs et des cas limites.