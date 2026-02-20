# Module : Templates
Ce répertoire contient les modèles HTML utilisés par le moteur de rendu de Flask pour générer l'interface utilisateur. Il définit la structure de la calculatrice et intègre la logique client (JavaScript) pour l'interaction immédiate.

## fcihier et Responsabilités
* **index.html** : 
    * Définit la structure DOM de la calculatrice.
    * Affiche dynamiquement les résultats provenant du serveur (`{{ result }}`).
    * Contient la logique JavaScript côté client pour la manipulation de l'affichage en temps réel.

## Dépendances
* **Moteur Jinja2** : Le fichier utilise des expressions entre doubles accolades pour la communication avec le serveur Flask.
* **Lien Statique** : Repose sur l'existence du fichier `style.css` dans le dossier `/static` via la fonction `url_for`.