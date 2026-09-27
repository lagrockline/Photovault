# PhotoVault v0.2

PhotoVault est un utilitaire Python conçu pour optimiser le stockage des photothèques iPhone exportées en extrayant la partie vidéo des Live Photos sans altérer les images d'origine.

## Fonctionnalités
- **Filtre Live Photos (v0.1)** : Identifie et écarte les composants vidéo (`.mov`) liés à des images fixes (`.heic`).
- **Préservation Intégrale (v0.1)** : Conserve les images fixes ainsi que les véritables vidéos indépendantes.
- **Détection des Doublons (v0.1)** : Analyse l'empreinte numérique SHA-1 par blocs pour bloquer les doublons stricts.
- **Rapport de Rentabilité (v0.1)** : Calcule l'espace disque exact économisé à la fin de l'exécution.
- **Barres de Progression Dynamiques (v0.2)** : Affiche l'avancement en temps réel (indexation et traitement) dans le terminal sans dépendance externe.

## Structure du Projet
- `photovault.py` : Point d'entrée de l'application.
- `scanner.py` : Logique centrale de l'analyse, du filtrage et de la copie des médias.
- `media.py` : Classe de modélisation orientée objet des fichiers.
- `utils.py` : Fonctions utilitaires, notamment le calcul du hachage SHA-1.

## Utilisation
1. Configurer les chemins source et destination dans `photovault.py`.
2. Exécuter le script :
   ```bash
   python3 photovault.py
   ```
