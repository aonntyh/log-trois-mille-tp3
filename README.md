# Description du projet
Ce projet consiste en une application web de calculatrice simple développée avec le micro-framework Flask. Il permet d'effectuer des opérations arithmétiques de base (addition, soustraction, multiplication et division) via une interface utilisateur intuitive.
L'application a été restructurée pour suivre les meilleures pratiques de développement : séparation de la logique métier et la présentation, documentation complète du code et mise en place d'un environnement robuste pour la collaboration sur GitHub.

# Guide d'installation
Suivez les instructions suivantes pour configurer l'environnement de développement local :

1. clonez le dépôt :
git clone https://github.com/aonntyh/log-trois-mille-tp3.git

2. Installer les dépendances avec uv :
uv sync

# Instructions d'utilisation
1. Lancement de l'application

Pour démarrer le serveur de développement, exécutez la commande suivante à la racine du projet :
uv run python app.py

2. Fonctionnalités

Saisie interactive : Utilisez le pavé numérique affiché à l'écran pour composer vos expressions.

Calcul serveur : Les calculs sont traités côté back-end pour garantir la précision.

Gestion d'erreurs : L'interface affiche des messages explicites en cas de division par zéro ou de format d'expression invalide

# Tests
Pour lancer les tests, exécutez la commande suivante :
uv run pytest

# Flux de contribution
Pour maintenir la qualité de la base de code, nous utilisons le flux de travail suivant :

1. Issues : Toute modification ou correction de bogue doit être documentée par une Issue sur GitHub.

2. Branches : Ne travaillez jamais directement sur main. Créez une branche thématique :

feature/nom-de-la-fonctionnalite

fix/description-du-bug

3. Pull Request : Soumettez vos modifications via une Pull Request. Le code doit être documenté avec des docstrings et des commentaires clairs avant d'être fusionné.
