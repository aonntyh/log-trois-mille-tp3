# Module : Statique
Ce répertoire contient le fichier statique nécessaire à l'interface utilisateur de la calculatrice. Son rôle est de séparer la présentation visuelle de la logique métier et du balisage HTML, afin de faciliter la maintenance du design sans toucher au code source.

## Responsabilités
* **style.css** : Définit l'identité visuelle de l'application. 
    * Gère la mise en page responsive via Flexbox et CSS Grid.
    * Contient les styles spécifiques pour le boîtier de la calculatrice (`.calculator`), l'écran d'affichage (`#display`) et la grille de boutons (`.buttons`).
    * Définit les retours visuels interactifs (états `:hover` et `:active`) pour améliorer l'expérience utilisateur.

## Dépendances et utilisation
* **Utilisation** : Ce fichier doit être lié dans le `<head>` du fichier HTML principal via une balise `<link>`.
* **Dépendances** : Aucune bibliothèque externe n'est requise ; le style repose exclusivement sur du CSS.