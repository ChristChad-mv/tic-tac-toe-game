# TIC-TAC-TOE

## Bienvenue dans la documentation du TIC-TAC-TOE

Cette documentation est dédiée au projet **TIC-TAC-TOE** et sert de manuel de référence. Elle fournit des explications détaillées pour chaque classe et fonction utilisées dans le développement de ce jeu.

---

## Bref descriptif du projet

Ce projet de développement d’application s’inscrit dans le cadre de l’Unité d’Enseignement **Génie Logiciel et Algorithmes** de notre formation (S5).  
L’objectif est de concevoir le jeu classique **TIC-TAC-TOE** avec de nouvelles fonctionnalités, en permettant à un joueur humain d'affronter un ordinateur (une AI) utilisant l’algorithme **Minimax** pour prendre des décisions optimales.

---

## Réalisation

- **MVOUNGOU Christ Chadrak**  
- **MERABTENE Radia**

---

## Comment faire fonctionner le projet

1. **Installer Python 3**  
   - Si vous êtes sous Linux ou macOS, vous pouvez installer Python 3 via votre gestionnaire de paquets (ex. `apt-get`, `brew`) ou télécharger directement depuis [python.org](https://www.python.org/downloads/).  
   - Sous Windows, vous pouvez télécharger l’installateur sur [python.org](https://www.python.org/downloads/windows/) et l’installer ensuite.

2. **Installer les bibliothèques nécessaires**  
   - **Tkinter** : Elle est généralement installée par défaut avec Python sur la plupart des systèmes.  
   - **Pillow** pour la gestion et le traitement des images :  
     ```bash
     pip install Pillow
     ```
     Si cela ne fonctionne pas, vous pouvez essayer :
     ```bash
     pip3 install Pillow
     ```

3. **Lancer le jeu**  
   - Placez-vous dans le répertoire racine du projet (là où se trouve `main.py`)  
   - Exécutez la commande :
     ```bash
     python3 main.py
     ```
   - Le jeu devrait alors se lancer avec son interface graphique.

4. **Problème d’affichage de l'image en arrière-plan ?**  
   - En cas d’erreur liée au chargement de l’image, vérifiez le chemin de l’image.  
   - Modifiez le chemin vers l'image dans le code en utilisant un chemin absolu ou un chemin correct relatif à votre configuration de fichiers.

---

## Générer et consulter la documentation avec Doxygen

Le projet contient une documentation générée via **Doxygen**. Pour la consulter :

1. Assurez-vous d’avoir généré ou de disposer du dossier `documentation/html` (créé par Doxygen).
2. Ouvrez un terminal et placez-vous dans le répertoire :  
   ```bash
   cd documentation/html
   ```
3. Lancez un server HTTP:
  ```bash
  python3 -m http.server 8000
  ```
4. Tapez cet URL dans votre navigateur 
  [http://localhost:8000](http://localhost:8000)
