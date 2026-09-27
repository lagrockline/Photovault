# PhotoVault v0.2

PhotoVault est un utilitaire Python conçu pour optimiser le stockage des photothèques iPhone en extrayant la partie vidéo des Live Photos sans altérer les images d'origine, tout en éliminant les doublons stricts.

## 📋 Prérequis & Préparation

Avant de lancer le script, vous devez extraire vos médias de votre appareil :
1. **Exportation depuis l'iPhone** : Connectez votre iPhone à votre ordinateur et exportez l'intégralité de vos photos/vidéos dans un dossier local. 
   *(Note : Pour un fonctionnement optimal avec ce script, veillez à exporter les **Originaux non modifiés** afin de conserver la structure HEIC + MOV des Live Photos).*
2. **Dossier Source** : Ce dossier d'export brut servira de répertoire `source` pour le script.
3. **Dossier Destination** : Créez un dossier vide qui servira de répertoire `destination` propre.

## ✨ Fonctionnalités
- **Filtre Live Photos (v0.1)** : Identifie et écarte les composants vidéo (`.mov`) liés à des images fixes (`.heic`).
- **Préservation Intégrale (v0.1)** : Conserve les images fixes ainsi que les véritables vidéos indépendantes.
- **Détection des Doublons (v0.1)** : Analyse l'empreinte numérique SHA-1 par blocs pour bloquer les doublons stricts.
- **Rapport de Rentabilité (v0.1)** : Calcule l'espace disque exact économisé à la fin de l'exécution.
- **Barres de Progression Dynamiques (v0.2)** : Affiche l'avancement en temps réel (indexation et traitement) dans le terminal sans dépendance externe.

## 📂 Structure du Projet
- `photovault.py` : Point d'entrée de l'application (configuration des chemins).
- `scanner.py` : Logique centrale de l'analyse, du filtrage et de la copie des médias.
- `media.py` : Classe de modélisation orientée objet des fichiers.
- `utils.py` : Fonctions utilitaires, notamment le calcul du hachage SHA-1 par blocs.

## 🚀 Utilisation
1. Ouvrez `photovault.py` et configurez les chemins de vos dossiers `source` (votre export iPhone) et `destination` (votre dossier propre).
2. Exécutez le script dans votre terminal :
   ```bash
   python3 photovault.py
   ```

## 📱 Restitution sur l'iPhone via iTunes / Finder

Une fois le traitement terminé, le dossier `destination` contient votre photothèque épurée. Suivez scrupuleusement cette procédure physique locale pour réimporter vos fichiers et libérer votre espace de stockage :

### Étape 1 : Nettoyage complet de l'appareil
1. Sur l'iPhone, ouvrez l'application **Photos**, sélectionnez toutes les photos et supprimez-les.
2. Allez dans l'album **Supprimés récemment** et videz-le définitivement.
3. **Important (iCloud)** : Si le stockage reste bloqué par des données fantômes, désactivez temporairement la synchronisation iCloud ou les albums partagés dans vos réglages, effectuez un redémarrage de l'iPhone, puis vérifiez que l'espace disponible a bien augmenté dans *Réglages > Général > Stockage iPhone*.

### Étape 2 : Configuration du transfert dans iTunes / Finder
1. Branchez votre iPhone en USB sur votre ordinateur et ouvrez **iTunes** (ou le **Finder** sous macOS).
2. Cliquez sur l'icône de votre **iPhone** pour accéder à sa gestion.
3. Dans le menu latéral, cliquez sur l'onglet **Photos**.
4. Cochez la case **"Synchroniser les photos"**.
5. Sur la ligne *"Copier les photos depuis :"*, ouvrez le menu déroulant, cliquez sur **"Choisir un dossier..."** et sélectionnez votre dossier `destination` (le répertoire épuré).
6. **Configuration des cases à cocher** :
   - 🟩 **Cocher obligatoirement : "Inclure les vidéos"** (pour ne pas bloquer les vraies vidéos indépendantes préservées par le script).
   - ⬜ **Décocher : "Conserver l'organisation des dossiers"** (pour laisser l'iPhone fusionner le tout directement dans le flux principal).

### Étape 3 : Exécution du transfert
1. Cliquez sur **Appliquer** (ou **Synchroniser**) en bas à droite.
2. Suivez l'avancement du transfert dans la barre supérieure du logiciel. **Ne débranchez pas le câble** avant la fin complète de l'opération.
3. Une fois terminé, l'iPhone va lire les données **EXIF** natives de chaque fichier. Vos photos et vidéos vont se reclasser automatiquement à leurs **dates et heures de prise de vue d'origine** dans votre chronologie. Les algorithmes d'iOS reconstruiront vos Souvenirs en tâche de fond lors des prochaines recharges sur secteur.
